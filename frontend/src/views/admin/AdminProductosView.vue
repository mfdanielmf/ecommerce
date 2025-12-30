<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ProductTable from '@/components/dashboard/ProductTable.vue'
import { productStore } from '@/stores/productosStore'
import { PlusIcon } from 'lucide-vue-next'
import { onMounted } from 'vue'

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

  <div v-else>
    <span>
      <button class="btn btn-primary mb-4">
        <PlusIcon :size="18" />
        Añadir producto
      </button>
    </span>
    <ProductTable :productos="productosStore.productos" />
  </div>
</template>
