<script setup>
import { ShoppingCartIcon } from 'lucide-vue-next'
import { carritoStore } from '@/stores/carritoStore'
import QuantitySelectorComponent from './QuantitySelectorComponent.vue'
import { computed, ref } from 'vue'
import { toast } from 'vue-sonner'

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
  if (props.producto.stock === 0) return toast.error('No hay stock disponible para este producto')

  if (
    productoLocalStorage.value &&
    productoLocalStorage.value.cantidad + cantidad.value > props.producto.stock
  )
    return toast.error('¡No puedes añadir tantos productos!', {
      description: `MAX: ${props.producto.stock} En tu carrito: ${productoLocalStorage.value.cantidad}`,
    })

  carritoStore().añadirProducto(props.producto, cantidad.value)
}
</script>

<template>
  <p v-if="producto.descripcion" class="mt-8 border-t border-neutral-200 pt-4 text-neutral-600">
    {{ producto.descripcion }}
  </p>

  <div class="w-62.5 max-w-sm relative mt-4">
    <QuantitySelectorComponent
      :stock="producto.stock"
      v-model="cantidad"
      v-if="producto.stock > 0"
    />

    <button
      class="flex items-center justify-center gap-4 font-semibold w-full btn btn-primary btn-lg"
      :class="{ 'mt-6': producto.stock > 0 }"
      @click="añadirProducto"
      :disabled="props.producto.stock === 0"
    >
      <ShoppingCartIcon v-if="props.producto.stock > 0" />
      <p>{{ props.producto.stock > 0 ? 'Añadir al carrito' : 'Producto agotado' }}</p>
    </button>
  </div>
</template>
