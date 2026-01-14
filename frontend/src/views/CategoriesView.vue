<script setup>
import CategoryCard from '@/components/category-list/CategoryCard.vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useCategoriasStore } from '@/stores/categoriasStore'
import { defineAsyncComponent, onMounted } from 'vue'

const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const categoriasStore = useCategoriasStore()

onMounted(() => {
  categoriasStore.error = null
  categoriasStore.fetchCategorias()
})
</script>

<template>
  <div v-if="categoriasStore.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="categoriasStore.error">{{ categoriasStore.error }}</ErrorMessage>

  <main class="min-h-screen py-20 px-4" v-else>
    <div
      class="mx-auto grid justify-center grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8"
    >
      <CategoryCard
        :categoria="categoria"
        v-for="categoria of categoriasStore.categorias"
        :key="categoria.id"
      />
    </div>
  </main>
</template>
