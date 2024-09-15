@echo off
setlocal

:: Check if Python is already installed
python --version >nul 2>&1
if %errorlevel%==0 (
    echo Python is already installed.
    exit /b 0
)

:: Set Python version and URL
set "PYTHON_VERSION=3.11.5"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe"
set "INSTALLER=python-installer.exe"

:: Download the Python installer
echo Downloading Python %PYTHON_VERSION%...
powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %INSTALLER%"

:: Check if the download was successful
if not exist %INSTALLER% (
    echo Failed to download Python installer.
    exit /b 1
)

:: Install Python silently and add to PATH
echo Installing Python %PYTHON_VERSION%...
%INSTALLER% /quiet InstallAllUsers=1 PrependPath=1

:: Check if the installation was successful
python --version >nul 2>&1
if %errorlevel%==0 (
    echo Python %PYTHON_VERSION% was installed successfully.
) else (
    echo Python installation failed.
    exit /b 1
)

:: Clean up
del %INSTALLER%
echo Installation complete.

endlocal
exit /b 0
