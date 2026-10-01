from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'senha secreta'
@app.route('/')
def index():
    if 'lista' not in session:
        session['lista']= []

    return render_template('tarefas.html', lista=session['lista'])

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form.get('task')
    
    if task_name and task_name.strip():
        if 'tasks' not in session:
            session['tasks'] = []
        
        # Adiciona a nova tarefa
        session['tasks'].append(task_name.strip())
        # Notifica o Flask de que o objeto mutável dentro da sessão foi alterado
        session.modified = True

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    if 'tasks' in session:
        # Verifica se o ID fornecido está dentro do intervalo válido da lista
        if 0 <= task_id < len(session['tasks']):
            session['tasks'].pop(task_id)
            session.modified = True

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)