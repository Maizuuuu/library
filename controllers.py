from todo.models import TaskRepo
from todo.views import make_buttons_for_tasks_list, make_buttons_for_task


def get_task_list(user_id):
    tasks = TaskRepo().get_by_user_id(user_id)
    kb = make_buttons_for_tasks_list(tasks)
    return kb


def get_task(id):
    task = TaskRepo().get(id)
    text, kb = make_buttons_for_task(task)
    return text, kb


def add_new_task(user_id, text, author, status, added_at):
    TaskRepo().add_task(user_id, text, author, status, added_at)
def update_task(user_id, text, author, status, added_at):
    TaskRepo().update(updated_task=get_task(id))