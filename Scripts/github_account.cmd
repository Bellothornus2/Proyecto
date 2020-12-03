@echo off

set /p name=usuario GitHub:
set /p email=Email GitHub

git config --unset credential.helper
git config --global user.name %name%
git config --global user.email %email%

set name=
set email=
echo se ha cambiado tu cuenta de Github