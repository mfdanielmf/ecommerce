<script setup>
import { ShoppingCartIcon } from 'lucide-vue-next'
import QuantitySelectorComponent from './QuantitySelectorComponent.vue'
import { carritoStore } from '@/stores/carritoStore'
import { computed, ref } from 'vue'

const props = defineProps({
  producto: {
    type: Object,
    required: true,
  },
})

const cantidad = ref(1)

const productoLocalStorage = computed(() => {
  return carritoStore().encontrarProducto(props.producto.id)
})

const añadirProducto = () => {
  if (
    productoLocalStorage.value &&
    productoLocalStorage.value.cantidad + cantidad.value > props.producto.stock
  )
    return

  carritoStore().añadirProducto(props.producto, cantidad.value)
}
</script>

<template>
  <p v-if="producto.descripcion" class="mt-8 border-t border-neutral-200 pt-4 text-neutral-600">
    {{ producto.descripcion }}
  </p>

  <div class="w-62.5 max-w-sm relative mt-4">
    <QuantitySelectorComponent :stock="producto.stock" v-model="cantidad" />

    <button
      class="flex items-center justify-center gap-4 mt-6 font-semibold w-full btn btn-primary btn-lg"
      @click="añadirProducto"
    >
      <ShoppingCartIcon />
      <p>Añadir al carrito</p>
    </button>
  </div>
</template>
