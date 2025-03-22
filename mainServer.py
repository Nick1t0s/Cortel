from fastapi import FastAPI, File, UploadFile
import dbTools
import uvicorn
db = dbTools.database("postgres", "postgres", "1", "localhost")
app = FastAPI()

@app.get('/api/getUsers')
def getChats(username, password):
    if db.check_password(username, password):
        return db.getChats(username)
    else:
        raise "Hello world"
@app.get('/api/getMessages')
def getMessages(username, password, chatID):
    if db.check_password(username, password):
        if int(chatID) in db.getChats(username):
            return db.getMessages(chatID)
    else:
        return 'Hello, World!'

@app.get('/api/sendMessage')
def sendMessage(username, password, chatID, content, files):
    if db.check_password(username, password):
        if int(chatID) in db.getChats(username):
            return db.sendMessage(chatID, username, content)
        return "Hello world"

    else:
        return 'Hello, World!'

@app.get('/api/createChat')
def createChat(username, password, name, is_open, users_invite, user_send):
    if db.check_password(username, password):

    else:
        return 'Hello, World!'



uvicorn.run(
        app,
        host="0.0.0.0",
        port=25565
)