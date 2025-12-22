import { defineStore } from 'pinia'
import { ref } from 'vue'
import productosApi from '@/api/productosApi'

export const productStore = defineStore('productos', () => {
  const productos = ref({})
  const error = ref(null)
  const cargando = ref(false)
  const listaCargada = ref(false)

  //TODOS
  async function fetchProductos() {
    if (listaCargada.value) return

    cargando.value = true
    try {
      const productosFetch = await productosApi.getProductos()
      productosFetch.data.products.forEach((p) => {
        productos.value[p.id] = p
      })
      listaCargada.value = true
    } catch {
      error.value = 'Error al obtener la lista de productos'
    } finally {
      cargando.value = false
    }
  }

  //FILTRAR
  function getProductoPorId(id) {
    return productos.value[id]
  }

  async function fetchProductoId(id) {
    if (getProductoPorId(id)) return

    cargando.value = true
    try {
      const productoFetch = await productosApi.getProductoId(id)
      productos.value[productoFetch.data.producto.id] = productoFetch.data.producto
    } catch {
      error.value = `Error al obtener el producto con ID ${id}`
    } finally {
      cargando.value = false
    }
  }

  return { productos, error, cargando, fetchProductos, fetchProductoId, getProductoPorId }
})
