import Vue from 'vue'
import VueRouter from 'vue-router'
import login from "../components/login";
import register from "../components/register";
import firstpage from "../components/firstpage";
import user from "../components/user";
import team from "../components/team";
import favorites from "../components/favorites"
Vue.use(VueRouter)

const routes = [
  {path: '/',redirect: '/login'},
  {path:'/login',component:login},
  {path: '/login/register',component: register},
  {path: '/firstpage',component: firstpage,children:[
      {path:'/user',component:user},
      {path:'/team',component:team},
          {path:'/favorites',component:favorites},
      ]},

]

const router = new VueRouter({
  routes
})

export default router
