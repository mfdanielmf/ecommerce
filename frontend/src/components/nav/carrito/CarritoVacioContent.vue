<script setup>
import { ShoppingBagIcon } from 'lucide-vue-next'
</script>

<template>
  <ShoppingBagIcon :size="50" class="flex justify-self-center self-center" />
  <p>Tu carrito está vacío</p>
  <p class="text-neutral-500">¡Añade productos para empezar la compra!</p>
</template>
