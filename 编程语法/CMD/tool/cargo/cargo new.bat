@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
D: && cd D:\0-code\rust_pro
set /p pro=请输入项目名字:
cargo new %pro%
pause