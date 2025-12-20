<script setup>
import { RouterView } from 'vue-router'
import NavComponent from './components/nav/NavComponent.vue'
import { Toaster } from 'vue-sonner'
import 'vue-sonner/style.css'
</script>

<template>
  <Toaster rich-colors :close-button="true" position="top-right" />
  <NavComponent />
  <RouterView />
</template>
