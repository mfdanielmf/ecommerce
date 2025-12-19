<script setup>
import BlackButton from '../common/BlackButton.vue'
import { LogInIcon } from 'lucide-vue-next'
import CarritoDrawerComponent from './CarritoDrawerComponent.vue'
</script>

<template>
  <div class="navbar-end flex items-center gap-4">
    <CarritoDrawerComponent />

    <BlackButton class="group flex items-center gap-2.5">
      <LogInIcon class="group-hover:translate-x-1 transition" />
      <p>Iniciar sesión</p>
    </BlackButton>
  </div>
</template>
