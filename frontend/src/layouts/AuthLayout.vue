<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const esLogin = computed(() => {
  return route.meta.esLogin
})
</script>

<template>
  <section class="flex flex-col items-center justify-center min-h-screen mx-5">
    <div class="bg-white p-10 rounded-md shadow-xl w-full max-w-143.5">
      <div class="text-center">
        <h1 class="mb-1 font-semibold text-3xl text-blue-600">
          {{ esLogin ? 'Iniciar Sesión' : 'Registrarse' }}
        </h1>
        <p class="text-neutral-700">
          {{ esLogin ? 'Inicia sesión en tu cuenta' : 'Regístrate si no tienes una cuenta' }}
        </p>
      </div>

      <main class="mt-8">
        <RouterView />
      </main>

      <p class="text-center mt-4">
        {{ esLogin ? '¿Todavía no tienes una cuenta?' : '¿Ya tienes una cuenta?' }}
        <RouterLink
          :to="esLogin ? { name: 'register' } : { name: 'login' }"
          class="text-blue-600 font-semibold hover:text-blue-800"
          >{{ esLogin ? 'REGISTRARSE' : 'INICIAR SESIÓN' }}</RouterLink
        >
      </p>
    </div>
  </section>
</template>
