import { defineStore } from 'pinia'
import { ref } from 'vue'
import categoriasApi from '@/api/categoriasApi'

export const useCategoriasStore = defineStore('categorias', () => {
  const categorias = ref({})
  const cargando = ref(false)
  const error = ref(null)

  //OBTENER TODAS LAS CATEGORÍAS
  async function fetchCategorias() {
    if (Object.keys(categorias.value).length > 0) return

    cargando.value = true
    try {
      const req = await categoriasApi.getCategorias()

      req.data.categorias.forEach((c) => {
        categorias.value[c.id] = c
      })
    } catch {
      error.value = 'Error al obtener la lista de categorías'
    } finally {
      cargando.value = false
    }
  }

  return { categorias, cargando, error, fetchCategorias }
})
