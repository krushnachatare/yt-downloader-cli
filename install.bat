@echo off
echo ====================================
echo Installing YouTube Downloader...
echo ====================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo Python is not installed.
        echo Please install Python first from:
        echo https://python.org
        pause
        exit /b
    )
)

py -m pip install -r requirements.txt 2>nul || python -m pip install -r requirements.txt

echo.
echo ====================================
echo Installation Complete!
echo.
echo IMPORTANT:
echo Please install FFmpeg and add it to PATH.
echo ====================================
pause