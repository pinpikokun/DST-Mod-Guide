@echo off
echo ============================================
echo   Voice Generation
echo ============================================
echo.

if not exist venv\Scripts\activate.bat (
    echo [ERROR] venv not found. Run 01_setup.bat first.
    pause
    exit /b 1
)
call venv\Scripts\activate.bat

if not exist wav (
    echo [ERROR] "wav" folder not found.
    echo Create a "wav" folder and put reference WAV files in it.
    pause
    exit /b 1
)

echo Running on CPU - this takes 30sec to a few minutes per line.
echo Please wait...
echo.

python generate_voice.py

echo.
pause