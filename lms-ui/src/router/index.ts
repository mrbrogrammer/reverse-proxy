import { createRouter, createWebHistory } from 'vue-router'
import Courses from '../Courses.vue'
import App from '../App.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: App },
    { path: '/courses', component: Courses }
  ],
})

export default router
