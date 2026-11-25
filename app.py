from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My To-Do List</title>
</head>
<body>
    <h1>My To-Do List</h1>
    <form action="/add" method="POST">
        <input name="task" placeholder="Enter a task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
    {% for task in tasks %}
        <li>
            {{ task.text }}
            {% if not task.done %}
                <a href="/complete/{{ loop.index0 }}">Complete</a>
            {% else %}
                <strong>Done</strong>
            {% endif %}
            <a href="/delete/{{ loop.index0 }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append({"text": task, "done": False})
    return redirect(url_for("home"))

@app.route("/complete/<int:index>")
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
