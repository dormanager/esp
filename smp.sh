#!/bin/bash
while pgrep espresso; do  sleep 1m && ls -lh esp_out1 ; done
