<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useGetProductosCategoria } from '@/queries/useCategoriasQuery'
import { defineAsyncComponent } from 'vue'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ProductCard = defineAsyncComponent(() => import('@/components/product-list/ProductCard.vue'))

const props = defineProps({
  id: {
    required: true,
  },
})

const { data, error, isLoading } = useGetProductosCategoria(props.id)
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">
    {{ error.response?.data?.error || 'Error al obtener los productos de la categoría' }}
  </ErrorMessage>

  <main v-else-if="data.productos.length > 0" class="min-h-screen py-20 px-4">
    <div class="mx-auto grid justify-center sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div v-for="producto of data.productos" :key="producto.id">
        <ProductCard :producto="producto" v-if="producto" />
      </div>
    </div>
  </main>

  <ErrorMessage v-else> Parece que no hay productos para esta categoría... </ErrorMessage>
</template>
