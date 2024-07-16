
class Task:
    def __init__(self, name, status='incomplete'):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"Task(name={self.name}), status={self.status})"