import Vue from 'vue'
import VueRouter from 'vue-router'
import login from "../components/login";
import register from "../components/register";

Vue.use(VueRouter)

const routes = [
  {path: '/',redirect: '/login'},
  {path:'/login',component:login},
  {path: '/login/register',component: register},
]

const router = new VueRouter({
  routes
})

export default router
