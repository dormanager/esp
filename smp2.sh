#!/bin/bash
if pgrep espresso
then
sudo criu dump -D checkpoint -t $PID --shell-job
sleep 10s
sudo criu restore -d -D checkpoint --shell-job
fi
