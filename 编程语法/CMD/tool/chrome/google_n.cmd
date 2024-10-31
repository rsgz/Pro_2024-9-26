@echo off
chcp 65001
set /p duankou=请输入谷歌浏览器端口9530: 
"D:\58-chrome\chrome-win64\chrome.exe" --user-data-dir="D:\58-chrome\user01" --remote-debugging-port=%duankou%
pause