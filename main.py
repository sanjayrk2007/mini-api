from fastapi import FastAPI
import sqlite3

def get_db():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if count == 0:
        conn.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [("Buy milk", 0), ("Write report", 0), ("Walk dog", 1)]
        )
        conn.commit()
    conn.close()

init_db()
app=FastAPI()
@app.get("/")
def root():
    return {"message": "Hello, world!"}
@app.get("/health")
def health():
    return {"status": "ok"} 
@app.get("/hello")
def hello(name:str="world"):
    return {"message": f"Hello, {name}!"}
