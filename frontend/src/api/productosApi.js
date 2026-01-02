import api from './api'

export default {
  getProductos() {
    return api().get('/api/productos/')
  },
  getProductoId(id) {
    return api().get(`/api/productos/${id}`)
  },
  insertarProducto(data) {
    return api().post('/api/productos/', data)
  },
}
