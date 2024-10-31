@echo off
setlocal enabledelayedexpansion
set ffmpeg="D:\58-ffmpeg\ffmpeg-5.0.1-essentials_build\bin\ffmpeg.exe"
if exist %ffmpeg% (
	for /r . %%i in (*.kux) do (
		%ffmpeg% -y -i "%%i" -c:a copy -c:v copy -threads 2 "%%~dpni.mp4"
	)
) else
echo
pause
