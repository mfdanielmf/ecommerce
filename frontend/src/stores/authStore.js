import { defineStore } from 'pinia'
import { ref } from 'vue'
import authApi from '@/api/authApi'
import { toast } from 'vue-sonner'

export const useAuthStore = defineStore('auth', () => {
  const nombreUsuarioTemporal = ref(null)
  const usuario = ref(null)
  const cargandoUsuario = ref(false)
  const usuarioCargado = ref(false)
  let promesa = null

  async function iniciarSesion(data) {
    try {
      const req = await authApi.iniciarSesion(data)

      toast.success(req.data.msg || 'Has iniciado sesión correctamente')

      usuario.value = req.data.usuario
      usuarioCargado.value = true

      return true //Redirigir a productos o a la url que intentó acceder
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
        position: 'top-right',
      })

      usuario.value = null
      usuarioCargado.value = false

      return false //No redirigir
    }
  }

  async function registrarUsuario(data) {
    try {
      const req = await authApi.registrarUsuario(data)

      toast.success(req.data.msg || 'Te has registrado correctamente')

      nombreUsuarioTemporal.value = req.data.usuario.nombre

      return true //Redirigir a login
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
        position: 'top-right',
      })

      return false // No redirigir
    }
  }

  async function cerrarSesion() {
    cargandoUsuario.value = true
    try {
      const req = await authApi.cerrarSesion()

      toast.success(req.data.msg)

      usuario.value = null
      usuarioCargado.value = false

      return true //Redirigir a login
    } catch {
      toast.error('Ha ocurrido un error al cerrar sesión')

      return false //No redirigir
    } finally {
      cargandoUsuario.value = false
    }
  }

  async function cargarUsuario() {
    if (usuarioCargado.value) return

    // Evitamos que se haga un doble fetch a /me. Si ya estamos ejecutando la promesa, devolvemos esa misma
    if (promesa) return promesa

    cargandoUsuario.value = true
    promesa = ejecutarPeticion()
  }

  async function ejecutarPeticion() {
    try {
      const req = await authApi.obtenerUsuario()

      usuario.value = req.data.usuario
      usuarioCargado.value = true
    } catch {
      usuario.value = null
      usuarioCargado.value = false
    } finally {
      cargandoUsuario.value = false
    }
  }

  return {
    nombreUsuarioTemporal,
    usuario,
    cargandoUsuario,
    usuarioCargado,
    iniciarSesion,
    registrarUsuario,
    cerrarSesion,
    cargarUsuario,
  }
})
