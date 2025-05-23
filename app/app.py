from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Arquivo para armazenar os dados do Kanban
DATA_FILE = 'kanban_data.json'

# Estrutura inicial do Kanban se o arquivo não existir
DEFAULT_DATA = {
    "columns": [
        {"id": "todo", "title": "A Fazer", "cards": []},
        {"id": "doing", "title": "Em Andamento", "cards": []},
        {"id": "done", "title": "Concluído", "cards": []}
    ]
}

def load_data():
    """Carrega os dados do Kanban do arquivo JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        # Se o arquivo não existir, cria com a estrutura padrão
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA

def save_data(data):
    """Salva os dados do Kanban no arquivo JSON"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    """Página principal do Kanban"""
    data = load_data()
    return render_template('index.html', columns=data['columns'])

@app.route('/add_card', methods=['POST'])
def add_card():
    """Adiciona um novo cartão ao Kanban"""
    data = load_data()
    column_id = request.form.get('column_id')
    title = request.form.get('title')
    description = request.form.get('description')
    
    # Encontra a coluna correta
    for column in data['columns']:
        if column['id'] == column_id:
            # Gera um ID simples para o cartão
            card_id = f"card_{len(column['cards']) + 1}_{column_id}"
            # Adiciona o novo cartão
            column['cards'].append({
                'id': card_id,
                'title': title,
                'description': description
            })
            break
    
    save_data(data)
    return redirect(url_for('index'))

@app.route('/move_card', methods=['POST'])
def move_card():
    """Move um cartão de uma coluna para outra"""
    data = load_data()
    card_id = request.form.get('card_id')
    from_column_id = request.form.get('from_column_id')
    to_column_id = request.form.get('to_column_id')
    
    # Encontra o cartão na coluna de origem
    card_to_move = None
    for column in data['columns']:
        if column['id'] == from_column_id:
            for i, card in enumerate(column['cards']):
                if card['id'] == card_id:
                    card_to_move = card
                    column['cards'].pop(i)
                    break
    
    # Adiciona o cartão na coluna de destino
    if card_to_move:
        for column in data['columns']:
            if column['id'] == to_column_id:
                column['cards'].append(card_to_move)
                break
    
    save_data(data)
    return redirect(url_for('index'))

@app.route('/delete_card', methods=['POST'])
def delete_card():
    """Remove um cartão do Kanban"""
    data = load_data()
    card_id = request.form.get('card_id')
    column_id = request.form.get('column_id')
    
    # Encontra e remove o cartão
    for column in data['columns']:
        if column['id'] == column_id:
            column['cards'] = [card for card in column['cards'] if card['id'] != card_id]
            break
    
    save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)