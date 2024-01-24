import os
from time import sleep
import redis
from rq import Queue
from tasks import add

q = Queue(connection=redis.from_url(os.environ.get("RQ_REDIS_URL")))

# 10個のタスクの実行をキューに投げる
tasks = [q.enqueue(add, args=(i, 1)) for i in range(10)]

# タスク実行が完了するまで少し待つ
sleep(1)

# 結果を出力する
print([task.result for task in tasks])
