<script setup>
import { PencilIcon, Trash2Icon } from 'lucide-vue-next'

const props = defineProps({
  productos: {
    required: true,
  },
})
</script>

<template>
  <div class="overflow-x-auto rounded-box border border-base-content/10 bg-base-100 rounded-md">
    <table class="table">
      <!-- head -->
      <thead>
        <tr>
          <th></th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Fecha creación</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <!-- row 1 -->
        <tr v-for="producto in props.productos" :key="producto.id">
          <th>{{ producto.id }}</th>
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.precio }} €</td>
          <td>{{ producto.stock }}</td>
          <td>{{ producto.fecha_creacion }}</td>
          <td class="flex gap-2" id="btn-container">
            <button class="btn btn-soft btn-info">
              <PencilIcon :size="18" />
              Editar
            </button>
            <button class="btn btn-error">
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
