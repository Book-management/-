import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Course  from '@/components/Course'
import New from "@/components/New"

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path:'/course',
      name : "Course",
      component:Course
    },
    {
      path:"/new",
      name : "New",
      component:New
    },
  ]
})
