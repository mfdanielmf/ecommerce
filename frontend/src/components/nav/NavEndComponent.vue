<script setup>
  import BlackButton from '../common/BlackButton.vue';
  import { LogInIcon } from 'lucide-vue-next';
</script>

<template>
  <div class="navbar-end">
      <BlackButton class="group flex items-center gap-2.5">
        <LogInIcon class="group-hover:translate-x-1 transition" />
        <p>Iniciar sesión</p>
      </BlackButton>
    </div>
</template>
