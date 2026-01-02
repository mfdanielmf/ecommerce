import { defineStore } from 'pinia'
import { ref } from 'vue'
import productosApi from '@/api/productosApi'
import { toast } from 'vue-sonner'

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
    } catch (e) {
      error.value = e.response?.data?.error || `Error al obtener el producto con ID ${id}`
    } finally {
      cargando.value = false
    }
  }

  //INSERTAR
  async function insertarProducto(data) {
    try {
      const req = await productosApi.insertarProducto(data)

      toast.success(req.data.msg || 'Se ha insertado el producto correctamente')

      productos.value[req.data.producto.id] = req.data.producto

      return true //Éxito (cerrar el diálogo de insertar el producto)
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado')

      return false //Fallo (dejar el diálogo abierto)
    }
  }

  async function eliminarProductoId(id) {
    try {
      const req = await productosApi.eliminarProductoId(id)

      delete productos.value[id]

      toast.success(req.data?.msg)
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado')
    }
  }

  return {
    productos,
    error,
    cargando,
    fetchProductos,
    fetchProductoId,
    getProductoPorId,
    insertarProducto,
    eliminarProductoId,
  }
})
