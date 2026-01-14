<script setup>
import { useCategoriasStore } from '@/stores/categoriasStore'
import { onMounted } from 'vue'

const props = defineProps({
  id: {
    required: true,
  },
})

const categoriasStore = useCategoriasStore()

onMounted(() => {
  categoriasStore.error = null
  categoriasStore.fetchCategoriaId(props.id)
})
</script>

<template>
  <h1>Detalles</h1>
</template>
