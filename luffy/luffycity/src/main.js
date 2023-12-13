import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

// axios的配置
import axios from 'axios'
Vue.prototype.$axios = axios

//配置全局样式
import '@/assets/css/global.css'

//配置全局自定义设置
import settings from "@/assets/js/settings";
Vue.prototype.$settings = settings
// 在需要用的地方， this.$settings.base_url + '拼接的具体后台路由'

// vue-cookies的配置
import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies

// elementui的配置
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

//bootstrap 配置
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
