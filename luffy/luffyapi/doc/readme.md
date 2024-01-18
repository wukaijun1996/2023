
django3.2.18
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
create  database  luffyapi;
select user,host from mysql.user;
grant all privileges on luffyapi.* to 'luffyapi'@'%' identified by '123456';

flush privileges;

跨域问题解决（同源策略）:
CORS:跨域资源共享
csrf: 跨站请求伪造
xss: 跨站请求攻击
pip install django-cors-headers


Redis:
https://c.biancheng.net/redis/windows-installer.html
Redis-x64-5.0.14.1.msi 安装包，将服务加到环境变量  执行 redis-cli 进入服务
pip install django-redis 

celery:
pip install celery
pip install eventlet
celery  -A celery_task  worker  -l info -P eventlet
celery  -A celery_task  beat  -l info


vue环境搭建:
https://nodejs.org/zh-cn/download/  （64 msi）
node -v
npm -v 
安装目录下新建两个文件夹【node_global】和【node_cache】
npm config set prefix "D:\develop\Node.js\node_global"
npm config set cache "D:\develop\Node.js\node_cache"
配置环境变量
变量名：NODE_PATH
变量值：C:\Program Files\nodejs\node_global\node_modules
编辑【用户变量】中的【Path】
系统变量】中选择【Path】点击【编辑】添加【NODE_PATH】，
npm install express -g   // -g代表全局安装
npm config set registry https://registry.npm.taobao.org
npm config get registry
npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm -v
cnpm install -g @vue/cli
vue create luffycity
cd luffycity
npm run serve


cnpm install axios //要在项目下执行，会安装在node_modules下
在main.js下配置
import axios from 'axios'
Vue.prototype.$axios = axios

cnpm install vue-cookies
cnpm install element-ui
cnpm install jquery
cnpm install bootstrap@3

xadmin配置：
python manage.py createsuperuser
pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2


配置镜像源：
vim /etc/yum.repos.d/aliyun.repo
[appstream]
name=appstream
baseurl=https://mirrors.aliyun.com/rockylinux/9/AppStream/x86_64/os/
gpgcheck=0
[baseos]
name=baseos
baseurl=https://mirrors.aliyun.com/rockylinux/9/BaseOS/x86_64/os/
gpgcheck=0
必要
yum install  openssl-devel bzip2-devel expat-devel  readline-devel sqlite-devel psmisc libffi-devel -y
yum install gdbm-libs.i686
下载开发工具包：
 yum -y groupinstall "Development tools"
 
nginx:
./configure --prefix=/usr/local/nginx 
./configure --with-cc-opt='-Wno-error -Wno-deprecated-declarations'    --with-http_ssl_module  # https 报错就这样，然后make生成objs/nginx




#安装nginx所需要的依赖包
yum install -y gcc-c++	zlib zlib-devel	openssl openssl-devel pcre pcre-devel

#查看已放行的端口
firewall-cmd --list-all
#将80端口加入到防火墙放行白名单中，并重载防火墙
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --reload

#临时关闭防火墙
systemctl stop firewalld.service
#永久关闭防火墙
systemctl disable firewalld.service