import os
import sys

if os.name != "nt":
    print("Unsupported device. This script can only run on Windows.")
    sys.exit(1)

skrgit = r"""
@echo off
setlocal
set ARG1=%%~1
if "%%ARG1%%"=="-rfg" call :run_from_git %%2 & exit /b
if "%%ARG1%%"=="-py" call :install_python %%2 & exit /b
if "%%ARG1%%"=="" call :run_feature & exit /b
echo Invalid command or arguments.
exit /b
:
:run_from_git
set FILE=%%~1
if "%%FILE%%"=="" (
echo Error: No file specified for -rfg. Provide a file name.
exit /b
)
set BASE_URL=https://github.com/SirPigari/skrgit/blob/main/
echo Downloading %%FILE%% from %%BASE_URL%%%%FILE%%...
curl -o "%%FILE%%" "%%BASE_URL%%%%FILE%%" >nul 2>&1
if errorlevel 1 (
echo Failed to download file: %%FILE%%.
exit /b
)
if "%%FILE:~-3%%"==".py" (
echo Running Python script...
python "%%FILE%%"
) else if "%%FILE:~-4%%"==".bat" (
echo Running batch script...
call "%%FILE%%"
) else if "%%FILE:~-4%%"==".cmd" (
echo Running command script...
call "%%FILE%%"
) else if "%%FILE:~-4%%"==".exe" (
echo Running executable...
"%%FILE%%"
) else (
echo Unsupported file type: %%FILE%%
)
del "%%FILE%%" >nul 2>&1
exit /b
:
:install_python
set VERSION=%%~1
if "%%VERSION%%"=="" (
echo Error: No version specified for Python installation. Use -py -v:<version>.
exit /b
)
echo Installing Python version %%VERSION%%...
curl -o "python-installer.exe" "https://www.python.org/ftp/python/%%VERSION%%/python-%%VERSION%%-amd64.exe" >nul 2>&1
if errorlevel 1 (
echo Failed to download Python installer.
exit /b
)
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
del python-installer.exe >nul 2>&1
exit /b
:
:run_feature
echo Placeholder: Custom feature logic goes here.
exit /b
"""

try:
    with open(r"C:\Windows\skrgit.bat", "w", encoding="utf-8") as f:
        f.write(skrgit)
    print("Batch file created successfully!")
except PermissionError:
    print("Permission denied: Run the script as administrator to write to C:/Windows.")
    sys.exit(1)

# Self-deleting script
try:
    os.remove(__file__)
    print("Script deleted successfully.")
except Exception as e:
    print(f"Error deleting script: {e}")