<script setup>
import VaciarCarritoDialog from '@/components/nav/carrito/VaciarCarritoDialog.vue'
import { carritoStore } from '@/stores/carritoStore'
import { PlusIcon, MinusIcon, Trash2 } from 'lucide-vue-next'
import { toast } from 'vue-sonner'

const store = carritoStore()

function eliminarProducto(id) {
  store.eliminarProductoCarrito(id)
}

function restarCantidad(producto) {
  if (!producto.cantidad || producto.cantidad - 1 < 1) return

  producto.cantidad--
}

function sumarCantidad(producto) {
  if (!producto.cantidad || producto.cantidad + 1 > producto.stock)
    return toast.error('¡No queda tanto stock!')

  producto.cantidad++
}

function vaciarCarrito() {
  store.carrito = []
  toast.info('Has vaciado el carrito', { position: 'top-center' })
}
</script>

<template>
  <div class="p-4 mb-4 tracking-wide border-b border-neutral-300">
    <h1 class="text-xl font-semibold text-blue-700 mb-2">TechStore</h1>
    <div class="flex justify-between items-center">
      <p class="text-xs opacity-60">{{ store.cantidadTotalProductos }} productos</p>
      <p>Precio total: {{ store.precioTotalCarrito }}</p>
    </div>
  </div>

  <ul class="list bg-base-100 rounded-box shadow-md overflow-auto">
    <li v-for="producto in store.carrito" :key="producto.id" class="list-row">
      <div
        class="flex items-center justify-center bg-transparent shadow-none cursor-default active:text-black"
      >
        <img class="rounded-box" :src="producto.img_url" width="80" height="80" />
      </div>

      <p class="flex self-center bg-transparent shadow-none cursor-default">
        {{ producto.nombre }}
      </p>

      <div class="flex flex-col bg-transparent shadow-none cursor-default active:text-black">
        <p class="flex self-end">
          {{
            (producto.precio * producto.cantidad).toLocaleString('es', {
              style: 'currency',
              currency: 'EUR',
            })
          }}
        </p>
        <div class="flex items-center gap-2">
          <p>{{ producto.cantidad }}</p>

          <div class="flex items-center gap-0.5">
            <button class="btn btn-xs btn-circle" @click="restarCantidad(producto)">
              <MinusIcon :size="13" />
            </button>
            <button class="btn btn-xs btn-circle" @click="sumarCantidad(producto)">
              <PlusIcon :size="13" />
            </button>
          </div>

          <Trash2
            :size="20"
            class="btn btn-ghost btn-xs btn-circle cursor-pointer text-red-500 hover:text-red-700"
            @click="eliminarProducto(producto.id)"
          />
        </div>
      </div>
    </li>
  </ul>

  <div class="mt-5 flex flex-col gap-2">
    <button class="btn btn-primary">Finalizar Compra</button>
    <VaciarCarritoDialog @vaciar-carrito="vaciarCarrito" />
  </div>
</template>
