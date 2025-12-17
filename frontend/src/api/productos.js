import axios from 'axios'

export async function getProductos() {
  try {
    const req = await axios.get('http://127.0.0.1:8080/api/productos/')

    return req.data
  } catch (e) {
    console.error('ERROR:', e)
  }
}

export async function getProductoId(id) {
  try {
    const req = await axios.get(`http://127.0.0.1:8080/api/productos/${id}`)

    return req.data
  } catch (e) {
    console.error('ERROR:', e)
  }
}
