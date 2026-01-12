import { createRouter, createWebHistory } from 'vue-router'
import Courses from '../views/Courses.vue'
import App from '../App.vue'
import Home from '../views/Home.vue'

const routes = [
  { 
    path: '/',
    name: 'home',
    component: Home 
  },
  { 
    path: '/courses',
    name: 'courses',
    component: Courses
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
