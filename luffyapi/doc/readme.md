创建虚拟环境：
pip install virtualenv
pip install virtualenvwrapper-win
添加环境变量 WORKON_ HOME:E:\Virtualenvs
管理员执行 scripts下的virtualenvwrapper.bat


workon xxx
mkvirtualenv.bat -p python luffy  创建虚拟环境

deactivate 退出当前虚拟环境

rmvirtualenv xxx 删除xxx虚拟环境

数据库配置：
create  databases  luffyapi;
select user,host from mysql.user;
grant all privileges on luffyapi.* to 'luffyapi'@'%' identified by '123456';

flush privileges;





