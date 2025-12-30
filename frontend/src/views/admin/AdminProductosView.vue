<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ProductoDialog from '@/components/dashboard/productos/ProductoDialog.vue'
import ProductTable from '@/components/dashboard/productos/ProductTable.vue'
import { productStore } from '@/stores/productosStore'
import { PlusIcon } from 'lucide-vue-next'
import { onMounted, ref } from 'vue'

const productosStore = productStore()

const añadirAbierto = ref(false)

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
      <button class="btn btn-primary mb-4" @click="añadirAbierto = true">
        <PlusIcon :size="18" />
        Añadir producto
      </button>
    </span>

    <ProductoDialog v-model:open="añadirAbierto" />

    <ProductTable :productos="productosStore.productos" />
  </div>
</template>
