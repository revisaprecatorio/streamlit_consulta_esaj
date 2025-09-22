# 📋 Documentação Completa - Revisa Consulta CPF e-SAJ

## 🎯 Visão Geral

A aplicação **Revisa Consulta CPF e-SAJ** é uma interface web desenvolvida em Streamlit que permite consultar CPFs em lote no sistema e-SAJ do Tribunal de Justiça de São Paulo (TJSP). A aplicação processa arquivos CSV, valida CPFs, realiza consultas sequenciais no e-SAJ e gera relatórios detalhados.

## 🏗️ Arquitetura

### Estrutura de Arquivos
```
UI-streamlit/
├── app.py                 # Aplicação principal Streamlit
├── config.py             # Configurações da aplicação
├── utils.py              # Funções utilitárias
├── requirements.txt      # Dependências Python
├── run.sh               # Script de execução
├── exemplo_entrada.csv  # Arquivo de exemplo
├── README.md            # Documentação básica
└── DOCUMENTACAO_COMPLETA.md  # Esta documentação
```

### Componentes Principais

1. **Interface Streamlit** (`app.py`)
   - Upload de arquivos CSV
   - Processamento e validação de dados
   - Consultas sequenciais no e-SAJ
   - Exibição de resultados e downloads

2. **Configurações** (`config.py`)
   - URLs e parâmetros do e-SAJ
   - Headers HTTP para simular navegador
   - Configurações de validação e logging

3. **Utilitários** (`utils.py`)
   - Normalização e validação de CPFs
   - Processamento de HTML do e-SAJ
   - Funções auxiliares

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação Automática
```bash
cd UI-streamlit
chmod +x run.sh
./run.sh
```

### Instalação Manual
```bash
cd UI-streamlit
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
pip install -r requirements.txt
streamlit run app.py
```

### Acesso
- **URL Local**: http://localhost:8501
- **URL Rede**: http://[seu-ip]:8501

## 📊 Formato de Entrada

### Estrutura do CSV
O arquivo CSV deve conter as seguintes colunas (case-insensitive):

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `Nome` ou `nome` | String | Nome da pessoa | "João Silva" |
| `CPF` ou `cpf` | String | CPF (9-11 dígitos) | "12345678901" |

### Exemplo de CSV
```csv
Nome,CPF
João Silva,12345678901
Maria Santos,98765432100
Pedro Costa,11122233344
```

### Validação de CPF
- **Aceita**: 9 a 11 dígitos
- **Normalização**: Preenche com zeros à esquerda para 11 dígitos
- **Validação**: Algoritmo oficial de verificação de CPF
- **Exemplos**:
  - `123456789` → `00123456789`
  - `12345678901` → `12345678901` (mantém como está)

## 🔧 Funcionalidades

### 1. Upload e Validação
- **Upload de CSV**: Interface drag-and-drop
- **Validação de colunas**: Verifica presença de `Nome` e `CPF`
- **Normalização de CPF**: Converte para formato padrão
- **Validação de CPF**: Verifica dígitos verificadores

### 2. Consulta e-SAJ
- **Consulta sequencial**: Processa CPFs um por vez
- **Delay configurável**: 1-5 segundos entre consultas
- **Headers anti-bot**: Simula navegador real
- **Logging detalhado**: Registra todas as operações

### 3. Processamento de Respostas
- **Extração de dados**: Nome, processos, datas
- **Detecção de erros**: Identifica CPFs não encontrados
- **Formatação**: Gera respostas estruturadas

### 4. Relatórios e Downloads
- **Métricas**: Contadores de encontrados/não encontrados
- **CSV Encontrados**: Uma linha por processo
- **CSV Não Encontrados**: Lista de CPFs sem processos
- **Preview**: Visualização dos dados na interface

## 📋 Formato de Saída

