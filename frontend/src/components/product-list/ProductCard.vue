<script setup>
import { carritoStore } from '@/stores/carritoStore'
import { computed } from 'vue'
import { toast } from 'vue-sonner'

const props = defineProps({
  producto: {
    type: Object,
    required: true,
  },
})

const productoLocalStorage = computed(() => {
  return carritoStore().encontrarProducto(props.producto.id)
})

const añadirProductoCarrito = () => {
  if (props.producto.stock === 0) return toast.error('No hay stock disponible para este producto')

  if (
    productoLocalStorage.value &&
    productoLocalStorage.value.cantidad + 1 > productoLocalStorage.value.stock
  )
    return toast.error('¡No puedes añadir tantos productos!', {
      description: `MAX: ${productoLocalStorage.value.stock} En tu carrito: ${productoLocalStorage.value.cantidad}`,
    })

  carritoStore().añadirProducto(props.producto, 1)
}
</script>

<template>
  <RouterLink
    :to="{ name: 'detalles_producto', params: { id: producto.id } }"
    class="card bg-base-100 w-auto shadow-sm"
  >
    <figure>
      <img :src="producto.img_url" :alt="producto.nombre" loading="lazy" />
    </figure>

    <div class="card-body">
      <h2 class="card-title">{{ producto.nombre }}</h2>
      <p class="h-15 overflow-hidden">{{ producto.descripcion }}</p>
      <div class="card-actions justify-between items-center">
        <p class="font-semibold text-xl">{{ producto.precio }} €</p>
        <button class="btn btn-primary" @click.stop.prevent="añadirProductoCarrito">
          Añadir al carrito
        </button>
      </div>
    </div>
  </RouterLink>
</template>
