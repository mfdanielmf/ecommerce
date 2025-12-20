<script setup>
import { carritoStore } from '@/stores/carritoStore'
import { PlusIcon, MinusIcon, Trash2 } from 'lucide-vue-next'

const productos = carritoStore().carrito
</script>

<template>
  <div class="p-4 mb-4 tracking-wide border-b border-neutral-300">
    <h1 class="text-xl font-semibold text-blue-700 mb-2">TechStore</h1>
    <p class="text-xs opacity-60">{{ carritoStore().cantidadTotalProductos }} productos</p>
  </div>

  <ul class="list bg-base-100 rounded-box shadow-md overflow-auto">
    <li v-for="producto in productos" :key="producto.id" class="list-row">
      <div
        class="flex items-center justify-center bg-transparent shadow-none cursor-default active:text-black"
      >
        <img class="rounded-box" :src="producto.img_url" width="80" height="80" />
      </div>

      <p class="flex self-center bg-transparent shadow-none cursor-default">
        {{ producto.nombre }}
      </p>

      <div class="flex flex-col bg-transparent shadow-none cursor-default active:text-black">
        <p class="flex self-end">{{ producto.precio * producto.cantidad }}€</p>
        <div class="flex items-center gap-2">
          <p>{{ producto.cantidad }}</p>

          <div class="flex items-center gap-0.5">
            <button class="btn btn-xs btn-circle">
              <MinusIcon :size="13" />
            </button>
            <button class="btn btn-xs btn-circle">
              <PlusIcon :size="13" />
            </button>
          </div>

          <Trash2 :size="20" class="cursor-pointer text-red-500 hover:text-red-700" />
        </div>
      </div>
    </li>
  </ul>
</template>
