this is a web project based on django
初步实现网页雏形
开始实现部署
Successfully installed django-bootstrap3-11.1.0
初步实现界面美化
实现部署
Successfully installed dj-database-url-0.5.0
Successfully installed dj-static-0.0.6 static3-0.7.0
Successfully installed gunicorn-19.9.0

建立在线数据库
先进行数据库迁移
heroku run python manage.py migrate
改进heroku的部署
创建超级用户
python manage.py createsuperuser
在heroku上创建用户友好的url
heroku app:rename learning_log
提交推送
git commmit -am "something"
git status
git push heroku master
此时不会重建数据库，所以不用进行数据库的迁移
add delete entry
