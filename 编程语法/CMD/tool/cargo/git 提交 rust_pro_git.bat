@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
D: && cd D:\0-code\rust_pro\rust_pro_git
set /p info=请输入main分支改动信息:
git add .
git commit -m %info%
git push origin main
pause