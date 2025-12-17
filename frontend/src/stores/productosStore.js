import { getProductoId, getProductos } from '@/api/productos'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const productStore = defineStore('productos', () => {
  const productos = ref([])
  const error = ref(null)
  const cargando = ref(false)
  const productoId = ref(null)

  //TODOS
  async function fetchProductos() {
    if (productos.value.length) return

    cargando.value = true
    try {
      const productosFetch = await getProductos()
      productos.value = productosFetch.products
    } catch {
      error.value = 'Error al obtener la lista de productos'
    } finally {
      cargando.value = false
    }
  }

  //FILTRAR
  function filtrarPorId(id) {
    return productos.value.find((productoActual) => productoActual.id === Number(id))
  }

  async function fetchProductoId(id) {
    const productoActual = filtrarPorId(id)

    if (productoActual) {
      productoId.value = productoActual

      return
    }

    cargando.value = true
    try {
      const productoFetch = await getProductoId(id)
      productoId.value = productoFetch.producto
    } catch {
      error.value = `Error al obtener el producto con ID ${id}`
    } finally {
      cargando.value = false
    }
  }

  return { productos, productoId, error, cargando, fetchProductos, fetchProductoId, filtrarPorId }
})
