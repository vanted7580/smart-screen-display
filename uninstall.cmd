@echo off
net.exe session 1>NUL 2>NUL && (
    goto install
) || (
    echo Please run this script as Administrator.
   goto end
)

:install

cd /d "%~dp0"

SET destination="C:\Program Files\Smart Screen Display\"
SET cdestination="C:\ProgramData\Smart Screen Display\"
SET program="Smart Screen Display.exe"
SET config="Smart Screen Display.ini"
SET taskxml="Smart Screen Display.xml"
SET taskname="Smart Screen Display"
SET taskuser="%ComputerName%\%UserName%"

rd /s /q %destination%
schtasks /delete /tn %taskname% /f
echo Uninstalled

:end
pause