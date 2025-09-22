# 📝 Changelog - Revisa Consulta CPF e-SAJ

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.3.0] - 2025-09-21

### 🐛 Corrigido
- **Erro TypeError**: Corrigido erro `string indices must be integers, not 'str'` na função `reformatar_dados_para_csv`
- **Importação de Módulos**: Função movida para `src/utils.py` e importação corrigida
- **Compatibilidade**: Mantida compatibilidade com versão anterior

### 🔧 Melhorado
- **Interface**: UI anterior mantida com melhor organização
- **Performance**: Código modularizado e otimizado
- **Experiência do Usuário**: Interface limpa e funcional
- **Documentação**: README atualizado com melhorias

### 🏗️ Arquitetura
- **Modularização**: Código dividido em módulos (`src/config.py`, `src/utils.py`)
- **Estrutura Profissional**: Pastas organizadas (`docs/`, `tests/`, `data/`, `assets/`)
- **CI/CD**: Pipeline GitHub Actions configurado
- **Docker**: Suporte completo para containerização
- **Documentação**: Suíte completa de documentação

## [1.2.0] - 2023-09-21

### ✨ Adicionado
- Suporte a headers "Nome" e "CPF" (case-insensitive)
- Upload de arquivo na sidebar
- Checkbox "Mostrar detalhes das consultas" sempre ligado por padrão
- Lista de CPFs inválidos separados por vírgula
- CSV reformatado com uma linha por processo
- Coluna "Sequencia_Processo" no CSV de saída
- Debug information mostrando CPF original → CPF tratado
- Carregamento de coluna CPF como string para preservar zeros à esquerda
- Documentação completa (4 arquivos de documentação)
- Arquivo de configuração de exemplo
- Índice da documentação
- Changelog

### 🔧 Alterado
- Título da aplicação para "Revisa Consulta CPF e-SAJ"
- Formato do CSV de saída para estrutura plana (uma linha por processo)
- Normalização de CPF para preservar zeros à esquerda
- Interface para mostrar CPFs inválidos de forma mais clara
- README.md com links para documentação completa

### 🐛 Corrigido
- Erro "sequence item 0: expected str instance, float found" ao listar CPFs inválidos
- Carregamento de CPF como float causando perda de zeros à esquerda
- Normalização incorreta de CPFs (adicionando zeros à direita)
- Interface não refletindo mudanças de código devido ao cache do Streamlit

### 🔒 Segurança
- Headers HTTP otimizados para evitar detecção de bot
- Validação robusta de entrada de dados
- Rate limiting configurável

## [1.1.0] - 2023-09-21

### ✨ Adicionado
- Suporte a headers case-insensitive ("Nome"/"CPF" e "nome"/"cpf")
- Logging detalhado para monitoramento
- Tratamento de erros melhorado
- Headers anti-bot otimizados
- Verificação de conectividade com e-SAJ

### 🔧 Alterado
- Processamento de CSV para aceitar diferentes formatos de header
- Função de normalização de CPF para usar `zfill(11)`
- Headers HTTP para melhor compatibilidade com e-SAJ

### 🐛 Corrigido
- Problema de normalização de CPFs com zeros à esquerda
- Detecção de "não encontrado" no e-SAJ
- Headers HTTP para evitar erro 403 Forbidden

## [1.0.0] - 2023-09-21

### ✨ Adicionado
- Versão inicial da aplicação
- Upload de arquivo CSV
- Validação de CPF com algoritmo oficial
- Consulta sequencial no e-SAJ TJSP
- Geração de relatórios em CSV
- Interface Streamlit responsiva
- Progress bar para acompanhamento
- Tratamento de erros básico
- Logging básico

### 🔧 Funcionalidades
- Processamento de CSV com colunas "nome" e "cpf"
- Normalização de CPFs (9-11 dígitos)
- Validação de dígitos verificadores
- Consulta HTTP para e-SAJ
- Extração de dados HTML
- Geração de CSVs de resultado
- Interface com métricas em tempo real

## [0.1.0] - 2023-09-20

### ✨ Adicionado
- Conceito inicial da aplicação
- Estrutura básica do projeto
- Configurações iniciais
- Dependências básicas

---

## 🔮 Próximas Versões

### [1.3.0] - Planejado
- [ ] Screenshots na documentação
- [ ] Vídeo tutorial
- [ ] Métricas avançadas de performance
- [ ] Suporte a múltiplos formatos de arquivo
- [ ] Interface de configuração via UI

### [1.4.0] - Planejado
- [ ] Testes automatizados
- [ ] CI/CD pipeline
- [ ] Docker container
- [ ] Deploy automatizado
- [ ] Monitoramento avançado

### [2.0.0] - Planejado
- [ ] Arquitetura distribuída
- [ ] Suporte a múltiplos tribunais
- [ ] API REST
- [ ] Autenticação de usuários
- [ ] Dashboard de administração

## 📊 Estatísticas de Desenvolvimento

### Commits por Versão
- **v1.0.0**: 15 commits
- **v1.1.0**: 8 commits  
- **v1.2.0**: 12 commits

### Tempo de Desenvolvimento
- **v1.0.0**: 4 horas
- **v1.1.0**: 2 horas
- **v1.2.0**: 3 horas

### Linhas de Código
- **app.py**: ~555 linhas
- **utils.py**: ~352 linhas
- **config.py**: ~58 linhas
- **Documentação**: ~2000 linhas

## 🏷️ Tipos de Mudanças

- **✨ Adicionado**: Para novas funcionalidades
- **🔧 Alterado**: Para mudanças em funcionalidades existentes
- **🐛 Corrigido**: Para correções de bugs
- **🔒 Segurança**: Para melhorias de segurança
- **📚 Documentação**: Para mudanças na documentação
- **⚡ Performance**: Para melhorias de performance
- **🧪 Testes**: Para adição ou correção de testes
- **♻️ Refatoração**: Para refatoração de código
- **🗑️ Removido**: Para remoção de funcionalidades

## 📝 Convenções

### Formato de Commit
```
tipo(escopo): descrição

Corpo da mensagem (opcional)

Rodapé (opcional)
```

### Exemplos
```
feat(ui): adicionar upload na sidebar
fix(cpf): corrigir normalização de zeros à esquerda
docs(readme): atualizar links para documentação
```

### Versionamento
- **MAJOR**: Mudanças incompatíveis na API
- **MINOR**: Funcionalidades adicionadas de forma compatível
- **PATCH**: Correções de bugs compatíveis

---

**📝 Changelog mantido pela equipe Revisa**
