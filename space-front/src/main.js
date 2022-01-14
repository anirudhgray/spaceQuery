import { createApp } from 'vue'

import 'primevue/resources/themes/saga-blue/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'
import 'primeflex/primeflex.css'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'

import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import AOS from 'aos'
import 'aos/dist/aos.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
AOS.init()

createApp(App).use(store).use(router, axios).use(PrimeVue, { ripple: true }).use(ToastService).mount('#app')
