import json

# Substitua 'resultado.json' pelo nome do seu arquivo
with open('centro001.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

for item in dados.get('local_results', []):
    title = item.get('title', 'N/A')
    phone = item.get('phone', 'N/A')
    
    # Remove o +55
    if phone != 'N/A':
        phone = phone.replace('+55', '').strip()
    
    print(f"{title}\t{phone}")