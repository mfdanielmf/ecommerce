<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useDeleteProducto, useGetProductos } from '@/queries/useProductosQuery'
import { useCategoriasStore } from '@/stores/categoriasStore'
import { productStore } from '@/stores/productosStore'
import { PlusIcon } from 'lucide-vue-next'
import { computed, defineAsyncComponent, onMounted, ref } from 'vue'

const ProductoDialog = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductoDialog.vue'),
)
const ProductTable = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductTable.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ConfirmDialog = defineAsyncComponent(() => import('@/components/dashboard/ConfirmDialog.vue'))

const productosStore = productStore()
const categoriasStore = useCategoriasStore()

const cargandoDatos = ref(true)

const añadirAbierto = ref(false)
const eliminarAbierto = ref(false)
const editarAbierto = ref(false)
const productoEliminar = ref(null)
const productoEditar = ref(null)

const {data: dataProductos, isLoading: loadingProductos, error: errorProductos} = useGetProductos()
const {isPending: loadingEliminar, mutateAsync: mutateEliminar} = useDeleteProducto()

const productosConCategoria = computed(() => {
  if (!dataProductos) return []

  return dataProductos.value.map(producto => ({
    ...producto,
    categoria: categoriasStore.categorias[producto.id_categoria]
  }))
})

onMounted(async () => {
  categoriasStore.error = null

  await categoriasStore.fetchCategorias()

  cargandoDatos.value = false
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

  await mutateEliminar(productoEliminar.value.id)

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
  <div v-if="loadingProductos" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="errorProductos || categoriasStore.error">
    {{ error.response?.data?.error || "Ha ocurrido un error al cargar los datos" }}
  </ErrorMessage>

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
      :productos="productosConCategoria"
      v-if="dataProductos"
      @abrir-confirmar-eliminar="abrirConfirmarEliminar"
      @abrir-editar-producto="abrirEditarProducto"
    />

    <ConfirmDialog
      v-model:open="eliminarAbierto"
      v-if="eliminarAbierto"
      @confirmar-eliminar="eliminarProducto"
      :eliminando="loadingEliminar"
    >
      ¿Seguro que quieres eliminar el producto {{ productoEliminar.nombre }}?
    </ConfirmDialog>
  </div>
</template>
