import { useLocalStorage } from '@vueuse/core'
import { defineStore } from 'pinia'
import { computed } from 'vue'
import { toast } from 'vue-sonner'

export const carritoStore = defineStore('carrito', () => {
  const carrito = useLocalStorage('carrito_techstore', [])

  function encontrarProducto(id) {
    return carrito.value.find((productoActual) => productoActual.id === id)
  }

  function añadirProducto(producto, cantidad) {
    const productoExistente = encontrarProducto(producto.id)

    if (productoExistente) {
      productoExistente.cantidad += cantidad
    } else {
      carrito.value.push({
        id: producto.id,
        nombre: producto.nombre,
        precio: producto.precio,
        cantidad: cantidad,
      })
    }

    toast.success(`¡Se ha añadido el producto ${producto.nombre} al carrito!`)
  }

  const cantidadTotalProductos = computed(() => {
    if (carrito.value.length) {
      return carrito.value.reduce((total, productoActual) => total + productoActual.cantidad, 0)
    }

    return 0
  })

  return { carrito, encontrarProducto, añadirProducto, cantidadTotalProductos }
})
