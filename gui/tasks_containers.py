import flet as ft

def tasks_container(tasks, on_task_check):
    return ft.Container(
        height=400,
        content=ft.Column(
            controls=[
                ft.Checkbox(
                    label=task.name,
                    on_change=on_task_check,
                    value=(task.status == 'completed')
                ) for task in tasks
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )