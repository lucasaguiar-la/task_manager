import flet as ft
from database.db_manager import DBManager
from gui.main_page import main_page
from models.task import Task
from gui.tasks_containers import tasks_container

class ToDoApp:
    def __init__(self):
        self.db_manager = DBManager()
        self.tasks = self._load_tasks()
        self.task = ""
        self.view = 'all'

    def _load_tasks(self):
        results = self.db_manager.execute_query('SELECT * FROM tasks')
        return [Task(name, status) for name, status in results]

    def set_task_value(self, e):
        self.task = e.control.value

    def add_task(self, e, input_task):
        name = self.task
        if name:
            new_task = Task(name)
            self.db_manager.execute_query('INSERT INTO tasks VALUES(?, ?)', [new_task.name, new_task.status])
            input_task.value = ''
            self.tasks = self._load_tasks()
            self.update_task_list(e.page)

    def check_task(self, e):
        is_checked = e.control.value
        label = e.control.label
        status = "complete" if is_checked else "incomplete"
        self.db_manager.execute_query('UPDATE tasks SET status = ? WHERE name = ?', [status, label])
        self.tasks = self._load_tasks()
        self.update_task_list(e.page)

    def tab_changed(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.tasks = self._load_tasks()
            self.view = 'all'
        elif selected_index == 1:
            self.tasks = [task for task in self._load_tasks() if task.status == "incomplete"]
            self.view = 'incomplete'
        elif selected_index == 2:
            self.tasks = [task for task in self._load_tasks() if task.status == "complete"]
            self.view = 'complete'
        self.update_task_list(e.page)

    def update_task_list(self, page):
        page.controls.pop()
        tasks = tasks_container(self.tasks, self.check_task)
        page.add(tasks)
        page.update()

    def main(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 400
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'ToDo App'
        main_page(self.page, self.db_manager, self.add_task, self.check_task, self.tab_changed)

ft.app(target=ToDoApp().main)
