import api from './api'

export default {
  getCategorias() {
    return api().get('/api/categorias/')
  },
  insertarCategoria(data) {
    return api().post('/api/categorias/', data, { withCredentials: true })
  },
  eliminarCategoria(id) {
    return api().delete(`/api/categorias/${id}`, { withCredentials: true })
  },
  editarCategoria(id, data) {
    return api().put(`/api/categorias/${id}`, data, { withCredentials: true })
  },
}
