<script setup>
import { ShoppingCartIcon, XIcon } from 'lucide-vue-next'
import { carritoStore } from '@/stores/carritoStore'
import { defineAsyncComponent, ref } from 'vue'

const CarritoVacioContent = defineAsyncComponent(() => import('./CarritoVacioContent.vue'))
const CarritoContentComponent = defineAsyncComponent(() => import('./CarritoContentComponent.vue'))

const almacenCarrito = carritoStore()

const drawerAbierto = ref(false)
</script>

<template>
  <div class="drawer drawer-end flex items-center justify-end">
    <input id="my-drawer-5" type="checkbox" class="drawer-toggle" v-model="drawerAbierto" />
    <div class="drawer-content flex items-center">
      <!-- Page content here -->
      <label for="my-drawer-5" class="indicator drawer-button cursor-pointer">
        <ShoppingCartIcon :size="20" />
        <span class="badge badge-sm rounded-full indicator-item">{{
          almacenCarrito.cantidadTotalProductos
        }}</span>
      </label>
    </div>
    <div class="drawer-side">
      <label
        for="my-drawer-5"
        aria-label="close sidebar"
        class="drawer-overlay cursor-default"
      ></label>

      <div
        class="menu bg-base-200 min-h-full w-xl"
        :class="{ 'grid place-content-center text-center': !almacenCarrito.carrito.length }"
      >
        <template v-if="drawerAbierto">
          <label for="my-drawer-5" class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4">
            <XIcon />
          </label>

          <CarritoVacioContent v-if="!almacenCarrito.carrito.length" />
          <CarritoContentComponent v-else />
        </template>
      </div>
    </div>
  </div>
</template>
