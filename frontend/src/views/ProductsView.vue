<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ProductCard from '@/components/product-list/ProductCard.vue'
import { useGetProductos } from '@/queries/useProductosQuery'

import { defineAsyncComponent} from 'vue'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const {data, error, isLoading} = useGetProductos()
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">Error al obtener la lista de productos</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4">
    <div class="mx-auto grid justify-center sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div v-for="producto of data" :key="producto.id">
        <ProductCard :producto="producto" />
      </div>
    </div>
  </main>
</template>
