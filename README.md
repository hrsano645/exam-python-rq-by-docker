# exam-python-rq-by-docker

## requirement

* python3.11
* docker
* (dev)rye

## How to run

* (dev) rye sync
* single worker: docker-compose up
* multiple worker: docker-compose up --scale worker=4

# Reference

* <https://python-rq.org/>
* [Python で分散タスクキュー (RQ 編) #Python - Qiita](https://qiita.com/hoto17296/items/39597f6e26c0186a6e1b)
