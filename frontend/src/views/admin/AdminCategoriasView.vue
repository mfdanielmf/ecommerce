<script setup>
import { useCategoriasStore } from '@/stores/categoriasStore'
import { defineAsyncComponent, onMounted, ref } from 'vue'
import { PlusIcon } from 'lucide-vue-next'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import CategoryTable from '@/components/dashboard/categorias/CategoryTable.vue'

const CategoriaDialog = defineAsyncComponent(
  () => import('@/components/dashboard/categorias/CategoriaDialog.vue'),
)
const ErrorMessage = defineAsyncComponent(() => import('@/components/common/ErrorMessage.vue'))

const categoriasStore = useCategoriasStore()

onMounted(() => {
  categoriasStore.error = null
  categoriasStore.fetchCategorias()
})

const añadirAbierto = ref(false)

async function añadirCategoria(data) {
  const success = await categoriasStore.insertarCategoria(data)

  if (success) {
    añadirAbierto.value = false
  } else {
    añadirAbierto.value = true
  }
}

function abrirConfirmarEliminar() {
  console.log('test')
}

function abrirEditarCategoria() {
  console.log('test')
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
  </div>
</template>
