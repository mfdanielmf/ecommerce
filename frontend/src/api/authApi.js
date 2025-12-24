import api from './api'

export default {
  registrarUsuario(data) {
    return api().post('/auth/register', data)
  },
  iniciarSesion(data) {
    return api().post('/auth/login', data, { withCredentials: true })
  },
  obtenerUsuario() {
    return api().get('/auth/me', { withCredentials: true })
  },
}
