<script setup>
import TopBody from './body-components/TopBodyComponent.vue'
import BottomBodyComponent from './body-components/BottomBodyComponent.vue'

defineProps({
  producto: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <div class="flex flex-col justify-center not-lg:items-center">
    <TopBody :nombre="producto.nombre" :precio="producto.precio" />
    <BottomBodyComponent :producto="producto" />
  </div>
</template>
