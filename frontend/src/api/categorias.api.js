import api from "./api";

export async function getCategorias() {
  const req = await api().get('/api/categorias/')

  return req.data.categorias
}

export async function insertarCategoria(data) {
  const req = await api().post('/api/categorias/', data, { withCredentials: true })

  return req.data
}
