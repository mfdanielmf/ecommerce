<script setup>
import BlackButton from '../common/BlackButton.vue'
import { LogInIcon } from 'lucide-vue-next'
import CarritoDrawerComponent from './carrito/CarritoDrawerComponent.vue'
</script>

<template>
  <div class="navbar-end flex items-center gap-4">
    <CarritoDrawerComponent />

    <div class="h-5 w-px bg-neutral-300 mx-1"></div>

    <BlackButton class="group flex items-center gap-2.5">
      <LogInIcon class="group-hover:translate-x-1 transition" />
      <p>Iniciar sesión</p>
    </BlackButton>
  </div>
</template>
