import api from './api'

export default {
  getProductos() {
    return api().get('/api/productos/')
  },
  getProductoId(id) {
    return api().get(`/api/productos/${id}`)
  },
  insertarProducto(data) {
    return api().post('/api/productos/', data, { withCredentials: true })
  },
  eliminarProductoId(id) {
    return api().delete(`/api/productos/${id}`, { withCredentials: true })
  },
  editarProductoId(id, data) {
    return api().put(`/api/productos/${id}`, data, { withCredentials: true })
  },
}
