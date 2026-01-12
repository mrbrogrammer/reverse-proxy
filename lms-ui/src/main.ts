import { createApp } from 'vue'
// import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import Courses from './Courses.vue'

import App from './App.vue'
// import router from './router/index.ts'

const app = createApp(App)

const routes = [
    { 
      path: '/',
      name: 'home',
      component: App 
    },
    { 
      path: '/courses',
      name: 'courses',
      component: Courses
   }
  ]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


// export default router

// app.use(createPinia())
app.use(router)

app.mount('#app')
