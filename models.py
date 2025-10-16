# Models to handle the Database Data Entry and Retrieval
import json
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

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