# 👤 Guia do Usuário - Revisa Consulta CPF e-SAJ

## 🎯 O que é esta aplicação?

A **Revisa Consulta CPF e-SAJ** é uma ferramenta web que permite consultar CPFs em lote no sistema e-SAJ do Tribunal de Justiça de São Paulo. Em vez de consultar CPF por CPF manualmente, você pode fazer upload de um arquivo CSV com uma lista de CPFs e a aplicação fará todas as consultas automaticamente.

## 🚀 Como usar

### Passo 1: Preparar seu arquivo CSV

Crie um arquivo CSV com as seguintes colunas:
- **Nome**: Nome da pessoa
- **CPF**: CPF da pessoa (pode ter 9, 10 ou 11 dígitos)

**Exemplo de arquivo CSV:**
```csv
Nome,CPF
João Silva,12345678901
Maria Santos,98765432100
Pedro Costa,11122233344
Ana Lima,123456789
```

### Passo 2: Acessar a aplicação

1. Abra seu navegador
2. Acesse: `http://localhost:8501`
3. A aplicação abrirá automaticamente

### Passo 3: Fazer upload do arquivo

1. Na barra lateral direita, clique em **"Escolha um arquivo CSV"**
2. Selecione seu arquivo CSV
3. Aguarde o processamento

### Passo 4: Configurar as consultas

1. **Delay entre consultas**: Escolha entre 1 e 5 segundos (recomendado: 2 segundos)
2. **Mostrar detalhes das consultas**: Deixe marcado para ver o progresso

### Passo 5: Iniciar as consultas

1. Clique no botão **"🚀 Iniciar Consultas no e-SAJ"**
2. Aguarde o processamento (pode levar alguns minutos)
3. Acompanhe o progresso na barra de progresso

### Passo 6: Baixar os resultados

Após o processamento, você verá:

#### ✅ CPFs Encontrados
- **Métrica**: Quantos CPFs foram encontrados
- **Download**: Botão para baixar CSV com os resultados
- **Preview**: Tabela mostrando os dados encontrados

#### ❌ CPFs Não Encontrados
- **Métrica**: Quantos CPFs não foram encontrados
- **Download**: Botão para baixar CSV com os não encontrados
- **Lista**: Tabela mostrando os CPFs não encontrados

#### ⚠️ CPFs Inválidos
- **Métrica**: Quantos CPFs são inválidos
- **Lista**: Tabela mostrando os CPFs inválidos

## 📊 Entendendo os resultados

### CSV de CPFs Encontrados

Cada processo encontrado gera uma linha separada:

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| **CPF** | CPF consultado | 12345678901 |
| **Nome** | Nome do seu CSV | João Silva |
| **Nome_Extraido** | Nome encontrado no e-SAJ | João Silva Santos |
| **Sequencia_Processo** | Ordem do processo | 1, 2, 3... |
| **Numero_Processo** | Número do processo | 1234567-89.2023.8.26.0500 |
| **Classe_Processo** | Tipo do processo | Precatório |
| **Data_Processo** | Data de recebimento | 15/03/2023 |
| **Data_Consulta** | Data da consulta | 2023-09-21 10:30:00 |

**Exemplo**: Se João Silva tem 2 processos, ele aparecerá em 2 linhas:
- Linha 1: CPF, Nome, Nome_Extraido, Sequencia_Processo=1, Processo1...
- Linha 2: CPF, Nome, Nome_Extraido, Sequencia_Processo=2, Processo2...

### CSV de CPFs Não Encontrados

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| **nome** | Nome do seu CSV | João Silva |
| **cpf** | CPF consultado | 12345678901 |
| **motivo** | Por que não foi encontrado | Não encontrado no e-SAJ |
| **data_consulta** | Data da consulta | 2023-09-21 10:30:00 |

## ❓ Perguntas Frequentes

### Q: Meu CPF tem menos de 11 dígitos, funciona?
**R:** Sim! A aplicação preenche automaticamente com zeros à esquerda. Por exemplo:
- `123456789` vira `00123456789`
- `1234567890` vira `01234567890`

### Q: Posso usar "nome" e "cpf" em minúsculas?
**R:** Sim! A aplicação aceita tanto maiúsculas quanto minúsculas:
- `Nome,CPF` ✅
- `nome,cpf` ✅
- `NOME,CPF` ✅

### Q: Quanto tempo demora para processar?
**R:** Depende da quantidade de CPFs e do delay configurado:
- 100 CPFs com delay de 2s = ~3-4 minutos
- 1000 CPFs com delay de 2s = ~30-35 minutos

### Q: O que significa "CPF inválido"?
**R:** São CPFs que não passaram na validação:
- Menos de 9 dígitos
- Mais de 11 dígitos
- Dígitos verificadores incorretos
- Sequência repetida (11111111111)

### Q: Por que alguns CPFs não são encontrados?
**R:** Pode ser por vários motivos:
- CPF não tem processos no e-SAJ
- CPF está incorreto
- Problema temporário no e-SAJ
- CPF não está no banco de dados do TJSP

### Q: Posso interromper o processamento?
**R:** Sim, mas os resultados parciais serão perdidos. Para interromper:
- Feche a aba do navegador
- Ou recarregue a página (F5)

### Q: Os dados são salvos permanentemente?
**R:** Não. A aplicação não salva seus dados. Tudo é processado em memória e você precisa baixar os CSVs para salvar os resultados.

## 🚨 Resolução de Problemas

### Erro: "CSV deve conter colunas 'CPF' e 'Nome'"
**Solução:**
1. Verifique se as colunas estão com nomes corretos
2. Aceita tanto maiúsculas quanto minúsculas
3. Verifique se não há espaços extras nos nomes das colunas

### Erro: "Nenhum CPF válido encontrado"
**Solução:**
1. Verifique se os CPFs têm entre 9 e 11 dígitos
2. Verifique se não há caracteres especiais nos CPFs
3. Verifique se os CPFs não são sequências repetidas

### Erro: "Erro de rede" ou "Timeout"
**Solução:**
1. Verifique sua conexão com internet
2. Aumente o delay entre consultas (3-5 segundos)
3. Tente novamente em alguns minutos

### Aplicação não carrega
**Solução:**
1. Verifique se a aplicação está rodando
2. Tente acessar: `http://localhost:8501`
3. Reinicie a aplicação se necessário

## 💡 Dicas de Uso

### Para melhor performance:
1. **Use delay de 2-3 segundos** entre consultas
2. **Processe em lotes menores** (até 500 CPFs por vez)
3. **Verifique os CPFs** antes de fazer upload
4. **Use conexão estável** com internet

### Para evitar problemas:
1. **Salve os resultados** imediatamente após o processamento
2. **Verifique o arquivo CSV** antes do upload
3. **Não interrompa** o processamento desnecessariamente
4. **Monitore os logs** se houver problemas

### Para grandes volumes:
1. **Divida em lotes** de 200-500 CPFs
2. **Use delay maior** (3-5 segundos)
3. **Processe em horários** de menor movimento
4. **Monitore a performance** do e-SAJ

## 📞 Suporte

Se você encontrar problemas:

1. **Verifique este guia** primeiro
2. **Consulte os logs** da aplicação
3. **Teste com poucos CPFs** primeiro
4. **Entre em contato** com a equipe técnica

---

**Versão**: 1.2.0  
**Data**: 2023-09-21  
**Aplicação**: Revisa Consulta CPF e-SAJ
