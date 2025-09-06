# Main Application File

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for flash messages

PROJECTS = [
    {"id": 1, "title": "2D Super Mario Game", "desc": "A tribute to my first interaction with a computer in 2005 (Grade 4)."},
    {"id": 2, "title": "Lite ERP", "desc": "Basic ERP inventory management, manufacturing and batch tracibility."},
    {"id": 3, "title": "Lite ERP Dashboard", "desc": "An extension of the Lite ERP for data analytics and visualization."}
]
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/<project_id>')
def project_detail(project_id):
    return render_template('project_detail.html', project_id=project_id)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Here you would typically handle the form submission, e.g., save to a database or send an email
    # For testing only a print statement is used
    print(f"📩 New contact submission: {name}, {email}, {message}")
    
    flash("Thanks for reaching out! Your message has been received.")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)