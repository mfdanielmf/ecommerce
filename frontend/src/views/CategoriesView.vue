<script setup>
import CategoryCard from '@/components/category-list/CategoryCard.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useGetCategorias } from '@/queries/useCategoriasQuery'
import { defineAsyncComponent} from 'vue'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const {data, isLoading, error} = useGetCategorias()
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">{{ error.response?.data?.error || "Error al obtener las categorías" }}</ErrorMessage>

  <main class="min-h-screen py-20 px-4" v-else>
    <div
      class="mx-auto grid justify-center grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8"
    >
      <CategoryCard
        v-for="categoria of data"
        :key="categoria.id"
        :categoria="categoria"
      />
    </div>
  </main>
</template>
