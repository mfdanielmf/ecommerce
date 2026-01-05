import api from './api'

export default {
  getCategorias() {
    return api().get('/api/categorias/')
  },
}
