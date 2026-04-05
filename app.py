# Main Application File
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from models import db, TimelineEvent, Project, ContactMessage
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

# Configure database (for simplicity, using SQLite here)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

with app.app_context(): #  Create database tables if they don't exist
    db.create_all()

# Context processor to inject current year into all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    projects = Project.query.order_by(Project.id.desc()).limit(3).all() # Show only 3 projects on the homepage
    return render_template('index.html', projects=projects)

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
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Save to DB using the model's static method
        if name and email and message:
            ContactMessage.save_message(name, email, message)
            flash("Thanks for reaching out! Your message has been received.")
            return redirect(url_for('contact'))
        else:
            flash("Please fill out all fields before submitting.")
    # GET
    return render_template('contact.html') # If GET request, just render the form

if __name__ == '__main__':
    app.run(debug=True)