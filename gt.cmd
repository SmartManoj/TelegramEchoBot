@echo off
rem heroku login
::heroku create
git init
heroku git:remote -a navaexp
git add .
git commit -m 'Cool'
::heroku pg:killall
if "%1" NEQ "1" (
	git push heroku master
	heroku ps:scale web=1
)		
echo %date%,%time%


