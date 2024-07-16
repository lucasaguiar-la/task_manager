
import flet as ft
from .tasks_containers import tasks_container

def main_page(page, db_manager, add_task_callback, check_task_callback, tab_change_callback):
    input_task = ft.TextField(hint_text="Digite aqui uma tarefa", expand=True, on_change=add_task_callback)

    input_bar = ft.Row(
        controll=[
            input_task,
            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=lambda e: add_task_callback(e, input_task))
        ]
    )

    tabs = ft.Tabs(
        selected_index=0,
        on_change=tab_change_callback,
        tabs=[
            ft.Tab(text="Todos"),
            ft.Tab(text="Em Andamento"),
            ft.Tab(text="Finalizando")
        ],
    )

    tasks = tasks_container(db_manager.execute_query('SELECT * FROM tasks'), check_task_callback)

    page.add(input_bar, tabs, tasks)
    page.update()