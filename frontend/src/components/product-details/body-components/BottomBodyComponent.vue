<script setup>
import { ShoppingCartIcon } from 'lucide-vue-next'
import QuantitySelectorComponent from './QuantitySelectorComponent.vue'

defineProps({
  descripcion: {
    type: String,
    required: false,
  },
  stock: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <p v-if="descripcion" class="mt-8 border-t border-neutral-200 pt-4 text-neutral-600">
    {{ descripcion }}
  </p>

  <div class="w-62.5 max-w-sm relative mt-4">
    <QuantitySelectorComponent :stock="stock" />

    <button
      class="flex items-center justify-center gap-4 mt-6 font-semibold w-full btn btn-primary btn-lg"
    >
      <ShoppingCartIcon />
      <p>Añadir al carrito</p>
    </button>
  </div>
</template>
