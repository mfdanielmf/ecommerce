import api from "./api";

export async function getCategorias() {
  const req = await api().get('/api/categorias/')

  return req.data.categorias
}
