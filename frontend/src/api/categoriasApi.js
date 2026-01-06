import api from './api'

export default {
  getCategorias() {
    return api().get('/api/categorias/')
  },
  insertarCategoria(data) {
    return api().post('/api/categorias/', data)
  },
}
