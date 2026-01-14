import api from "./api"

export async function getProductos(){
  const req = await api().get('/api/productos/')

  return req.data.products
}
