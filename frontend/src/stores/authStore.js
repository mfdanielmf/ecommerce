import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const nombreUsuarioTemporal = ref(null)
  const usuario = ref(null)

  return { nombreUsuarioTemporal, usuario }
})
