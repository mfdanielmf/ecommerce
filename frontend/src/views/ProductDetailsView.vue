<script setup>
import { productStore } from '@/stores/productosStore'
import { onMounted, computed } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ErrorMessage from '@/components/common/ErrorMessage.vue'

const props = defineProps({
  id: {
    required: true,
  },
})

const almacenProductos = productStore()
const producto = computed(() => {
  return almacenProductos.productoId
})

onMounted(async () => {
  almacenProductos.error = null
  if (!producto.value) {
    await almacenProductos.fetchProductoId(props.id)
  }
})
</script>

<template>
  <div v-if="almacenProductos.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="almacenProductos.error">{{ almacenProductos.error }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4r">
    <h1 v-if="producto">Detalles producto {{ producto.id }}</h1>
  </main>
</template>
