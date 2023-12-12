
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
create  databases  luffyapi;
select user,host from mysql.user;
grant all privileges on luffyapi.* to 'luffyapi'@'%' identified by '123456';

flush privileges;

跨域问题解决（同源策略）:
CORS:跨域资源共享
csrf: 跨站请求伪造
xss: 跨站请求攻击
pip install django-cors-headers





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



xadmin配置：
python manage.py createsuperuser
pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2