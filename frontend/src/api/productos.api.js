import api from './api'

export async function getProductos() {
  const req = await api().get('/api/productos/')

  return req.data.products
}

export async function añadirProducto(data) {
  const req = await api().post('/api/productos/', data, { withCredentials: true })

  return req.data
}

export async function editarProducto(id, data) {
  const req = await api().put(`/api/productos/${id}`, data, { withCredentials: true })

  return req.data
}

export async function eliminarProductoId(id) {
  const req = await api().delete(`/api/productos/${id}`, { withCredentials: true })

  return req.data
}
