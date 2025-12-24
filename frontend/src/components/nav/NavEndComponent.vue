<script setup>
import { LogInIcon } from 'lucide-vue-next'
import CarritoDrawerComponent from './carrito/CarritoDrawerComponent.vue'
import { useAuthStore } from '@/stores/authStore'
import { defineAsyncComponent } from 'vue'

const AvatarComponent = defineAsyncComponent(() => import('./AvatarComponent.vue'))

const authStore = useAuthStore()
</script>

<template>
  <div class="navbar-end flex items-center gap-4">
    <CarritoDrawerComponent />

    <div class="h-5 w-px bg-neutral-300 mx-1"></div>

    <RouterLink
      v-if="!authStore.usuario"
      :to="{ name: 'login' }"
      class="group flex items-center btn bg-neutral-900 text-white border-none hover:bg-neutral-800"
    >
      <LogInIcon class="group-hover:translate-x-1 transition" />
      <p>Iniciar sesión</p>
    </RouterLink>

    <AvatarComponent v-else :nombre="authStore.usuario.nombre[0]" />
  </div>
</template>
