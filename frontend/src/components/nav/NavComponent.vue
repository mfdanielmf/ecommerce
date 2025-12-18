<script setup>
import NavStartComponent from './NavStartComponent.vue';
import NavCenterComponent from './NavCenterComponent.vue';
import NavEndComponent from './NavEndComponent.vue';
</script>

<template>
  <div class="navbar bg-white/80 shadow-sm fixed top-0 backdrop-blur-md z-30">
    <NavStartComponent />

    <NavCenterComponent />

    <NavEndComponent />
  </div>
</template>
