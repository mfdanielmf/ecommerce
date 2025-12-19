import { useLocalStorage } from '@vueuse/core'
import { defineStore } from 'pinia'

export const carritoStore = defineStore('carrito', () => {
  const carrito = useLocalStorage('carrito', [])

  function encontrarProducto(id) {
    return carrito.value.find((productoActual) => (productoActual.id = id))
  }

  function añadirProducto(producto, cantidad) {
    const productoExistente = encontrarProducto(producto.id)

    if (productoExistente) {
      productoExistente.cantidad++
    } else {
      carrito.value.push({
        id: producto.id,
        nombre: producto.nombre,
        precio: producto.precio,
        cantidad: cantidad,
      })
    }
  }

  return { carrito, encontrarProducto, añadirProducto }
})
