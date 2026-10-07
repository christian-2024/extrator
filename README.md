# Extrator de Telefones do Google Maps (SerpApi)

Este é um script simples em Python desenvolvido para ler o arquivo JSON de resultados extraídos do Google Maps via SerpApi e formatar os dados de forma limpa.

## 📌 O que este programa faz?

1. **Lê o arquivo JSON:** Abre o arquivo com os resultados do Google Maps (ex: `centro001.json`).
2. **Filtra as informações:** Extrai apenas o **Nome do Estabelecimento** (`title`) e o **Telefone** (`phone`).
3. **Limpa o telefone:** Remove o código internacional `+55` e espaços desnecessários.
4. **Formata para Planilhas:** Separa o nome e o telefone usando uma tabulação (`\t`).
5. **Exibe no Terminal:** Printa o resultado pronto para você copiar (`Ctrl + C`) e colar (`Ctrl + V`) direto no **Excel** ou **Google Planilhas**, onde cada dado vai automaticamente para sua respectiva coluna.

---

## 🚀 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Coloque o arquivo JSON gerado pela SerpApi na mesma pasta do script com o nome `centro001.json` (ou altere o nome no arquivo Python).
3. Execute o comando no terminal:

```bash
python extrair.py
