import json
import csv

arquivos_json = ['centro001.json']
dados_combinados = []

for arquivo in arquivos_json:
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)

        if isinstance(dados, dict):
            dados_combinados.extend(dados.get('local_results', []))

# Cria um arquivo CSV pronto para abrir no Excel
with open('resultado_planilha.csv', 'w', newline='', encoding='utf-8-sig') as f_csv:
    writer = csv.writer(f_csv, delimiter=';') # Usa ';' que o Excel reconhece como coluna
    writer.writerow(['Nome', 'Telefone']) # Cabeçalho

    for item in dados.get('local_results', []):
        title = item.get('title', 'N/A')
        phone = item.get('phone', 'N/A')
        
        if phone != 'N/A':
            phone = phone.replace('+55', '').strip()
        
        writer.writerow([title, phone])

print("Planilha 'resultado_planilha.csv' gerada com sucesso!")