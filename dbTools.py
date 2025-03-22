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
        print(password)
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
            cursor.execute(f"SELECT password_hash FROM Users WHERE user_id = '{username}';")
            password = cursor.fetchall()
            conn.close()
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
            cursor.execute(f"SELECT chats FROM Users WHERE user_id = '{username}';")
            res = cursor.fetchall()[0][0]
            conn.close()
            return res

    def getMessages(self, chat_id):
        try:
            conn = psycopg2.connect(dbname = self.db_name, user =  self.db_user, password =  self.db_pass, host = self.db_host)
        except:
            pass
        else:
            cursor = conn.cursor()
            cursor.execute(f"SELECT message_id, chat_id, sender_id, content, content_path, sent_at::text  FROM chat{chat_id};")
            res = cursor.fetchall()
            conn.close()
            return res

    def sendMessage(self, chat_id, from_id, content):
        try:
            conn = psycopg2.connect(dbname=self.db_name, user=self.db_user, password=self.db_pass, host=self.db_host)
        except:
            pass
        else:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT users_send FROM chats where chat_id = '{chat_id}';")
            users_send = cursor.fetchall()[0][0]
            cursor.execute(f"SELECT admins_id FROM chats where chat_id = '{chat_id}';")
            admins = cursor.fetchall()[0][0]
            print(users_send)
            print(type(admins[0]))
            print(type(from_id))
            if users_send or int(from_id) in admins:
                cursor.execute(f"INSERT INTO chat{chat_id} (sender_id, content) "
                               f"VALUES ({from_id}, '{content}');")
                cursor.connection.commit()
                conn.close()
                print('')
                return True
            conn.close()
            return False

    def createChat(self, user_id, name, is_open, users_invite, user_send):
        try:
            conn = psycopg2.connect(dbname=self.db_name, user=self.db_user, password=self.db_pass, host=self.db_host)
        except:
            pass
        else:
            cursor = conn.cursor()
            print(f"INSERT INTO chats (name, users_id, admins_id, open, users_invite, avatar_path, created_by, users_send)"\
                           f"VALUES ({name}, '{{{user_id}}}'::int8[], '{{{user_id}}}'::int8[], {is_open}, {users_invite},"\
                           f"'chatAvatars{user_id}.jpg', {user_send}, {user_send});")
            cursor.execute(f"INSERT INTO chats (name, users_id, admins_id, open, users_invite, avatar_path, created_by, users_send)"\
                           f"VALUES ('{name}', '{{{user_id}}}'::int8[], '{{{user_id}}}'::int8[], {is_open}, {users_invite},"\
                           f"'5', {user_id}, {user_send});")
            #ДОДЕЛАТЬ ЗАПРОС!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



db = database("postgres", "postgres", "1", "localhost")
print(db.createChat(512,"sdf", 'true', 'true', 'true'))