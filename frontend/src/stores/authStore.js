import { defineStore } from 'pinia'
import { ref } from 'vue'
import authApi from '@/api/authApi'
import { toast } from 'vue-sonner'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const nombreUsuarioTemporal = ref(null)
  const usuario = ref(null)
  const cargandoUsuario = ref(false)

  async function iniciarSesion(data) {
    try {
      const req = await authApi.iniciarSesion(data)

      toast.success(req.data.msg || 'Has iniciado sesión correctamente')

      usuario.value = req.data.usuario

      await router.push({ name: 'lista_productos' })
    } catch (e) {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
        position: 'top-right',
      })
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

  return { nombreUsuarioTemporal, usuario, cargandoUsuario, iniciarSesion, registrarUsuario }
})
