from flask import Flask, render_react, render_template, request, redirect, url_for

app = Flask(__name__)

# In-Memory Storage: List of dictionaries to keep track of tasks
# Each task has an 'id', 'text' description, and a 'completed' status
tasks = [
    {"id": 1, "text": "Learn Flask routes", "completed": False},
    {"id": 2, "text": "Build a To-Do app", "completed": False}
]
next_id = 3

@app.route('/')
def index():
    # Level 01: Displays the main list of tasks
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global next_id
    # Level 01: Handles form submission via POST to add a new task
    task_text = request.form.get('task_text')
    if task_text:
        new_task = {
            "id": next_id,
            "text": task_text,
            "completed": False
        }
        tasks.append(new_task)
        next_id += 1
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    # Level 02: Toggles the completion status of a task
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Level 02: Deletes a specific task from the list
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Runs the application locally on http://127.0.0
    app.run(debug=True)