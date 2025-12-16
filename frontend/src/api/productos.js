export async function getProductos() {
  const req = await fetch('https://fakestoreapi.com/products')

  if (!req.ok) {
    throw new Error('ERROR')
  }

  return req.json()
}
