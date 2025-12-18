<script setup>
import { productStore } from '@/stores/productosStore'
import { computed, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ErrorMessage from '@/components/common/ErrorMessage.vue'
import ImgComponent from '@/components/product-details/ImgComponent.vue'
import DetailsBodyComponent from '@/components/product-details/DetailsBodyComponent.vue'

const props = defineProps({
  id: {
    required: true,
  },
})

const almacenProductos = productStore()

const producto = computed(() => {
  return almacenProductos.getProductoPorId(Number(props.id))
})

onMounted(async () => {
  almacenProductos.error = null

  if (!producto.value) {
    await almacenProductos.fetchProductoId(Number(props.id))
  }
})
</script>

<template>
  <div v-if="almacenProductos.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="almacenProductos.error">{{ almacenProductos.error }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4 grid place-content-center">
    <div v-if="producto" class="grid lg:grid-cols-2 gap-12 mb-16">
      <ImgComponent :img_url="producto.img_url" :alt="producto.nombre" />
      <DetailsBodyComponent :producto="producto" />
    </div>
  </main>
</template>
