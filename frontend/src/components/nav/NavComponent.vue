<script setup>
import NavStartComponent from './nav-start/NavStartComponent.vue'
import NavCenterComponent from './nav-center/NavCenterComponent.vue'
import NavEndComponent from './nav-end/NavEndComponent.vue'
</script>

<template>
  <div class="navbar bg-white/80 shadow-sm fixed top-0 backdrop-blur-md z-30">
    <NavStartComponent />

    <NavCenterComponent />

    <NavEndComponent />
  </div>
</template>
