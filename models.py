# Models to handle the Database Data Entry and Retrieval
import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Timeline Event Model
class TimelineEvent(db.Model):
    __tablename__ = 'timeline_events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False) # Academic, Project, Work Experience, Client Project (Freelance)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False) # Can be "Ongoing/In Progress"
    image_path = db.Column(db.String(250))
    tech_stack_json = db.Column(db.Text) # JSON encoded list of technologies used

    def __repr__(self):
        return f"<TimelineEvent {self.title} - {self.category}>"
    
    @property
    def is_ongoing(self):
        return self.end_date is None
    
    @property
    def tech_stack(self):
        if self.tech_stack_json:
            return json.loads(self.tech_stack_json)
        return []
    
    @tech_stack.setter
    def tech_stack(self, value):
        self.tech_stack_json = json.dumps(value)

# Projects Model
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(250))
    tech_stack_json = db.Column(db.Text) # JSON encoded list of technologies used
    demo_url = db.Column(db.String(250), default="#")
    github_url = db.Column(db.String(250), default="#")
    timeline_event_id = db.Column(db.Integer, db.ForeignKey('timeline_events.id'))

    # Relationship to TimelineEvent
    timeline_event = db.relationship('TimelineEvent', backref=db.backref('projects', uselist=False))
    def __repr__(self):
        return f"<Project {self.title}>"
    
    @property
    def tech_stack(self):
        if self.tech_stack_json:
            return json.loads(self.tech_stack_json)
        return []
    
    @tech_stack.setter
    def tech_stack(self, value):
        self.tech_stack_json = json.dumps(value)