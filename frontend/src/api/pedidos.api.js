import api from "./api";

export async function hacerPedido(data) {
  const req = await api().post("/api/pedidos", data, { withCredentials: true })

  return req.data
}
