from celery import Celery
import time

app = Celery('tasks', backend='redis://127.0.0.1', broker='redis://127.0.0.1')

@app.task
def add(x, y):
    return x + y

@app.task
def su(x, y):
    time.sleep(5)
    return x * y