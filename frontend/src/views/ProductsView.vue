<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ProductCard from '@/components/product-list/ProductCard.vue'
import { productStore } from '@/stores/productosStore'
import { defineAsyncComponent, onMounted } from 'vue'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const productosStore = productStore()

onMounted(() => {
  productosStore.error = null
  productosStore.fetchProductos()
})
</script>

<template>
  <div v-if="productosStore.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="productosStore.error">{{ productosStore.error }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4">
    <div class="mx-auto grid justify-center sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div v-for="producto in productosStore.productos" :key="producto.id">
        <ProductCard :producto="producto" />
      </div>
    </div>
  </main>
</template>
