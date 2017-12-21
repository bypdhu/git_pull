#!/usr/bin/env bash
kill `ps -ef|grep gitpull.py|grep -v grep|awk '{print $2}'`
nohup python gitpull.py > gitpull.log & sleep 0