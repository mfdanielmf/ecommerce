import { getProductos } from '@/api/productos'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const productStore = defineStore('productos', () => {
  const productos = ref([])
  const error = ref(null)
  const cargando = ref(false)

  async function fetchProductos() {
    if (productos.value.length) return

    cargando.value = true
    try {
      const productosFetch = await getProductos()
      productos.value = productosFetch.products
    } catch (e) {
      error.value = e.message
    } finally {
      cargando.value = false
    }
  }

  return { productos, error, fetchProductos, cargando }
})
