<script setup>
defineProps({
  categoria: {
    required: true,
    type: Object,
  },
})
</script>

<template>
  <RouterLink
    :to="{ name: 'detalles_categoria', params: { id: categoria.id } }"
    class="card bg-white w-full shadow-sm"
  >
    <div class="card-body">
      <h2 class="card-title">{{ categoria.nombre }}</h2>
      <p>{{ categoria.descripcion }}</p>
    </div>
  </RouterLink>
</template>
