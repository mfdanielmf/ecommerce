<script setup>
import { productStore } from '@/stores/productos'
import { onMounted } from 'vue'

const productosStore = productStore()

onMounted(() => {
  productosStore.fetchProductos()
})
</script>

<template>
  <div v-if="productosStore.cargando" class="h-screen grid place-content-center">
    <span class="loading loading-spinner loading-xl text-primary"></span>
  </div>

  <main v-else class="min-h-screen py-20 px-4">
    <div class="mx-auto grid justify-center sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
      <div
        class="card bg-base-100 w-auto shadow-sm"
        v-for="producto in productosStore.productos"
        :key="producto.id"
      >
        <figure>
          <img
            src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            alt="Shoes"
            loading="lazy"
          />
        </figure>
        <div class="card-body">
          <h2 class="card-title">{{ producto.title }}</h2>
          <p class="h-15 overflow-hidden">{{ producto.description }}</p>
          <div class="card-actions justify-between items-center">
            <p class="font-semibold text-xl">{{ producto.price }} €</p>
            <button class="btn btn-primary">Añadir al carrito</button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
