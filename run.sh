#!/bin/bash

# Script para executar a aplicação Streamlit
# Uso: ./run.sh

echo "🏛️ Iniciando UI Streamlit - Consulta CPF e-SAJ TJSP"
echo "=================================================="

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale o Python3 primeiro."
    exit 1
fi

# Verificar se o pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 não encontrado. Instale o pip3 primeiro."
    exit 1
fi

# Instalar dependências se necessário
echo "📦 Verificando dependências..."
pip3 install -r requirements.txt

# Executar aplicação
echo "🚀 Iniciando aplicação Streamlit..."
echo "📱 Acesse: http://localhost:8501"
echo "⏹️  Para parar: Ctrl+C"
echo ""

streamlit run app.py
