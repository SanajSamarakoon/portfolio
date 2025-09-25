# Main Application File

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for flash messages

# Sample timeline data
# Types: Academic, Project, Client Project, Work Experience
TIMELINE = [
    {
        "id": 0, 
        "title": "CS50 - Introduction to Computer Science", 
        "description": "My first course into computer science, since 2018 when i did computational physical (fortran) during my undergrad as physics major.", 
        "type": ["Academic"],
        "date1": "January 2025",
        "date2": "August 2025"
    },
    {
        "id": 1, 
        "title": "Portfolio Website", 
        "description": "My first project (more details in projects). Most projects will not be added to timeline, only significant ones.", 
        "type": ["Project"],
        "date1": "August 2025",
        "date2": "October 2025"
    },
    {
        "id": 2, 
        "title": "Software Engineer - Intern at Startup", 
        "description": ".", 
        "type": ["Work Experience"],
        "date1": "December 2025",
        "date2": "February 2026"
    },
    {
        "id": 3, 
        "title": "Custom Dashboard and Visualization", 
        "description": "My first client project, about a total of 30 hours of work, for about $600 ($20 /hour).", 
        "type": ["Client Project"],
        "date1": "February 2026",
        "date2": "February 2026"
    },
    {
        "id": 4, 
        "title": "Mastering Aglorithms and Data Structures in C/C++", 
        "description": "An extension of the Lite ERP for data analytics and visualization.", 
        "type": ["Academic"],
        "date1": "October 2025",
        "date2": "February 2026"
    }
]
# Sample project data
PROJECTS = [
    {
        "id": 0, 
        "title": "Portfolio Website", 
        "description": "My first project.", 
        "image": "project0.png",
        "tech_stack": ["C++"],
        "demo_url": "#",
        "github_url": "#"
    },
    {
        "id": 1, 
        "title": "2D Super Mario Game", 
        "description": "A tribute to my first interaction with a computer in 2005 (Grade 4).", 
        "image": "project1.png",
        "tech_stack": ["C++"],
        "demo_url": "#",
        "github_url": "#"
    },
    {
        "id": 2, 
        "title": "Lite ERP", 
        "description": "Basic ERP inventory management, manufacturing and batch tracibility.", 
        "image": "project2.png",
        "tech_stack": ["Java (SpringBoot)", "PostgreSQL" ,"React"],
        "demo_url": "#",
        "github_url": "#"
    },
    {
        "id": 3, 
        "title": "Lite ERP Dashboard", 
        "description": "An extension of the Lite ERP for data analytics and visualization.", 
        "image": "project3.png",
        "tech_stack": ["Java (SpringBoot)", "PostgreSQL" ,"React"],
        "demo_url": "#",
        "github_url": "#"
    },
]
# Context processor to inject current year into all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html', projects=PROJECTS)

@app.route('/about')
def about():
    return render_template('about.html', timeline=TIMELINE)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if not project:
        flash("Project not found.")
        return redirect(url_for('projects'))
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For now, just print (later can send email and store in DB)
        print("Contact Form Submission:")
        print(f"New Message from {name} ({email}): {message}")
        flash("Thanks for reaching out! Your message has been received.")
        return redirect(url_for('index'))
    
    return render_template('contact.html') # If GET request, just render the form

if __name__ == '__main__':
    app.run(debug=True)