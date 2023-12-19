import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LightCourse from '../views/LightCourse.vue'
import FreeCourse from '../views/FreeCourse.vue'
import ActualCourse from '../views/ActualCourse.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/light-course',
        name: 'LightCourse',
        component: LightCourse
    },
    {
        path: '/free-course',
        name: 'FreeCourse',
        component: FreeCourse
    },
    {
        path: '/actual-course',
        name: 'ActualCourse',
        component: ActualCourse
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
