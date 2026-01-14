import api from "./api"

export async function getProductos(){
  const req = await api().get('/api/productos/')

  return req.data.products
}

export async function eliminarProductoId(id) {
  const req = await api().delete(`/api/productos/${id}`, { withCredentials: true })

  return req.data
}
