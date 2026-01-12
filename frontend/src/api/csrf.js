export function obtenerTokenCSRF() {
  return document.cookie
    .split('; ')
    .find((valor) => valor.startsWith('csrf_access_token='))
    ?.split('=')[1]
}
