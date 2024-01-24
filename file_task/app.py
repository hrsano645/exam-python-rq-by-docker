import os
import redis
from rq import Queue
from tasks import create_files


NUM_FILES = 100
FILE_SIZE = 1048576
NUM_TASKS = 3

q = Queue(connection=redis.from_url(os.environ.get("RQ_REDIS_URL")))

# タスクの実行をキューに投げる
tasks = [
    q.enqueue(create_files, args=(NUM_FILES, FILE_SIZE, f"test_files_{i}"))
    for i in range(NUM_TASKS)
]
