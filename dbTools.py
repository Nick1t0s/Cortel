import psycopg2
import hashlib
sha256_hash = hashlib.new('sha256')

class database:
    def __init__(self, db_name, db_user, db_pass, db_host):
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.sha256 = hashlib.sha256()

    def check_password(self, username, password):
        sha256_hash.update(password.encode('utf-8'))
        reslHash = self.getPass(username)
        if reslHash == sha256_hash.hexdigest():
            return True
        else:
            return False

    def getPass(self, username):
        try:
            conn = psycopg2.connect(dbname = self.db_name, user =  self.db_user, password =  self.db_pass, host = self.db_host)
        except:
            pass
        else:
            cursor = conn.cursor()
            cursor.execute(f"SELECT password_hash FROM Users WHERE username = '{username}';")
            password = cursor.fetchall()
            conn.close()
            if password:
                return password[0][0]
            else:
                return False

    def getChats(self, username):
        try:
            conn = psycopg2.connect(dbname = self.db_name, user =  self.db_user, password =  self.db_pass, host = self.db_host)
        except:
            pass
        else:
            cursor = conn.cursor()
            cursor.execute(f"SELECT chats FROM Users WHERE username = '{username}';")
            res = cursor.fetchall()[0][0]
            return res


db = database("postgres", "postgres", "1", "localhost")
print(db.getChats("nick1t1s"))