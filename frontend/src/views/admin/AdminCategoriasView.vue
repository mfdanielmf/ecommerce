<script setup>
import { useCategoriasStore } from '@/stores/categoriasStore'
import { defineAsyncComponent, onMounted, ref } from 'vue'
import { PlusIcon } from 'lucide-vue-next'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'

const CategoriaDialog = defineAsyncComponent(
  () => import('@/components/dashboard/categorias/CategoriaDialog.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))
const ConfirmDialog = defineAsyncComponent(() => import('@/components/dashboard/ConfirmDialog.vue'))
const CategoryTable = defineAsyncComponent(
  () => import('@/components/dashboard/categorias/CategoryTable.vue'),
)

const categoriasStore = useCategoriasStore()

onMounted(() => {
  categoriasStore.error = null
  categoriasStore.fetchCategorias()
})

const añadirAbierto = ref(false)
const eliminarAbierto = ref(false)
const editarAbierto = ref(false)
const categoriaEliminar = ref(null)
const eliminando = ref(false)
const categoriaEditar = ref(null)

async function añadirCategoria(data) {
  const success = await categoriasStore.insertarCategoria(data)

  if (success) {
    añadirAbierto.value = false
  } else {
    añadirAbierto.value = true
  }
}

function abrirConfirmarEliminar(categoria) {
  if (!categoria) return

  categoriaEliminar.value = categoria
  eliminarAbierto.value = true
}

async function eliminarCategoria() {
  if (!categoriaEliminar.value) return

  eliminando.value = true

  await categoriasStore.eliminarCategoria(categoriaEliminar.value.id)

  eliminando.value = false
  eliminarAbierto.value = false
}

function abrirEditarCategoria(categoria) {
  if (!categoria) return

  categoriaEditar.value = categoria
  editarAbierto.value = true
}

async function editarCategoria(data) {
  const success = await categoriasStore.editarCategoria(categoriaEditar.value.id, data)

  if (success) editarAbierto.value = false
  else editarAbierto.value = true
}
</script>

<template>
  <div v-if="categoriasStore.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="categoriasStore.error">
    {{ categoriasStore.error }}
  </ErrorMessage>

  <div v-else>
    <span>
      <button class="btn btn-primary mb-4" @click="añadirAbierto = true">
        <PlusIcon :size="18" />
        Añadir categoría
      </button>
    </span>

    <CategoryTable
      v-if="Object.keys(categoriasStore.categorias).length > 0"
      :categorias="categoriasStore.categorias"
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
      :eliminando="eliminando"
    >
      ¿Seguro que quieres eliminar la categoría {{ categoriaEliminar.nombre }}?
    </ConfirmDialog>
  </div>
</template>
