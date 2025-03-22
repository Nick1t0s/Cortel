from fastapi import FastAPI
import dbTools
import uvicorn
db = dbTools.database("postgres", "postgres", "1", "localhost")
app = FastAPI()
@app.get('/api/getMessages')
def hello_world(username, password, chatID):
    if db.check_password(username, password):
        if int(chatID) in db.getChats(username):
            return True
    else:
        return False
    return 'Hello, World!'



uvicorn.run(
        app,
        host="0.0.0.0",
        port=25565
)