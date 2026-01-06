<script setup>
import { PencilIcon, Trash2Icon } from 'lucide-vue-next'

const props = defineProps({
  categorias: {
    required: true,
  },
})

const emit = defineEmits(['abrirConfirmarEliminar', 'abrirEditarCategoria'])
</script>

<template>
  <div class="overflow-x-auto rounded-box border border-base-content/10 bg-base-100 rounded-md">
    <table class="table">
      <!-- head -->
      <thead>
        <tr>
          <th></th>
          <th>Nombre</th>
          <th>Descripcion</th>
          <th>Fecha creación</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="categoria in props.categorias" :key="categoria.id">
          <th>{{ categoria.id }}</th>
          <td>{{ categoria.nombre }}</td>
          <td>{{ categoria.descripcion }}</td>
          <td>{{ categoria.fecha_creacion }}</td>
          <td class="flex gap-2" id="btn-container">
            <button class="btn btn-soft btn-info" @click="emit('abrirEditarCategoria', categoria)">
              <PencilIcon :size="18" />
              Editar
            </button>

            <button
              class="btn btn-error"
              @click="
                emit('abrirConfirmarEliminar', { id: categoria.id, nombre: categoria.nombre })
              "
            >
              <Trash2Icon :size="18" />
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
@media (max-width: 900px) {
  #btn-container {
    flex-wrap: wrap;
  }

  button {
    width: 100%;
  }
}
</style>
