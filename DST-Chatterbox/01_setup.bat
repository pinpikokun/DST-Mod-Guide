@echo off
echo ============================================
echo   Chatterbox TTS Setup
echo ============================================
echo.

echo [1/5] Checking Python...
python --version 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python not found.
    echo Install Python 3.11 from:
    echo https://www.python.org/downloads/release/python-3119/
    echo Check "Add Python to PATH" during install.
    pause
    exit /b 1
)

echo.
echo [2/5] Creating virtual environment...
if exist venv (
    echo venv already exists. Skipping.
) else (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create venv.
        pause
        exit /b 1
    )
)

call venv\Scripts\activate.bat

echo.
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [4/5] Installing PyTorch (CPU)... This takes a few minutes.
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

echo.
echo [5/5] Installing Chatterbox TTS...
pip install chatterbox-tts

echo.
echo ============================================
echo   Setup Complete!
echo ============================================
echo.
echo Next: Put Captain_Teemo_on_duty.wav here, then run 02_generate.bat
echo.
pause
