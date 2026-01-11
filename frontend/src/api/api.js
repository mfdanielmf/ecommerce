import axios from 'axios'
import { obtenerTokenCSRF } from './csrf'

export default (url = 'http://localhost:8080') => {
  const api = axios.create({
    baseURL: url,
  })

  // Mandamos token csrf si el endpoint tiene jwt_required
  //El token jwt no hace falta (ya se manda por las cookies al tener withCredentials true, pero el csrf no)
  api.interceptors.request.use((config) => {
    const csrfToken = obtenerTokenCSRF()

    if (csrfToken && ['post', 'put', 'delete'].includes(config.method)) {
      config.headers['X-CSRF-TOKEN'] = csrfToken
    }

    return config
  })

  return api
}
