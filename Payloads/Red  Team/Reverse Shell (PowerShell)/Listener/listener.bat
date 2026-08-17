@echo off
title ATTP Listener
cd /d "%~dp0"
python listener.py %*
pause
