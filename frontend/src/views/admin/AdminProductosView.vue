<script setup>
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { useGetCategorias } from '@/queries/useCategoriasQuery'
import {
  useDeleteProducto,
  useEditarProducto,
  useGetProductos,
  useInsertarProducto,
} from '@/queries/useProductosQuery'
import { PlusIcon } from 'lucide-vue-next'
import { computed, defineAsyncComponent, ref } from 'vue'

const ProductoDialog = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductoDialog.vue'),
)
const ProductTable = defineAsyncComponent(
  () => import('@/components/dashboard/productos/ProductTable.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ConfirmDialog = defineAsyncComponent(() => import('@/components/dashboard/ConfirmDialog.vue'))

const añadirAbierto = ref(false)
const eliminarAbierto = ref(false)
const editarAbierto = ref(false)
const productoEliminar = ref(null)
const productoEditar = ref(null)

const {
  data: dataProductos,
  isLoading: loadingProductos,
  error: errorProductos,
} = useGetProductos()
const {
  data: dataCategorias,
  isLoading: loadingCategorias,
  error: errorCategorias,
} = useGetCategorias()
const { isPending: loadingEliminar, mutateAsync: mutateEliminar } = useDeleteProducto()
const { isSuccess: successAñadir, mutateAsync: mutateAñadir } = useInsertarProducto()
const { isSuccess: successEditar, mutateAsync: mutateEditar } = useEditarProducto()

const cargando = computed(() => {
  if (loadingCategorias.value || loadingProductos.value) {
    return true
  } else {
    return false
  }
})

const productosConCategoria = computed(() => {
  if (!dataProductos.value || !dataCategorias.value) return []

  return dataProductos.value.map((producto) => ({
    ...producto,
    categoria: dataCategorias.value.find((categoria) => categoria.id === producto.id_categoria),
  }))
})

async function añadirProducto(datos) {
  if (!datos) return

  try {
    await mutateAñadir(datos)
  } catch (e) {
    console.error(e.message)
  }

  if (successAñadir.value) {
    añadirAbierto.value = false
  }
}

function abrirConfirmarEliminar(producto) {
  if (!producto) return

  productoEliminar.value = producto
  eliminarAbierto.value = true
}

async function eliminarProducto() {
  if (!productoEliminar.value) return

  try {
    await mutateEliminar(productoEliminar.value.id)
  } catch (e) {
    console.error(e.message)
  }

  eliminarAbierto.value = false
}

function abrirEditarProducto(producto) {
  if (!producto) return

  productoEditar.value = producto

  editarAbierto.value = true
}

async function editarProducto(data) {
  if (!productoEditar.value) return

  try {
    await mutateEditar({ id: productoEditar.value.id, data, id_categoria: productoEditar.value.id_categoria})
  } catch (e) {
    console.error(e.message)
  }

  if (successEditar.value) {
    editarAbierto.value = false
  }
}
</script>

<template>
  <div v-if="cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="errorProductos || errorCategorias">
    {{
      errorProductos.response?.data?.error ||
      errorCategorias.response?.data?.error ||
      'Ha ocurrido un error al cargar los datos'
    }}
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
      :categorias="dataCategorias"
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
      :categorias="dataCategorias"
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
