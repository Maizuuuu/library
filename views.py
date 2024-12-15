from telebot import types

from todo.models import Task


def make_buttons_for_tasks_list(tasks: list[Task]):
    kb = types.InlineKeyboardMarkup(row_width=1)
    for task in tasks:
        btn = types.InlineKeyboardButton(
            text=task.title, callback_data=f"task/{task.id}"
        )
        kb.add(btn)
    add_btn = types.InlineKeyboardButton(text="Добавить новую", callback_data="add")
    kb.add(add_btn)
    return kb


def make_buttons_for_task(task: Task):
    text = f"{task.title}\n Автор: {task.author}\n Статус: {task.status}\n Дата: {task.added_at}"
    

    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(types.InlineKeyboardButton(text,
        callback_data=f"status/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = 'Изменить',
        callback_data=f"update/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = 'Удалить',
        callback_data=f"remove/{task.id}"
    ))
    kb.add(types.InlineKeyboardButton(
        text = '<- Назад',
        callback_data=f"back"
    ))
    return text, kb