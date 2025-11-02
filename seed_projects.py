
# Seed the initial databases with projects
import json
from app import app, db
from models import Project
from datetime import datetime

with app.app_context():
    # Clear existing projects
    Project.query.delete()

    # Define projects
    projects = [
        Project(
            title="Portfolio Website",
            description="My first project. A responsive portfolio website built with Flask and Bootstrap to showcase my work and skills.",
            image="project0.png",
            tech_stack=["Python", "Flask", "HTML", "CSS", "JavaScript", "Bootstrap"],
            demo_url="#",
            github_url="#",
            timeline_event_id=2
        ),
        Project(
            title="2D Super Mario Game",
            description="A tribute to my first interaction with a computer in 2005 (Grade 4). A 2D platformer game inspired by classic Super Mario.",
            image="project1.png",
            tech_stack=["C++", "SFML", "Game Development"],
            demo_url="#",
            github_url="#",
            timeline_event_id=6
        ),
        Project(
            title="Lite ERP",
            description="Basic ERP inventory management system with manufacturing and batch traceability features for small to medium businesses.",
            image="project2.png",
            tech_stack=["Java", "SpringBoot", "PostgreSQL", "React", "REST API"],
            demo_url="#",
            github_url="#",
            timeline_event_id=7
        ),
        Project(
            title="Lite ERP Dashboard",
            description="An extension of the Lite ERP for data analytics and visualization with interactive charts and reporting features.",
            image="project3.png",
            tech_stack=["Java", "SpringBoot", "PostgreSQL", "React", "Chart.js"],
            demo_url="#",
            github_url="#",
            timeline_event_id=8
        ),
    ]

    # Add projects to the session and commit to the database
    db.session.bulk_save_objects(projects)
    db.session.commit()

    print("Database seeded with initial projects.")