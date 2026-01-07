import { defineStore } from 'pinia'
import { ref } from 'vue'
import categoriasApi from '@/api/categoriasApi'
import { toast } from 'vue-sonner'

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

  async function insertarCategoria(data) {
    try {
      const req = await categoriasApi.insertarCategoria(data)

      toast.success(req.data.msg || 'Se ha insertado la categoría correctamente')

      categorias.value[req.data.categoria.id] = req.data.categoria

      return true //Éxito (cerrar el diálogo de insertar categoría)
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado')

      return false //Fallo (dejar el diálogo abierto)
    }
  }

  async function eliminarCategoria(id) {
    try {
      const req = await categoriasApi.eliminarCategoria(id)

      toast.success(req.data.msg || 'Se ha eliminado la categoría correctamente')

      delete categorias.value[id]
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado')
    }
  }

  return { categorias, cargando, error, fetchCategorias, insertarCategoria, eliminarCategoria }
})
