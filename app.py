import streamlit as st
import pandas as pd
import requests
import time
import re
from datetime import datetime
import io
import json
import sys
import os

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importar módulos locais
from config import *
from utils import *

# Configuração da página
st.set_page_config(
    page_title="Revisa Consulta CPF e-SAJ",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.375rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 0.375rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 0.375rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 0.375rem;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def processar_consultas(cpfs_validos, cpfs_invalidos, delay_consulta, mostrar_detalhes):
    """Processa as consultas de CPF no e-SAJ"""
    resultados_encontrados = []
    resultados_nao_encontrados = []
    
    # Configurar logging
    configurar_logging()
    
    # Barra de progresso
    total_cpfs = len(cpfs_validos)
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for contador, (idx, row) in enumerate(cpfs_validos.iterrows(), 1):
        cpf = row['cpf']
        nome = row['nome']
        
        # Atualizar barra de progresso
        progress = contador / total_cpfs
        progress_bar.progress(progress)
        status_text.text(f"Processando {contador}/{total_cpfs}: {nome} ({cpf})")
        
        # Consultar e-SAJ
        resultado = consultar_esaj(cpf, nome)
        
        if resultado['sucesso'] and resultado['encontrado']:
            resultados_encontrados.append({
                'cpf': cpf,
                'nome': nome,
                'nome_extraido': resultado['nome_extraido'],
                'processos': resultado['processos'],
                'total_processos': resultado['total_processos'],
                'data_consulta': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            })
            
            if mostrar_detalhes:
                st.success(f"✅ {nome} ({cpf}): {resultado['total_processos']} processos encontrados")
        else:
            resultados_nao_encontrados.append({
                'cpf': cpf,
                'nome': nome,
                'data_consulta': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            })
            
            if mostrar_detalhes:
                st.info(f"ℹ️ {nome} ({cpf}): Não encontrado")
        
        # Delay entre consultas
        if delay_consulta > 0:
            time.sleep(delay_consulta)
    
    # Limpar barra de progresso
    progress_bar.empty()
    status_text.empty()
    
    return resultados_encontrados, resultados_nao_encontrados

def mostrar_resultados(resultados_encontrados, resultados_nao_encontrados, cpfs_invalidos):
    """Mostra os resultados das consultas"""
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("✅ Encontrados", len(resultados_encontrados))
    
    with col2:
        st.metric("❌ Não Encontrados", len(resultados_nao_encontrados))
    
    with col3:
        st.metric("⚠️ CPFs Inválidos", len(cpfs_invalidos))
    
    with col4:
        total_processos = sum(r.get('total_processos', 0) for r in resultados_encontrados)
        st.metric("📋 Total Processos", total_processos)
    
    # Resultados encontrados
    if resultados_encontrados:
        st.success(f"✅ {len(resultados_encontrados)} CPFs com processos encontrados!")
        
        # Reformatar dados para CSV
        df_encontrados_reformatado = reformatar_dados_para_csv(resultados_encontrados)
        
        # Download CSV encontrados
        csv_encontrados = df_encontrados_reformatado.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📥 Download CSV - Encontrados",
            data=csv_encontrados,
            file_name=f"cpfs_encontrados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Mostrar preview dos dados
        st.subheader("📊 Preview dos Dados Encontrados")
        st.dataframe(df_encontrados_reformatado, use_container_width=True)
    
    # Resultados não encontrados
    if resultados_nao_encontrados:
        st.warning(f"⚠️ {len(resultados_nao_encontrados)} CPFs não encontrados")
        
        # Criar DataFrame para não encontrados
        df_nao_encontrados = pd.DataFrame(resultados_nao_encontrados)
        
        # Download CSV não encontrados
        csv_nao_encontrados = df_nao_encontrados.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📥 Download CSV - Não Encontrados",
            data=csv_nao_encontrados,
            file_name=f"cpfs_nao_encontrados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Mostrar lista de não encontrados
        st.subheader("📋 CPFs Não Encontrados")
        st.dataframe(df_nao_encontrados, use_container_width=True)
    
    # CPFs inválidos
    if len(cpfs_invalidos) > 0:
        st.error(f"❌ {len(cpfs_invalidos)} CPFs inválidos encontrados")
        cpfs_invalidos_lista = cpfs_invalidos['cpf'].astype(str).tolist()
        st.write(f"**CPFs inválidos:** {', '.join(cpfs_invalidos_lista)}")

def main():
    """Função principal da aplicação"""
    
    # Título principal
    st.markdown('<h1 class="main-header">🏛️ Revisa Consulta CPF e-SAJ</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Upload de arquivo CSV
        uploaded_file = st.file_uploader(
            "📁 Upload do arquivo CSV",
            type=['csv'],
            help="Arquivo deve conter colunas 'Nome' e 'CPF'"
        )
        
        # Configurações de processamento
        delay_consulta = st.slider(
            "⏱️ Delay entre consultas (segundos)",
            min_value=0,
            max_value=5,
            value=2,
            help="Tempo de espera entre cada consulta para evitar sobrecarga"
        )
        
        mostrar_detalhes = st.checkbox(
            "👀 Mostrar detalhes das consultas",
            value=True,
            help="Exibir progresso detalhado de cada consulta"
        )
    
    # Processamento do arquivo
    if uploaded_file is not None:
        try:
            # Processar CSV
            cpfs_validos, cpfs_invalidos = processar_csv(uploaded_file)
            
            if len(cpfs_validos) > 0:
                st.success(f"✅ Arquivo processado: {len(cpfs_validos)} CPFs válidos encontrados")
                
                # Mostrar CPFs inválidos se houver
                if len(cpfs_invalidos) > 0:
                    cpfs_invalidos_lista = cpfs_invalidos['cpf'].astype(str).tolist()
                    st.warning(f"⚠️ {len(cpfs_invalidos)} CPFs inválidos encontrados: {', '.join(cpfs_invalidos_lista)}")
                
                # Botão para iniciar consultas
                if st.button("🚀 Iniciar Consultas", type="primary"):
                    with st.spinner("Processando consultas..."):
                        resultados_encontrados, resultados_nao_encontrados = processar_consultas(
                            cpfs_validos, cpfs_invalidos, delay_consulta, mostrar_detalhes
                        )
                        
                        # Mostrar resultados
                        mostrar_resultados(resultados_encontrados, resultados_nao_encontrados, cpfs_invalidos)
            else:
                st.error("❌ Nenhum CPF válido encontrado no arquivo")
                
        except Exception as e:
            st.error(f"❌ Erro ao processar arquivo: {str(e)}")
    
    else:
        # Layout em duas colunas
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Instruções de uso
            st.subheader("🔍 Como utilizar?")
            st.markdown("**1.** Prepare seu arquivo CSV com colunas `Nome` e `CPF` (9-11 dígitos)")
            st.markdown("**2.** Faça upload na barra lateral")
            st.markdown("**3.** Configure o delay (recomendado: 2s)")
            st.markdown("**4.** Clique em \"Iniciar Consultas\"")
            st.markdown("**5.** Baixe os resultados em CSV")
            
            st.info("⚠️ **Importante:** CPFs com menos de 11 dígitos serão preenchidos com zeros à esquerda automaticamente.")
        
        with col2:
            # Exemplo de arquivo
            st.subheader("📄 Exemplo de arquivo CSV")
            exemplo_data = {
                'Nome': ['João Silva', 'Maria Santos', 'Pedro Oliveira', 'Ana Costa'],
                'CPF': ['12345678901', '98765432100', '11122233344', '55566677788']
            }
            exemplo_df = pd.DataFrame(exemplo_data)
            st.dataframe(exemplo_df, use_container_width=True)
            
            # Aviso sobre CPFs inválidos
            st.warning("⚠️ **Atenção:** CPFs inválidos não serão consultados, mas serão listados no relatório final.")

if __name__ == "__main__":
    main()