from database import create_con


class Task:
    def __init__(self, id, user_id, title, author, status, added_at):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.author = author
        self.status = status
        self.added_at = added_at


class TaskRepo:
    __table_name = "task"

    def get(self, id: int):
        con = create_con()
        SQL = f"SELECT * FROM {self.__table_name} WHERE id = ?"
        query = con.execute(SQL, [id])
        data = query.fetchone()
        return Task(*data)

    def get_by_user_id(self, user_id):
        con = create_con()
        SQL = f"SELECT * FROM {self.__table_name} WHERE user_id = ?"
        query = con.execute(SQL, [user_id])
        data = query.fetchall()
        return [Task(*row) for row in data]

    def add_task(self, user_id: int, text: str, author: str, status: str, added_at:str):
        con = create_con()
        SQL = f"""
            INSERT INTO {self.__table_name}(title, user_id, author, status, added_at)
            VALUES (?, ?, ?, ?, ?)
        """
        con.execute(
            SQL,
            [text, user_id, author, status, added_at],
        )
        con.commit()

    def update(self, updated_task: Task):
        con = create_con()
        SQL = f"""
            UPDATE {self.__table_name}
            SET title = ?,
                author = ?,
                status = ?,
                added_at = ?
            WHERE id = ?
        """
        con.execute(SQL, [
            updated_task.title, 
            updated_task.author,
            updated_task.status,
            updated_task.added_at,
            updated_task.id
        ])
        con.commit()

    def delete(self, id):
        con = create_con()
        SQL = f"""
            DELETE FROM {self.__table_name}
            WHERE id = ?
        """
        con.execute(SQL, [id])
        con.commit()