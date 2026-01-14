import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { QueryClient, VueQueryPlugin } from '@tanstack/vue-query'

import App from './App.vue'
import router from './router'

const app = createApp(App)

export const queryClient = new QueryClient({
  defaultOptions:{
    queries:{
      staleTime: 60*1000,
      retry: 1,
      refetchOnWindowFocus: false
    }
  }
})

app.use(createPinia())
app.use(VueQueryPlugin, {queryClient: queryClient})
app.use(router)

app.mount('#app')
