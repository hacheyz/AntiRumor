import { createRouter, createWebHistory } from 'vue-router'
import LayoutVue from '@/views/Layout.vue'
import HomeVue from '@/views/home/Home.vue'
import ListVue from '@/views/list/List.vue'
import JudgeVue from '@/views/judge/Judge.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'root',
      component: LayoutVue,
      redirect: '/home',
      children: [
        { path: '/home', name: 'home', component: HomeVue },
        { path: '/list', name: 'list', component: ListVue },
        { path: '/judge', name: 'judge', component: JudgeVue },
      ]
    }
  ]
})

export default router
