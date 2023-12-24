<template>
  <div class="header">
    <div class="slogan">
      <p>老男孩IT教育 | 帮助有志向的年轻人通过努力学习获得体面的工作和生活</p>
    </div>
    <div class="nav">
      <ul class="left-part">
        <li class="logo">
          <router-link to="/">
            <img src="../assets/img/head-logo.svg" alt="">
          </router-link>
        </li>
        <li class="ele">
          <span @click="goPage('/free-course')" :class="{active: url_path === '/free-course'}">免费课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/actual-course')" :class="{active: url_path === '/actual-course'}">实战课</span>
        </li>
        <li class="ele">
          <span @click="goPage('/light-course')" :class="{active: url_path === '/light-course'}">轻课</span>
        </li>
      </ul>

      <div class="right-part">
        <div v-if="!username">
          <span @click="put_login">登录</span>
          <span class="line">|</span>
          <span @click="put_register">注册</span>
        </div>
        <div v-else>
          <span>{{ username }}</span>
          <span class="line">|</span>
          <span @click="logout">注销</span>
        </div>
      </div>
      <Login v-if="is_login" @close="close_login" @go="put_register" @loginsuccess="login_success"/>
      <Register v-if="is_register" @close="close_register" @go="put_login"/>
    </div>
  </div>

</template>

<script>
import Login from "@/components/Login";
import Register from "@/components/Register";

export default {
  name: "Header",
  data() {
    return {
      // 当前所在路径，去sessionStorage取的，如果取不到，就是 /
      url_path: sessionStorage.url_path || '/',
      is_login: false,
      is_register: false,
      token: '',
      username: '',
    }
  },
  methods: {
    goPage(url_path) {
      // 已经是当前路由就没有必要重新跳转
      if (this.url_path !== url_path) {
        this.$router.push(url_path);
      }
      sessionStorage.url_path = url_path;
    },
    close_login() {
      this.is_login = false
    },
    close_register() {
      this.is_register = false
    },
    put_register() {
      this.is_register = true
      this.is_login = false
    },
    put_login() {
      this.is_register = false
      this.is_login = true
    },
    login_success() {
      this.username = this.$cookies.get('username')
      this.token = this.$cookies.get('token')
    },
    logout() {
      this.$cookies.remove('username')
      this.$cookies.remove('token')
      this.username = ""
      this.token = ""
    },
  },
  created() {
    // 组件加载万成，就取出当前的路径，存到sessionStorage  this.$route.path
    sessionStorage.url_path = this.$route.path;
    // 把url_path = 当前路径
    this.url_path = this.$route.path;

    this.username = this.$cookies.get('username')
    this.token = this.$cookies.get('token')
  },
  components: {
    Login,
    Register
  },

}
</script>

<style scoped>
.header {
  background-color: white;
  box-shadow: 0 0 5px 0 #aaa;
}

.header:after {
  content: "";
  display: block;
  clear: both;
}

.slogan {
  background-color: #eee;
  height: 40px;
}

.slogan p {
  width: 1200px;
  margin: 0 auto;
  color: #aaa;
  font-size: 13px;
  line-height: 40px;
}

.nav {
  background-color: white;
  user-select: none;
  width: 1200px;
  margin: 0 auto;

}

.nav ul {
  padding: 15px 0;
  float: left;
}

.nav ul:after {
  clear: both;
  content: '';
  display: block;
}

.nav ul li {
  float: left;
}

.logo {
  margin-right: 20px;
}

.ele {
  margin: 0 20px;
}

.ele span {
  display: block;
  font: 15px/36px '微软雅黑';
  border-bottom: 2px solid transparent;
  cursor: pointer;
}

.ele span:hover {
  border-bottom-color: orange;
}

.ele span.active {
  color: orange;
  border-bottom-color: orange;
}

.right-part {
  float: right;
}

.right-part .line {
  margin: 0 10px;
}

.right-part span {
  line-height: 68px;
  cursor: pointer;
}
</style>
