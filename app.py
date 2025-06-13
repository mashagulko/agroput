from flask import Flask, jsonify, render_template

app = Flask(__name__)

professions = [
    {"id": 1, "name": "Агроном", "description": "Специалист по выращиванию сельскохозяйственных культур."},
    {"id": 2, "name": "Зоотехник", "description": "Эксперт по разведению и содержанию животных."},
    {"id": 3, "name": "Агроинженер", "description": "Специалист по техническому обеспечению сельского хозяйства."},
    {"id": 4, "name": "Биотехнолог", "description": "Работник с генетическими и биологическими технологиями в АПК."},
    {"id": 5, "name": "Разработчик роботов для АПК", "description": "Создаёт автоматизированные системы и роботов для сельского хозяйства."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/professions')
def get_professions():
    return jsonify(professions)

if __name__ == '__main__':
    app.run(debug=True)
