<script setup>
import { RouterView } from 'vue-router'
import { Toaster } from 'vue-sonner'
import 'vue-sonner/style.css'
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth.store'

const authStore = useAuthStore()

onMounted(async () => {
  authStore.cargarUsuario()
})
</script>

<template>
  <Toaster rich-colors :close-button="true" position="top-right" />

  <RouterView />
</template>
