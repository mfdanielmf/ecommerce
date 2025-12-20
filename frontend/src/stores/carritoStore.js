import { useLocalStorage } from '@vueuse/core'
import { defineStore } from 'pinia'
import { computed } from 'vue'
import { toast } from 'vue-sonner'

const IMG_URL = 'https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp'

export const carritoStore = defineStore('carrito', () => {
  const carrito = useLocalStorage('carrito_techstore', [])

  function encontrarProducto(id) {
    return carrito.value.find((productoActual) => productoActual.id === id)
  }

  function añadirProducto(producto, cantidad, foto = IMG_URL) {
    const productoExistente = encontrarProducto(producto.id)

    if (productoExistente) {
      productoExistente.cantidad += cantidad
    } else {
      carrito.value.push({
        id: producto.id,
        nombre: producto.nombre,
        precio: producto.precio,
        cantidad: cantidad,
        img_url: foto,
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
