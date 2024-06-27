import sqlite3

class Database:
    def init(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            username TEXT NULL,
            telegram_id INTEGER NOT NULL UNIQUE 
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, full_name, username, telegram_id):
        sql = """
        INSERT INTO Users(full_name, username, telegram_id) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(full_name, username, telegram_id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        sql = """
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

# Bu funksiya testlash uchun qo'shilgan, xuddi sizning faylingizda.
def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")

# Testing
if name == "main":
    db = Database()

    # Create table
    db.create_table_users()

    # Add user
    db.add_user("John Doe", "johndoe", 12345)

    # Select all users
    all_users = db.select_all_users()
    print("All Users:", all_users)

    # Select user by ID
    user_by_id = db.select_user(id=1)
    print("User by ID:", user_by_id)

    # Count users
    user_count = db.count_users()
    print("User Count:", user_count)