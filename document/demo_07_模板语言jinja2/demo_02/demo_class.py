class Teacher:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def intro(self):
        return f"Teacher:{self.name},has {len(self.students)} student"

    @property
    def property_intro(self):
        return f"Teacher:{self.name},has {len(self.students)} student"
