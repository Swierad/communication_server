from crypto import password_hash
from dbcon import db_connect


class User():
    __user_id = None
    username = None
    __password = None
    user_email = None

    def __init__(self):
        self.__id = -1
        self.username = ""
        self.user_email = ""
        self.__password = ""

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, id):
        self.__user_id = id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def save_to_db(self, db_con=db_connect()):
        c= db_con.cursor()
        if self.__id == -1:
            # saving new instance using prepared statements
            try:
                sql = f"""INSERT INTO Users(user_name, user_email, password)
                         VALUES('{self.username}', '{self.user_email}', '{self.password}') RETURNING user_id"""
                c.execute(sql)

                self.id = c.fetchone()[0]
                c.close()
                print('użytkownik dodany do bazy')
            except Exception as e:
                print(f"failed due to {e}")
        else:
            sql = f"""UPDATE Users(user_name, user_email, password)
                         VALUES('{self.username}', '{self.user_email}', '{self.password}') RETURNING user_id"""

            c.execute(sql)
            c.close()
            return True

    def delete(self, db_con=db_connect()):
        c = db_con.cursor()
        sql = "DELETE FROM Users WHERE id=%s"
        c.execute(sql, (self.__id,))
        self.__id = -1
        return True

    @staticmethod
    def load_user_by_id(user_id, db_con=db_connect() ):
        sql = f"""SELECT user_id, user_name, user_email, password FROM users WHERE user_id='{user_id}'"""
        c = db_con.cursor()
        c.execute(sql, (user_id,))
        data = c.fetchone()
        c.close()
        if data:
            loaded_user = User()
            loaded_user.id = data[0]
            loaded_user.username = data[1]
            loaded_user.email = data[2]
            loaded_user.password = data[3]
            print(loaded_user.username)

    @staticmethod
    def load_all_users(db_con=db_connect()):
        sql = f"""SELECT user_id, user_name, user_email, password FROM users"""
        c = db_con.cursor()
        ret = []
        c.execute(sql)
        for row in c.fetchall():
            loaded_user = User()
            loaded_user.id = row[0]
            loaded_user.username = row[1]
            loaded_user.email = row[2]
            loaded_user.password = row[3]
            ret.append(loaded_user)
        c.close()
        return ret






