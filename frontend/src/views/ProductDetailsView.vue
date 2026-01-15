<script setup>
import { defineAsyncComponent } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ImgComponent from '@/components/product-details/ImgComponent.vue'
import DetailsBodyComponent from '@/components/product-details/DetailsBodyComponent.vue'
import { useGetProductoId } from '@/queries/useProductosQuery'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const props = defineProps({
  id: {
    required: true,
  },
})

const { data, isLoading, error } = useGetProductoId(props.id)
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">{{
    error.response?.data?.error || `Error al obtener el producto con id ${props.id}`
  }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4 grid place-content-center">
    <div v-if="data.producto" class="grid lg:grid-cols-2 gap-12 mb-16">
      <ImgComponent :img_url="data.producto.img_url" :alt="data.producto.nombre" />
      <DetailsBodyComponent :producto="data.producto" />
    </div>
  </main>
</template>
