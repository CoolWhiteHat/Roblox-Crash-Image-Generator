@echo off

echo Checking if Python is installed...
echo Sprawdzanie czy Python jest zainstalowany...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    echo Python nie jest zainstalowany. zainstaluj Pythona i sprobuj ponownie.
    pause
    exit /b 1
)

echo Upgrade pip to the latest version...
echo Aktualizowanie pip do ostatniej wersji...
python -m pip install --upgrade pip

echo Installing required Python packages...
echo Instalacja potrzebnych pakietow...

echo Install required packages...
echo Instalowanie potrzebnych pakietow...
python -m pip install pillow

echo All required packages have been installed.
echo Wszystkie potrzebne pakiety zostaly zainstalowane.

pause
