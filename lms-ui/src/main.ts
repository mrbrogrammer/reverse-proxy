import { createApp } from 'vue'
// import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router/index.ts'

const app = createApp(App)

// export default router

// app.use(createPinia())
app.use(router)

app.mount('#app')
