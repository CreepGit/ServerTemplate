import { createApp, devtools } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')

if (!(devtools == undefined || devtools.enabled == false)) {
    document.title = "Dev " + document.title
}

