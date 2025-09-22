"""
Utilitários para a aplicação Streamlit de consulta CPF e-SAJ
"""

import re
import pandas as pd
import requests
import logging
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from config import ESAJ_CONFIG, HEADERS, LOG_CONFIG

def normalizar_cpf(cpf: str) -> str:
    """
    Normaliza CPF removendo caracteres especiais e preenchendo com zeros à esquerda
    
    Args:
        cpf: CPF em qualquer formato
        
    Returns:
        CPF normalizado com 11 dígitos (zeros à esquerda preservados)
    """
    cpf_limpo = re.sub(r'\D', '', str(cpf))
    
    # Se tem menos de 11 dígitos, preencher com zeros à esquerda
    if len(cpf_limpo) < 11:
        return cpf_limpo.zfill(11)
    
    # Se tem exatamente 11 dígitos, retornar como está
    if len(cpf_limpo) == 11:
        return cpf_limpo
    
    # Se tem mais de 11 dígitos, truncar à direita (manter os primeiros 11)
    return cpf_limpo[:11]

def validar_cpf(cpf: str) -> bool:
    """
    Valida CPF usando algoritmo de verificação
    
    Args:
        cpf: CPF para validar
        
    Returns:
        True se CPF é válido, False caso contrário
    """
    cpf_original = cpf
    cpf = normalizar_cpf(cpf)
    
    # Verificar se tem 11 dígitos e não é sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    return cpf[-2:] == f"{digito1}{digito2}"

def processar_csv(uploaded_file) -> Tuple[Optional[pd.DataFrame], Optional[pd.DataFrame]]:
    """
    Processa arquivo CSV e valida CPFs
    
    Args:
        uploaded_file: Arquivo CSV carregado
        
    Returns:
        Tupla com (cpfs_validos, cpfs_invalidos) ou (None, None) se erro
    """
    try:
        # Ler CSV - IMPORTANTE: tratar coluna CPF como string para preservar zeros à esquerda
        df = pd.read_csv(uploaded_file, dtype={'CPF': str, 'cpf': str})
        
        # Verificar colunas necessárias (aceitar 'Nome' e 'CPF' ou 'nome' e 'cpf')
        if 'CPF' in df.columns and 'Nome' in df.columns:
            # Renomear colunas para minúsculas para padronização
            df = df.rename(columns={'CPF': 'cpf', 'Nome': 'nome'})
        elif 'cpf' in df.columns and 'nome' in df.columns:
            pass  # Já está no formato correto
        else:
            raise ValueError("CSV deve conter colunas 'CPF' e 'Nome' (ou 'cpf' e 'nome')")
        
        # Normalizar CPFs (aceitar 9-11 dígitos)
        df["cpf_normalizado"] = df["cpf"].apply(normalizar_cpf)
        
        # Verificar se CPF tem entre 9 e 11 dígitos antes da normalização
        df["cpf_tamanho_ok"] = df["cpf"].apply(lambda x: 9 <= len(re.sub(r'\D', '', str(x))) <= 11)
        
        # Validar CPFs apenas se tiverem tamanho adequado
        df["cpf_valido"] = df.apply(lambda row: validar_cpf(row["cpf"]) if row["cpf_tamanho_ok"] else False, axis=1)
        
        # Separar válidos e inválidos
        cpfs_validos = df[df["cpf_valido"] == True].copy()
        cpfs_invalidos = df[df["cpf_valido"] == False].copy()
        
        return cpfs_validos, cpfs_invalidos
        
    except Exception as e:
        raise Exception(f"Erro ao processar CSV: {str(e)}")

def extrair_processos_html(html: str) -> List[Dict]:
    """
    Extrai informações dos processos do HTML do e-SAJ
    
    Args:
        html: Conteúdo HTML da resposta
        
    Returns:
        Lista de dicionários com informações dos processos
    """
    processos = []
    
    try:
        # Buscar todas as seções de processo
        processos_matches = re.findall(
            r'<li>\s*<div id="divProcesso[^"]*"[^>]*>.*?</div>\s*</li>', 
            html, 
            re.DOTALL
        )
        
        for processo_html in processos_matches:
            # Extrair número do processo
            numero_match = re.search(r'class="linkProcesso"[^>]*>\s*([^<\s]+)', processo_html)
            numero_processo = numero_match.group(1).strip() if numero_match else ""
            
            # Extrair classe do processo
            classe_match = re.search(r'<div class="classeProcesso">([^<]+)</div>', processo_html)
            classe_processo = classe_match.group(1).strip() if classe_match else ""
            
            # Extrair data do recebimento
            data_match = re.search(r'<div class="dataLocalDistribuicaoProcesso">([^<]+?)\s*-', processo_html)
            data_processo = data_match.group(1).strip() if data_match else ""
            
            if numero_processo and classe_processo and data_processo:
                processos.append({
                    "numero": numero_processo,
                    "classe": classe_processo,
                    "data": data_processo
                })
    
    except Exception as e:
        print(f"Erro ao extrair processos: {e}")
    
    return processos