### CSV Encontrados
Cada processo gera uma linha separada:

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| `CPF` | CPF consultado | "12345678901" |
| `Nome` | Nome do CSV | "João Silva" |
| `Nome_Extraido` | Nome do e-SAJ | "João Silva Santos" |
| `Sequencia_Processo` | Ordem do processo | 1, 2, 3... |
| `Numero_Processo` | Número do processo | "1234567-89.2023.8.26.0500" |
| `Classe_Processo` | Tipo do processo | "Precatório" |
| `Data_Processo` | Data de recebimento | "15/03/2023" |
| `Data_Consulta` | Data da consulta | "2023-09-21 10:30:00" |

### CSV Não Encontrados
| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| `nome` | Nome do CSV | "João Silva" |
| `cpf` | CPF consultado | "12345678901" |
| `motivo` | Motivo da não localização | "Não encontrado no e-SAJ" |
| `data_consulta` | Data da consulta | "2023-09-21 10:30:00" |

## ⚙️ Configurações

### Headers HTTP
```python
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36...",
    "Referer": "https://esaj.tjsp.jus.br/cpopg/abrirConsultaDeRequisitorios.do",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9...",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    # ... outros headers
}
```

### Configurações do e-SAJ
```python
ESAJ_CONFIG = {
    "base_url": "https://esaj.tjsp.jus.br/cpopg/search.do",
    "timeout": 30,
    "delay_min": 1,
    "delay_max": 5,
    "delay_default": 2
}
```

## 📝 Logging

### Arquivo de Log
- **Localização**: `consulta_esaj.log`
- **Formato**: `%(asctime)s - %(levelname)s - %(message)s`
- **Nível**: INFO

### Exemplo de Log
```
2023-09-21 10:30:15,123 - INFO - 🔍 Iniciando consulta CPF: 12345678901 - João Silva
2023-09-21 10:30:15,124 - INFO - 📡 Enviando requisição para: https://esaj.tjsp.jus.br/cpopg/search.do
2023-09-21 10:30:15,125 - INFO - 📋 Parâmetros: {'conversationId': '', 'cbPesquisa': 'DOCPARTE', 'dadosConsulta.valorConsulta': '12345678901', 'consultaDeRequisitorios': 'true'}
2023-09-21 10:30:16,234 - INFO - 📊 Status da resposta: 200
2023-09-21 10:30:16,235 - INFO - 📏 Tamanho da resposta: 75240 caracteres
2023-09-21 10:30:16,236 - INFO - ✅ Processos encontrados para CPF: 12345678901
2023-09-21 10:30:16,237 - INFO - 👤 Nome extraído: João Silva Santos
2023-09-21 10:30:16,238 - INFO - 📋 Encontradas 2 seções de processo
2023-09-21 10:30:16,239 - INFO - ✅ Processo extraído: 1234567-89.2023.8.26.0500 - Precatório - 15/03/2023
```

## 🔍 Detalhes Técnicos

### Normalização de CPF
```python
def normalizar_cpf(cpf):
    cpf_limpo = re.sub(r'\D', '', str(cpf))
    
    if len(cpf_limpo) < 11:
        return cpf_limpo.zfill(11)  # Preenche com zeros à esquerda
    
    if len(cpf_limpo) == 11:
        return cpf_limpo
    
    return cpf_limpo[:11]  # Trunca se maior que 11
```

### Validação de CPF
```python
def validar_cpf(cpf):
    cpf = normalizar_cpf(cpf)
    
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
```

### Extração de Processos
```python
def extrair_processos_html(html):
    processos = []
    processos_matches = re.findall(
        r'<li>\s*<div id="divProcesso[^"]*"[^>]*>.*?</div>\s*</li>', 
        html, 
        re.DOTALL
    )
    
    for processo_html in processos_matches:
        numero_match = re.search(r'class="linkProcesso"[^>]*>\s*([^<\s]+)', processo_html)
        classe_match = re.search(r'<div class="classeProcesso">([^<]+)</div>', processo_html)
        data_match = re.search(r'<div class="dataLocalDistribuicaoProcesso">([^<]+?)\s*-', processo_html)
        
        if numero_match and classe_match and data_match:
            processos.append({
                "numero": numero_match.group(1).strip(),
                "classe": classe_match.group(1).strip(),
                "data": data_match.group(1).strip()
            })
    
    return processos
```

## 🚨 Tratamento de Erros

