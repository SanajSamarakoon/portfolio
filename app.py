# Main Application File
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db, TimelineEvent

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed for flash messages

# Configure database (for simplicity, using SQLite here)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

with app.app_context(): #  Create database tables if they don't exist
    db.create_all()

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
    timeline_events = TimelineEvent.query

    # Get filter values from query string
    category = request.args.get('category')
    start_date = request.args.get('start_date')  # Format: YYYY-MM
    end_date = request.args.get('end_date')


    # Apply filters
    if category:
        timeline_events = timeline_events.filter_by(category=category)

    if start_date:
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m")
            timeline_events = timeline_events.filter(TimelineEvent.start_date >= start_date_obj)
        except ValueError:
            pass

    if end_date:
        try:
            end_date_obj = datetime.strptime(end_date, "%Y-%m")
            timeline_events = timeline_events.filter(TimelineEvent.end_date <= end_date_obj)
        except ValueError:
            pass

    timeline_events = timeline_events.order_by(TimelineEvent.start_date.asc()).all()

    return render_template('about.html', timeline=timeline_events)

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