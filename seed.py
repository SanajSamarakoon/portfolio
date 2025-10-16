# Seed the initial databases
import json
from app import app, db
from models import TimelineEvent
from datetime import datetime

# Helper function to parse dates
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%B %Y").date()
    except ValueError:
        return None
    
with app.app_context():
   # Define timeline events
    events = [
        TimelineEvent(
            title="CS50 - Introduction to Computer Science",
            description="My first course into computer science, since 2018 when I did computational physics (Fortran) during my undergrad as a Physics major.",
            category="Academic",
            start_date=parse_date("January 2025"),
            end_date=parse_date("August 2025"),
            image_path="images/event0.png",
            tech_stack=["C", "Python", "SQL", "JavaScript", "HTML", "CSS", "Flask"]
        ),
        TimelineEvent(
            title="Portfolio Website",
            description="My first project (more details in projects). Most projects will not be added to timeline, only significant ones.",
            category="Project",
            start_date=parse_date("August 2025"),
            end_date=parse_date("October 2025"),
            image_path="images/event1.png",
            tech_stack=["Flask", "Python", "HTML", "CSS", "JavaScript"]
        ),
        TimelineEvent(
            title="Software Engineer - Intern at Startup",
            description=".",
            category="Work Experience",
            start_date=parse_date("December 2025"),
            end_date=parse_date("February 2026"),
            image_path="images/event2.png",
            tech_stack=["Java (SpringBoot)", "PostgreSQL" ,"React"]
        ),
        TimelineEvent(
            title="Custom Dashboard and Visualization",
            description="My first client project, about a total of 30 hours of work, for about $600 ($20/hour).",
            category="Client Project",
            start_date=parse_date("February 2026"),
            end_date=parse_date("February 2026"),
            image_path="images/project3.png",
            tech_stack=["Java (SpringBoot)", "PostgreSQL" ,"React"]
        ),
        TimelineEvent(
            title="Mastering Algorithms and Data Structures in C/C++ SEEDED at 1:23pm (10th Oct 2025)",
            description="An extension of the Lite ERP for data analytics and visualization.",
            category="Academic",
            start_date=parse_date("October 2025"),
            end_date=parse_date("February 2026"),
            image_path="images/event3.png",
            tech_stack=["C++"])
    ]

    # Add events to the session and commit to the database
    db.session.bulk_save_objects(events)
    db.session.commit()

    print("Database seeded with initial timeline events.")