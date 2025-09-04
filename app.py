# Main Application File

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/<project_id>')
def project_detail(project_id):
    return render_template('project_detail.html', project_id=project_id)

if __name__ == '__main__':
    app.run(debug=True)