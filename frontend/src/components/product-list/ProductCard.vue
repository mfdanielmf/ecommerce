<script setup>
defineProps({
  producto:{
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="card bg-base-100 w-auto shadow-sm">
    <figure>
      <img
        :src="producto.img_url"
        :alt="producto.nombre"
        loading="lazy"
      />
    </figure>

    <div class="card-body">
      <h2 class="card-title">{{ producto.nombre }}</h2>
      <p class="h-15 overflow-hidden">{{ producto.descripcion }}</p>
      <div class="card-actions justify-between items-center">
        <p class="font-semibold text-xl">{{ producto.precio }} €</p>
        <button class="btn btn-primary">Añadir al carrito</button>
      </div>
    </div>
  </div>
</template>
