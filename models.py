from datetime import datetime
from mongoengine import Document, StringField, DateField, BooleanField

class Todo(Document):
    description = StringField(max_length=250, required=True)
    start_date = DateField(default=datetime.now)
    due_date = DateField()
    completed = BooleanField(default=False)
