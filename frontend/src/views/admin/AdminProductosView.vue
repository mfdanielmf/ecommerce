<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { productStore } from '@/stores/productosStore'
import { PlusIcon } from 'lucide-vue-next'
import { defineAsyncComponent, onMounted, ref } from 'vue'

const ProductoDialog = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductoDialog.vue'),
)
const ProductTable = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductTable.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ConfirmDialog = defineAsyncComponent(() => import('@/components/dashboard/ConfirmDialog.vue'))

const productosStore = productStore()

const añadirAbierto = ref(false)
const eliminarAbierto = ref(false)
const productoEliminar = ref(null)
const eliminando = ref(false)

onMounted(() => {
  productosStore.error = null
  productosStore.fetchProductos()
})

function abrirConfirmarEliminar(producto) {
  if (!producto) return

  productoEliminar.value = producto
  eliminarAbierto.value = true
}

async function eliminarProducto() {
  if (!productoEliminar.value) return

  eliminando.value = true

  await productosStore.eliminarProductoId(productoEliminar.value.id)

  eliminando.value = false
  eliminarAbierto.value = false
}
</script>

<template>
  <div v-if="productosStore.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="productosStore.error">{{ productosStore.error }}</ErrorMessage>

  <div v-else>
    <span>
      <button class="btn btn-primary mb-4" @click="añadirAbierto = true">
        <PlusIcon :size="18" />
        Añadir producto
      </button>
    </span>

    <ProductoDialog v-model:open="añadirAbierto" v-if="añadirAbierto" />

    <ProductTable
      :productos="productosStore.productos"
      v-if="Object.keys(productosStore.productos).length > 0"
      @abrir-confirmar-eliminar="abrirConfirmarEliminar"
    />

    <ConfirmDialog
      v-model:open="eliminarAbierto"
      v-if="eliminarAbierto"
      @confirmar-eliminar="eliminarProducto"
      :eliminando="eliminando"
    >
      ¿Seguro que quieres eliminar el producto {{ productoEliminar.nombre }}?
    </ConfirmDialog>
  </div>
</template>
