@echo off
chcp 65001
mode con: cols=80 lines=25
color 09
D: && cd D:\0-code\rust_pro
set /p pro_path=请输入要清除exe的项目路径:
cd %pro_path%
cargo clean
pause