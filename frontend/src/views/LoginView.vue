<script setup>
import { CircleXIcon } from 'lucide-vue-next'
import { useForm } from 'vee-validate'
import * as yup from 'yup'
import authApi from '@/api/authApi'
import { toast } from 'vue-sonner'

const schema = yup.object({
  nombre: yup
    .string()
    .required('El nombre de usuario es obligatorio')
    .min(4, 'El nombre de usuario es demasiado corto (MIN: 4 caracteres)')
    .max(20, 'El nombre de usuario es demasiado largo (MAX: 20 caracteres)'),
  contraseña: yup
    .string()
    .required('La contraseña es obligatoria')
    .min(6, 'La contraseña es demasiado corta (MIN: 6 caracteres)'),
})

const { defineField, handleSubmit, errors, isSubmitting } = useForm({
  validationSchema: schema,
})

const [nombreUsuario, nombreUsuarioProps] = defineField('nombre')
const [contraseña, contraseñaProps] = defineField('contraseña')

const onSubmit = handleSubmit(async (data) => {
  try {
    const req = await authApi.iniciarSesion(data)

    toast.success(req.data.msg || 'Has iniciado sesión correctamente')
  } catch (e) {
    toast.error(e.response?.data?.error || 'Ocurrió un error inesperado', {
      position: 'top-right',
    })
  }
})
</script>

<template>
  <form @submit.prevent="onSubmit">
    <div class="flex flex-col">
      <label for="nombre">Usuario</label>
      <input
        type="text"
        name="usuario"
        id="nombre"
        placeholder="Introduce el nombre de usuario"
        v-model="nombreUsuario"
        v-bind="nombreUsuarioProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p class="text-error flex items-center gap-1 mt-1" v-if="errors.nombre">
        <CircleXIcon :size="18" />
        {{ errors.nombre }}
      </p>
    </div>

    <div class="flex flex-col mt-4">
      <label for="contraseña">Contraseña</label>
      <input
        type="password"
        name="contraseña"
        id="contraseña"
        placeholder="Introduce la contraseña"
        v-model="contraseña"
        v-bind="contraseñaProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p class="text-error flex items-center gap-1 mt-1" v-if="errors.contraseña">
        <CircleXIcon :size="18" />
        {{ errors.contraseña }}
      </p>
    </div>

    <button type="submit" class="btn btn-primary w-full mt-4" :disabled="isSubmitting">
      <span class="loading loading-spinner" v-if="isSubmitting"></span>
      {{ isSubmitting ? 'Cargando...' : 'Iniciar sesión' }}
    </button>
  </form>
</template>
