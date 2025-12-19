<script setup>
import { ShoppingCartIcon } from 'lucide-vue-next'
import { carritoStore } from '@/stores/carritoStore'
import CarritoVacíoContent from './CarritoVacioContent.vue'

const carrito = carritoStore().carrito
</script>

<template>
  <div class="drawer drawer-end flex items-center justify-end">
    <input id="my-drawer-5" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex items-center">
      <!-- Page content here -->
      <label for="my-drawer-5" class="indicator drawer-button cursor-pointer">
        <ShoppingCartIcon :size="20" />
        <span class="badge badge-sm rounded-full indicator-item">{{ carrito.length }}</span>
      </label>
    </div>
    <div class="drawer-side">
      <label for="my-drawer-5" aria-label="close sidebar" class="drawer-overlay"></label>
      <div
        v-if="!carrito.length"
        class="menu bg-base-200 min-h-full w-xl p-4 grid place-content-center text-center"
      >
        <CarritoVacíoContent />
      </div>

      <div
        v-else
        class="menu bg-base-200 min-h-full w-xl p-4 grid place-content-center text-center"
      >
        <h1>test</h1>
      </div>
    </div>
  </div>
</template>
