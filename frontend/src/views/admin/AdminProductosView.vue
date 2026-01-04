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
const editarAbierto = ref(false)
const productoEliminar = ref(null)
const eliminando = ref(false)
const productoEditar = ref(null)

onMounted(() => {
  productosStore.error = null
  productosStore.fetchProductos()
})

async function añadirProducto(data) {
  const success = await productosStore.insertarProducto(data)

  if (success) {
    añadirAbierto.value = false
  } else {
    añadirAbierto.value = true
  }
}

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

function abrirEditarProducto(producto) {
  if (!producto) return

  productoEditar.value = producto
  editarAbierto.value = true
}

async function editarProducto(data) {
  const success = await productosStore.editarProducto(productoEditar.value.id, data)

  if (success) {
    editarAbierto.value = false
  } else {
    editarAbierto.value = true
  }
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

    <!-- Añadir dialog -->
    <ProductoDialog
      v-model:open="añadirAbierto"
      v-if="añadirAbierto"
      :funcion="añadirProducto"
      texto-boton="Añadir Producto"
    >
      <template #titulo>Crear un nuevo producto</template>
      <template #descripcion>Introduce los datos del producto</template>
    </ProductoDialog>

    <!-- Editar dialog -->
    <ProductoDialog
      v-model:open="editarAbierto"
      v-if="editarAbierto"
      :funcion="editarProducto"
      texto-boton="Editar Producto"
      :producto="productoEditar"
    >
      <template #titulo>Editar un producto</template>
      <template #descripcion>Modifica los campos del producto</template>
    </ProductoDialog>

    <ProductTable
      :productos="productosStore.productos"
      v-if="Object.keys(productosStore.productos).length > 0"
      @abrir-confirmar-eliminar="abrirConfirmarEliminar"
      @abrir-editar-producto="abrirEditarProducto"
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