def extrair_nome_html(html: str) -> str:
    """
    Extrai nome do requerente do HTML do e-SAJ
    
    Args:
        html: Conteúdo HTML da resposta
        
    Returns:
        Nome extraído ou string vazia
    """
    try:
        nome_match = re.search(r'<div class="unj-base-alt nomeParte">\s*([^<]+)', html)
        return nome_match.group(1).strip() if nome_match else ""
    except Exception:
        return ""

def formatar_resposta_consulta(cpf: str, nome: str, nome_extraido: str, processos: List[Dict]) -> str:
    """
    Formata resposta da consulta para exibição
    
    Args:
        cpf: CPF consultado
        nome: Nome original do CSV
        nome_extraido: Nome extraído do e-SAJ
        processos: Lista de processos encontrados
        
    Returns:
        Resposta formatada
    """
    resposta = f"🔍 Consulta sistema do Tribunal Judiciário\n\n"
    resposta += f"Prezado(a) {nome_extraido or nome}, CPF: {cpf}\n\n"
    
    if processos:
        resposta += f"📋 Localizamos os seguintes requerimentos:\n"
        for processo in processos:
            resposta += f"🔹 {processo['data']} {processo['numero']} {processo['classe']}\n"
    else:
        resposta += f"❌ Nenhum processo encontrado\n"
    
    resposta += f"\n🏛️ Consulta oficial realizada no sistema do Tribunal de Justiça às {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    
    return resposta

