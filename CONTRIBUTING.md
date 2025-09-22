# 🤝 Guia de Contribuição - Revisa Consulta CPF e-SAJ

Obrigado por considerar contribuir para o projeto **Revisa Consulta CPF e-SAJ**! Este documento fornece diretrizes para contribuições.

## 📋 Índice

- [Código de Conduta](#código-de-conduta)
- [Como Contribuir](#como-contribuir)
- [Processo de Desenvolvimento](#processo-de-desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Testes](#testes)
- [Documentação](#documentação)
- [Reportar Bugs](#reportar-bugs)
- [Sugerir Funcionalidades](#sugerir-funcionalidades)

## 📜 Código de Conduta

### Nossos Compromissos

- **Inclusividade**: Criamos um ambiente acolhedor e inclusivo
- **Respeito**: Tratamos todos com respeito e dignidade
- **Colaboração**: Valorizamos diferentes perspectivas e experiências
- **Profissionalismo**: Mantemos um comportamento profissional

### Comportamentos Esperados

- ✅ Usar linguagem acolhedora e inclusiva
- ✅ Respeitar diferentes pontos de vista e experiências
- ✅ Aceitar críticas construtivas graciosamente
- ✅ Focar no que é melhor para a comunidade
- ✅ Demonstrar empatia com outros membros

### Comportamentos Inaceitáveis

- ❌ Linguagem ou imagens sexualizadas
- ❌ Trolling, comentários insultuosos ou ataques pessoais
- ❌ Assédio público ou privado
- ❌ Publicar informações privadas sem permissão
- ❌ Outros comportamentos inadequados em ambiente profissional

## 🚀 Como Contribuir

### 1. Fork do Projeto
1. Faça fork do repositório
2. Clone seu fork localmente
3. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`

### 2. Configurar Ambiente
```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/revisa-consulta-cpf-esaj.git
cd revisa-consulta-cpf-esaj/UI-streamlit

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt
```

### 3. Fazer Mudanças
- Faça suas alterações
- Siga os padrões de código
- Adicione testes se necessário
- Atualize a documentação

### 4. Testar
```bash
# Executar testes
pytest

# Executar aplicação
streamlit run app.py

# Verificar linting
flake8 app.py utils.py config.py
```

### 5. Commit e Push
```bash
# Adicionar mudanças
git add .

# Fazer commit com mensagem descritiva
git commit -m "feat: adicionar nova funcionalidade X"

# Push para seu fork
git push origin feature/nova-funcionalidade
```

### 6. Pull Request
1. Abra um Pull Request no repositório original
2. Descreva suas mudanças claramente
3. Referencie issues relacionadas
4. Aguarde revisão e feedback

## 🔄 Processo de Desenvolvimento

### Branches
- **main**: Branch principal (produção)
- **develop**: Branch de desenvolvimento
- **feature/**: Novas funcionalidades
- **bugfix/**: Correções de bugs
- **hotfix/**: Correções urgentes

### Fluxo de Trabalho
1. **Issue**: Crie uma issue descrevendo o problema/feature
2. **Branch**: Crie uma branch a partir de `develop`
3. **Desenvolvimento**: Implemente a solução
4. **Testes**: Execute todos os testes
5. **Pull Request**: Abra PR para `develop`
6. **Code Review**: Aguarde revisão
7. **Merge**: Após aprovação, merge para `develop`
8. **Release**: Merge `develop` para `main` em releases

## 📏 Padrões de Código

### Python
- **PEP 8**: Siga o guia de estilo Python
- **Type Hints**: Use type hints quando possível
- **Docstrings**: Documente funções e classes
- **Naming**: Use nomes descritivos e em inglês

### Exemplo de Código
```python
def consultar_esaj(cpf: str, nome: str) -> Dict[str, Any]:
    """
    Consulta CPF no e-SAJ TJSP
    
    Args:
        cpf: CPF para consultar (11 dígitos)
        nome: Nome da pessoa
        
    Returns:
        Dicionário com resultado da consulta
        
    Raises:
        ValueError: Se CPF for inválido
        RequestException: Se houver erro de rede
    """
    if not validar_cpf(cpf):
        raise ValueError(f"CPF inválido: {cpf}")
    
    # Implementação...
    return resultado
```

### Estrutura de Arquivos
```
UI-streamlit/
├── app.py                 # Aplicação principal
├── config.py             # Configurações
├── utils.py              # Funções utilitárias
├── tests/                # Testes
│   ├── test_app.py
│   ├── test_utils.py
│   └── test_config.py
├── docs/                 # Documentação
├── requirements.txt      # Dependências
├── requirements-dev.txt  # Dependências de desenvolvimento
└── README.md
```

## 🧪 Testes

### Tipos de Testes
- **Unitários**: Testam funções individuais
- **Integração**: Testam fluxos completos
- **E2E**: Testam a aplicação completa

### Executar Testes
```bash
# Todos os testes
pytest

# Testes específicos
pytest tests/test_utils.py

# Com cobertura
pytest --cov=app --cov=utils

# Testes de integração
pytest tests/integration/
```

### Exemplo de Teste
```python
import pytest
from utils import normalizar_cpf, validar_cpf

def test_normalizar_cpf():
    """Testa normalização de CPF"""
    assert normalizar_cpf("123456789") == "00123456789"
    assert normalizar_cpf("12345678901") == "12345678901"
    assert normalizar_cpf("123456789012") == "12345678901"

def test_validar_cpf():
    """Testa validação de CPF"""
    assert validar_cpf("11144477735") == True
    assert validar_cpf("11111111111") == False
    assert validar_cpf("12345678901") == False
```

## 📚 Documentação

### Atualizar Documentação
- **README.md**: Para mudanças na API ou uso
- **DOCUMENTACAO_COMPLETA.md**: Para mudanças técnicas
- **GUIA_USUARIO.md**: Para mudanças na interface
- **CHANGELOG.md**: Para todas as mudanças

### Padrões de Documentação
- Use Markdown
- Inclua exemplos práticos
- Mantenha consistência
- Atualize índices e links

## 🐛 Reportar Bugs

### Template de Bug Report
```markdown
**Descrição**
Descrição clara e concisa do bug.

**Passos para Reproduzir**
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Comportamento Atual**
O que está acontecendo.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente**
- OS: [ex: Windows 10]
- Python: [ex: 3.8.5]
- Streamlit: [ex: 1.28.0]

**Logs**
Adicione logs relevantes.
```

### Severidade
- **Crítico**: Aplicação não funciona
- **Alto**: Funcionalidade principal quebrada
- **Médio**: Funcionalidade secundária quebrada
- **Baixo**: Problema cosmético

## 💡 Sugerir Funcionalidades

### Template de Feature Request
```markdown
**Funcionalidade**
Descrição clara da funcionalidade desejada.

**Problema**
Qual problema esta funcionalidade resolve?

**Solução Proposta**
Como você imagina que deveria funcionar?

**Alternativas**
Outras soluções consideradas.

**Contexto Adicional**
Qualquer contexto adicional.
```

### Critérios de Aceitação
- ✅ Resolve um problema real
- ✅ Alinha com os objetivos do projeto
- ✅ É tecnicamente viável
- ✅ Tem impacto positivo na UX
- ✅ Não quebra funcionalidades existentes

## 📋 Checklist para Pull Requests

### Antes de Enviar
- [ ] Código segue os padrões estabelecidos
- [ ] Testes passam
- [ ] Documentação atualizada
- [ ] CHANGELOG.md atualizado
- [ ] Commit messages descritivas
- [ ] Branch atualizada com develop

### Durante a Revisão
- [ ] Responder a feedback
- [ ] Fazer mudanças solicitadas
- [ ] Manter discussão construtiva
- [ ] Testar mudanças localmente

### Após Aprovação
- [ ] Merge para develop
- [ ] Deletar branch feature
- [ ] Testar em ambiente de staging
- [ ] Preparar release notes

## 🏷️ Labels e Milestones

### Labels
- **bug**: Algo não está funcionando
- **enhancement**: Nova funcionalidade
- **documentation**: Melhorias na documentação
- **good first issue**: Bom para iniciantes
- **help wanted**: Precisa de ajuda
- **priority:high**: Alta prioridade
- **priority:medium**: Média prioridade
- **priority:low**: Baixa prioridade

### Milestones
- **v1.3.0**: Próxima versão menor
- **v2.0.0**: Próxima versão maior
- **Backlog**: Funcionalidades futuras

## 📞 Contato

- **Issues**: Use o sistema de issues do GitHub
- **Discussions**: Use GitHub Discussions para perguntas
- **Email**: [contato@projeto.com]
- **Slack**: [Canal do projeto]

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a [MIT License](LICENSE).

---

**🤝 Obrigado por contribuir para o projeto Revisa!**
