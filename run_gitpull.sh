#!/usr/bin/env bash
pid=`ps -ef|grep gitpull.py|grep -v grep|awk '{print $2}'`
if [ -n $pid ]; then
    kill $pid
fi
nohup python gitpull.py > gitpull.log & sleep 0