def gerar_nome_arquivo(tipo: str, extensao: str = "csv") -> str:
    """
    Gera nome de arquivo com timestamp
    
    Args:
        tipo: Tipo do arquivo (ex: "encontrados", "nao_encontrados")
        extensao: Extensão do arquivo
        
    Returns:
        Nome do arquivo com timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"cpfs_{tipo}_{timestamp}.{extensao}"

def reformatar_dados_para_csv(resultados_encontrados: List[Dict]) -> pd.DataFrame:
    """
    Reformatar dados para CSV com uma linha por processo
    
    Args:
        resultados_encontrados: Lista de resultados encontrados
        
    Returns:
        DataFrame reformatado
    """
    dados_reformatados = []
    
    for resultado in resultados_encontrados:
        cpf = resultado['cpf']
        nome = resultado['nome']
        nome_extraido = resultado['nome_extraido']
        data_consulta = resultado['data_consulta']
        processos = resultado['processos']
        
        if processos and len(processos) > 0:
            # Para cada processo, criar uma linha
            for i, processo in enumerate(processos, 1):
                dados_reformatados.append({
                    'CPF': cpf,
                    'Nome': nome,
                    'Nome_Extraido': nome_extraido,
                    'Sequencia_Processo': i,
                    'Numero_Processo': processo['numero'],
                    'Classe_Processo': processo['classe'],
                    'Data_Processo': processo['data'],
                    'Data_Consulta': data_consulta
                })
        else:
            # Se não tem processos, criar uma linha vazia
            dados_reformatados.append({
                'CPF': cpf,
                'Nome': nome,
                'Nome_Extraido': nome_extraido,
                'Sequencia_Processo': 0,
                'Numero_Processo': '',
                'Classe_Processo': '',
                'Data_Processo': '',
                'Data_Consulta': data_consulta
            })
    
    return pd.DataFrame(dados_reformatados)

def calcular_estatisticas(resultados_encontrados: List[Dict], resultados_nao_encontrados: List[Dict]) -> Dict:
    """
    Calcula estatísticas dos resultados
    
    Args:
        resultados_encontrados: Lista de CPFs encontrados
        resultados_nao_encontrados: Lista de CPFs não encontrados
        
    Returns:
        Dicionário com estatísticas
    """
    total_encontrados = len(resultados_encontrados)
    total_nao_encontrados = len(resultados_nao_encontrados)
    total_processos = sum(r.get("total_processos", 0) for r in resultados_encontrados)
    
    return {
        "total_encontrados": total_encontrados,
        "total_nao_encontrados": total_nao_encontrados,
        "total_processos": total_processos,
        "total_consultados": total_encontrados + total_nao_encontrados
    }

def configurar_logging():
    """
    Configura o sistema de logging
    """
    logging.basicConfig(
        level=getattr(logging, LOG_CONFIG["log_level"]),
        format=LOG_CONFIG["log_format"],
        handlers=[
            logging.FileHandler(LOG_CONFIG["log_file"], encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def consultar_esaj(cpf: str, nome: str) -> Dict:
    """
    Consulta CPF no e-SAJ TJSP (baseado no n8n que funciona)
    
    Args:
        cpf: CPF para consultar
        nome: Nome da pessoa
        
    Returns:
        Dicionário com resultado da consulta
    """
    logger = configurar_logging()
    
    try:
        logger.info(f"🔍 Iniciando consulta CPF: {cpf} - {nome}")
        
        # Parâmetros da consulta (baseado no n8n)
        params = {
            "conversationId": "",
            "cbPesquisa": "DOCPARTE",
            "dadosConsulta.valorConsulta": cpf,
            "consultaDeRequisitorios": "true"
        }
        
        logger.info(f"📡 Enviando requisição para: {ESAJ_CONFIG['base_url']}")
        logger.info(f"📋 Parâmetros: {params}")
        
        # Fazer requisição GET (como no n8n)
        response = requests.get(
            ESAJ_CONFIG['base_url'],
            params=params,
            headers=HEADERS,
            timeout=ESAJ_CONFIG['timeout']
        )
        
        logger.info(f"📊 Status da resposta: {response.status_code}")
        logger.info(f"📏 Tamanho da resposta: {len(response.text)} caracteres")
        
        if response.status_code != 200:
            logger.error(f"❌ Erro HTTP: {response.status_code}")
            return {
                "sucesso": False,
                "erro": f"Erro HTTP {response.status_code}",
                "status_code": response.status_code,
                "html": response.text[:500] + "..." if len(response.text) > 500 else response.text
            }
        
        html = response.text
        logger.info(f"📄 HTML recebido: {len(html)} caracteres")
        
        # Verificar se tem processos encontrados
        has_processes = "Processos encontrados" in html or "linkProcesso" in html
        
        if not has_processes:
            logger.info(f"❌ Nenhum processo encontrado para CPF: {cpf}")
            return {
                "sucesso": True,
                "encontrado": False,
                "nome_extraido": "",
                "processos": [],
                "total_processos": 0,
                "html": html[:500] + "..." if len(html) > 500 else html
            }
        
        logger.info(f"✅ Processos encontrados para CPF: {cpf}")
        
        # Extrair nome do requerente
        nome_extraido = extrair_nome_html(html)
        logger.info(f"👤 Nome extraído: {nome_extraido}")
        
        # Extrair processos
        processos = extrair_processos_html(html)
        logger.info(f"📋 Processos extraídos: {len(processos)}")
        
        for i, processo in enumerate(processos):
            logger.info(f"  {i+1}. {processo['numero']} - {processo['classe']} - {processo['data']}")
        
        return {
            "sucesso": True,
            "encontrado": True,
            "nome_extraido": nome_extraido,
            "processos": processos,
            "total_processos": len(processos),
            "html": html[:500] + "..." if len(html) > 500 else html
        }
        
    except requests.exceptions.Timeout:
        logger.error(f"⏰ Timeout na consulta CPF: {cpf}")
        return {
            "sucesso": False,
            "erro": "Timeout na consulta",
            "timeout": True
        }
    except requests.exceptions.RequestException as e:
        logger.error(f"🌐 Erro de rede na consulta CPF {cpf}: {str(e)}")
        return {
            "sucesso": False,
            "erro": f"Erro de rede: {str(e)}",
            "network_error": True
        }
    except Exception as e:
        logger.error(f"💥 Erro inesperado na consulta CPF {cpf}: {str(e)}")
        return {
            "sucesso": False,
            "erro": f"Erro inesperado: {str(e)}",
            "unexpected_error": True
        }
