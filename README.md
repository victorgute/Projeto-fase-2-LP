# 🌦️ Análise de Dados Meteorológicos de Porto Alegre (1961–2016)

Este é o projeto final da **Fase 2 da disciplina de Lógica de Programação** (PUCRS), com foco no processamento, análise e visualização de dados meteorológicos reais, usando **Python puro**.

---

## 📌 Objetivo

Desenvolver um programa capaz de:
- Ler e tratar dados de um arquivo `.csv`
- Permitir visualização filtrada dos dados por período e categoria
- Realizar análises estatísticas
- Exibir gráficos em modo texto
- Gerar estatísticas específicas de temperatura e precipitação

---

## 📁 Arquivos do projeto

- `analise_de_dados_meteorologicos_de_Porto_Alegre.py` — script Python com todo o código
- `Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv` — base de dados meteorológicos usada no projeto (não modifique o arquivo)

---

## 📥 Como executar

1. Coloque **ambos os arquivos na mesma pasta**  
2. Execute no terminal com:

```bash
python analise_de_dados_meteorologicos_de_Porto_Alegre.py
```

> ❗ O programa não funciona se o CSV estiver em outro diretório.

---

## 🧪 Funcionalidades principais

- **Leitura e tratamento de dados** com `open()` e `split(',')`
- Menu com 3 opções:
  1. Visualização de dados por período (todos, precipitação, temperatura, umidade/vento)
  2. Mês mais chuvoso entre 1961 e 2016
  3. Análise da média de temperatura mínima (2006–2016), com gráfico textual
- **Gráfico de barras horizontal** gerado com caracteres (sem bibliotecas)
- **Média geral da temperatura mínima** do mês analisado
- **Tratamento de erros** com mensagens informativas

---

## 🛠️ Tecnologias utilizadas

- [x] Python 3
- [x] Estruturas de dados (listas, dicionários)
- [x] Módulos: `datetime`, `calendar`, `collections`

---

## 🎓 Autor

**Victor Hugo Gutierrez Carvalho**  
Estudante de Análise e Desenvolvimento de Sistemas (PUCRS)  
📍 São Paulo, Brasil  
🔗 [LinkedIn](https://www.linkedin.com/in/seu-link)

---

## 📃 Licença

Este projeto está licenciado sob a **MIT License**.  
Para mais detalhes, veja o arquivo [LICENSE](LICENSE).

---

> “Dados são o novo petróleo, mas só quem sabe refiná-los transforma em valor.”