import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import Courses from './Courses.vue'

import App from './App.vue'
// import router from './router/index.ts'

const app = createApp(App)

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // { path: '/', component: App },
    { path: '/', name: 'courses', component: Courses },
  ],
})


app.use(createPinia())
app.use(router)

app.mount('#app')
