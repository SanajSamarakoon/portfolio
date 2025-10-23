# Seed the initial databases with timeline events
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
            title="Mastering Algorithms and Data Structures in C/C++",
            description="An extension of the Lite ERP for data analytics and visualization.",
            category="Academic",
            start_date=parse_date("October 2025"),
            end_date=parse_date("February 2026"),
            image_path="images/event3.png",
            tech_stack=["C++"]),
        TimelineEvent(
            title="2D Super Mario Game",
            description="A tribute to my first interaction with a computer in 2005 (Grade 4). A 2D platformer game inspired by classic Super Mario.",
            category="Project",
            start_date=parse_date("February 2026"),
            end_date=parse_date("March 2026"),
            image_path="images/project1.png",
            tech_stack=["C++", "SFML"]),
        TimelineEvent(
            title="Lite ERP",
            description="Basic ERP inventory management system with manufacturing and batch traceability features for small to medium businesses.",
            category="Project",
            start_date=parse_date("March 2026"),
            end_date=parse_date("April 2026"),
            image_path="images/project2.png",
            tech_stack=["Java", "SpringBoot", "PostgreSQL", "React", "REST API"]),
        TimelineEvent(
            title="Lite ERP Dashboard",
            description="An extension of the Lite ERP for data analytics and visualization with interactive charts and reporting features.",
            category="Project",
            start_date=parse_date("April 2026"),
            end_date=parse_date("May 2027"),
            image_path="images/project3.png",
            tech_stack=["Java", "SpringBoot", "PostgreSQL", "React", "Chart.js"])
    ]

    # Add events to the session and commit to the database
    db.session.bulk_save_objects(events)
    db.session.commit()

    print("Database seeded with initial timeline events.")