### Tipos de Erro
1. **Erro de Upload**: Arquivo inválido ou colunas ausentes
2. **Erro de Validação**: CPFs inválidos
3. **Erro de Rede**: Timeout ou falha de conexão
4. **Erro de Processamento**: Falha na extração de dados

### Códigos de Status
- **200**: Sucesso
- **403**: Acesso negado (possível detecção de bot)
- **404**: Página não encontrada
- **500**: Erro interno do servidor
- **Timeout**: Tempo limite excedido

## 📈 Performance

### Otimizações
- **Delay configurável**: Evita sobrecarga do servidor
- **Processamento sequencial**: Controla taxa de requisições
- **Headers otimizados**: Simula navegador real
- **Logging eficiente**: Registra apenas informações essenciais

### Limitações
- **Rate limiting**: Delay mínimo de 1 segundo entre consultas
- **Timeout**: 30 segundos por consulta
- **Tamanho de arquivo**: Máximo 10MB (configurável)

## 🔒 Segurança

### Medidas Implementadas
- **Headers anti-bot**: Simula navegador real
- **Rate limiting**: Respeita limites do servidor
- **Validação de entrada**: Sanitiza dados de entrada
- **Logging de segurança**: Registra tentativas de acesso

### Boas Práticas
- **Não compartilhar logs**: Contêm informações sensíveis
- **Usar HTTPS**: Em produção
- **Monitorar uso**: Evitar abuso do sistema

## 🛠️ Manutenção

### Atualizações
1. **Dependências**: `pip install -r requirements.txt --upgrade`
2. **Configurações**: Editar `config.py`
3. **Logs**: Limpar arquivo `consulta_esaj.log` periodicamente

### Monitoramento
- **Verificar logs**: Analisar erros e performance
- **Testar conectividade**: Verificar acesso ao e-SAJ
- **Validar resultados**: Comparar com consultas manuais

## 📞 Suporte

### Problemas Comuns
1. **"CSV deve conter colunas 'CPF' e 'Nome'"**
   - Verificar se as colunas estão com nomes corretos
   - Aceita tanto maiúsculas quanto minúsculas

2. **"Nenhum CPF válido encontrado"**
   - Verificar formato dos CPFs no CSV
   - CPFs devem ter 9-11 dígitos

3. **"Erro de rede"**
   - Verificar conexão com internet
   - Verificar se o e-SAJ está acessível

4. **"Timeout na consulta"**
   - Aumentar delay entre consultas
   - Verificar estabilidade da conexão

### Logs de Debug
- Verificar arquivo `consulta_esaj.log`
- Procurar por mensagens de erro específicas
- Verificar status HTTP das respostas

## 📚 Referências

### APIs e Serviços
- **e-SAJ TJSP**: https://esaj.tjsp.jus.br/cpopg/
- **Streamlit**: https://streamlit.io/
- **Pandas**: https://pandas.pydata.org/

### Documentação Técnica
- **Algoritmo CPF**: https://pt.wikipedia.org/wiki/Cadastro_de_pessoas_físicas
- **HTTP Headers**: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- **Regex Python**: https://docs.python.org/3/library/re.html

---

## 📝 Changelog

### v1.0.0 (2023-09-21)
- ✅ Versão inicial
- ✅ Upload de CSV
- ✅ Validação de CPF
- ✅ Consulta e-SAJ
- ✅ Geração de relatórios
- ✅ Interface Streamlit

### v1.1.0 (2023-09-21)
- ✅ Suporte a headers "Nome" e "CPF" (case-insensitive)
- ✅ Normalização correta de CPFs
- ✅ Logging detalhado
- ✅ Tratamento de erros melhorado

### v1.2.0 (2023-09-21)
- ✅ Interface melhorada
- ✅ Upload na sidebar
- ✅ Checkbox "mostrar detalhes" sempre ligado
- ✅ CPFs inválidos listados separados por vírgula
- ✅ CSV reformatado com uma linha por processo
- ✅ Coluna "Sequencia_Processo" adicionada

---

**Desenvolvido com ❤️ para o projeto Revisa**
