import api from './api'

export default {
  registrarUsuario(data) {
    return api().post('/auth/register', data)
  },
}
