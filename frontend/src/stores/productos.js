import { getProductos } from '@/api/productos'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const productStore = defineStore('productos', () => {
  const productos = ref([])
  const error = ref(false)
  const cargando = ref(false)

  async function fetchProductos() {
    if (productos.value.length) return

    cargando.value = true
    try {
      productos.value = await getProductos()
    } catch (e) {
      error.value = e.message
    } finally {
      cargando.value = false
    }
  }

  return { productos, error, fetchProductos, cargando }
})
