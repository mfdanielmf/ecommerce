<script setup>
import { defineAsyncComponent, ref } from 'vue'
import { PlusIcon } from 'lucide-vue-next'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import {
  useDeleteCategoria,
  useEditarCategoria,
  useGetCategorias,
  useInsertarCategoria,
} from '@/queries/useCategoriasQuery'

const CategoriaDialog = defineAsyncComponent(
  () => import('@/components/dashboard/categorias/CategoriaDialog.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ConfirmDialog = defineAsyncComponent(() => import('@/components/dashboard/ConfirmDialog.vue'))
const CategoryTable = defineAsyncComponent(
  () => import('@/components/dashboard/categorias/CategoryTable.vue'),
)

const añadirAbierto = ref(false)
const eliminarAbierto = ref(false)
const editarAbierto = ref(false)
const categoriaEliminar = ref(null)
const categoriaEditar = ref(null)

const { data: categorias, isLoading, error } = useGetCategorias()
const { isSuccess: successInsertar, mutateAsync: mutateInsertar } = useInsertarCategoria()
const { mutateAsync: mutateEliminar, isPending: pendingEliminar } = useDeleteCategoria()
const { isSuccess: successEditar, mutateAsync: mutateEditar } = useEditarCategoria()

async function añadirCategoria(data) {
  try {
    await mutateInsertar(data)
  } catch (e) {
    console.error(e.message)
  }

  if (successInsertar.value) {
    añadirAbierto.value = false
  }
}

function abrirConfirmarEliminar(categoria) {
  if (!categoria) return

  categoriaEliminar.value = categoria
  eliminarAbierto.value = true
}

async function eliminarCategoria() {
  if (!categoriaEliminar.value) return

  try {
    await mutateEliminar(categoriaEliminar.value.id)
  } catch (e) {
    console.error(e.message)
  }

  eliminarAbierto.value = false
}

function abrirEditarCategoria(categoria) {
  if (!categoria) return

  categoriaEditar.value = categoria
  editarAbierto.value = true
}

async function editarCategoria(data) {
  if (!data) return

  try {
    await mutateEditar({ id: categoriaEditar.value.id, data })
  } catch (e) {
    console.error(e.message)
  }

  if (successEditar.value) editarAbierto.value = false
}
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">
    {{ error.response?.data?.error || 'Error al cargar la lista de categorías' }}
  </ErrorMessage>

  <div v-else>
    <span>
      <button class="btn btn-primary mb-4" @click="añadirAbierto = true">
        <PlusIcon :size="18" />
        Añadir categoría
      </button>
    </span>

    <CategoryTable
      v-if="categorias"
      :categorias="categorias"
      @abrir-confirmar-eliminar="abrirConfirmarEliminar"
      @abrir-editar-categoria="abrirEditarCategoria"
    />

    <!-- Añadir dialog -->
    <CategoriaDialog
      v-model:open="añadirAbierto"
      v-if="añadirAbierto"
      :funcion="añadirCategoria"
      texto-boton="Añadir Categoría"
    />

    <!-- Editar dialog -->
    <CategoriaDialog
      v-model:open="editarAbierto"
      v-if="editarAbierto"
      :funcion="editarCategoria"
      texto-boton="Editar Categoría"
      :categoria="categoriaEditar"
    >
      <template #titulo>Editar una categoría</template>
      <template #descripcion>Modifica los campos de la categoría</template>
    </CategoriaDialog>

    <!-- Para eliminar -->
    <ConfirmDialog
      v-model:open="eliminarAbierto"
      v-if="eliminarAbierto"
      @confirmar-eliminar="eliminarCategoria"
      :eliminando="pendingEliminar"
    >
      ¿Seguro que quieres eliminar la categoría {{ categoriaEliminar.nombre }}?
    </ConfirmDialog>
  </div>
</template>
