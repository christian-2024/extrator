import json
import csv

with open('centro001.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

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