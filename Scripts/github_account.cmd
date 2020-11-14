@echo off


set /p account=Elige Personal o Educativa (P o E):

if %account%==P goto :personal 
if %account%==E goto :educativa

:educativa
git config --unset credential.helper
git config --global user.name bellothornus2
git config --global user.email divanov@cifpfbmoll.eu
goto :final2

:personal
git config --unset credential.helper
git config --global user.name bellothornus
git config --global user.email bellothornus@gmail.com
goto :final2

:final2
set account=
echo se ha cambiado tu cuenta de Github