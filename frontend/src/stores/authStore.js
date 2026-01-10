import { defineStore } from 'pinia'
import { ref } from 'vue'
import authApi from '@/api/authApi'
import { toast } from 'vue-sonner'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const nombreUsuarioTemporal = ref(null)
  const usuario = ref(null)
  const cargandoUsuario = ref(true)
  const usuarioCargado = ref(false)

  async function iniciarSesion(data) {
    try {
      const req = await authApi.iniciarSesion(data)

      toast.success(req.data.msg || 'Has iniciado sesión correctamente')

      usuario.value = req.data.usuario
      usuarioCargado.value = true

      await router.push({ name: 'lista_productos' })
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
        position: 'top-right',
      })

      usuario.value = null
      usuarioCargado.value = false
    }
  }

  async function registrarUsuario(data) {
    try {
      const req = await authApi.registrarUsuario(data)

      toast.success(req.data.msg || 'Te has registrado correctamente')

      nombreUsuarioTemporal.value = req.data.usuario.nombre

      await router.push({ name: 'login' })
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
        position: 'top-right',
      })
    }
  }

  async function cerrarSesion() {
    cargandoUsuario.value = true
    try {
      const req = await authApi.cerrarSesion()

      toast.success(req.data.msg)

      usuario.value = null
      usuarioCargado.value = false

      await router.push({ name: 'login' })
    } catch {
      toast.error('Ha ocurrido un error al cerrar sesión')
    } finally {
      cargandoUsuario.value = false
    }
  }

  async function cargarUsuario() {
    cargandoUsuario.value = true

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
