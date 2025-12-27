<script setup>
import { RouterView } from 'vue-router'
import { Toaster } from 'vue-sonner'
import 'vue-sonner/style.css'
import { onMounted } from 'vue'
import authApi from './api/authApi'
import { useAuthStore } from './stores/authStore'

const authStore = useAuthStore()

onMounted(async () => {
  authStore.cargandoUsuario = true

  try {
    const req = await authApi.obtenerUsuario()

    authStore.usuario = req.data.usuario
  } catch {
    authStore.usuario = null
  } finally {
    authStore.cargandoUsuario = false
  }
})
</script>

<template>
  <Toaster rich-colors :close-button="true" position="top-right" />

  <RouterView />
</template>
