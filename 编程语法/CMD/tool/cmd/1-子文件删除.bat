@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
set /p dir_p=请输入目录路径:
set "dir_p2=%dir_p%\\*"
del /s /q %dir_p2%
pause