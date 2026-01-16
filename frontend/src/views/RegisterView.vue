<script setup>
import { CircleXIcon } from 'lucide-vue-next'
import { useForm } from 'vee-validate'
import * as yup from 'yup'
import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const nombreInput = ref(null)

const schema = yup.object({
  nombre: yup
    .string()
    .required('El nombre de usuario es obligatorio')
    .min(4, 'El nombre de usuario es demasiado corto (MIN: 4 caracteres)')
    .max(20, 'El nombre de usuario es demasiado largo (MAX: 20 caracteres)'),
  correo: yup
    .string()
    .required('El correo es obligatorio')
    .email('No has introducido un correo válido'),
  contraseña: yup
    .string()
    .required('La contraseña es obligatoria')
    .min(6, 'La contraseña es demasiado corta (MIN: 6 caracteres)'),
  contraseña_repetir: yup
    .string()
    .required('No has confirmado la contraseña')
    .oneOf([yup.ref('contraseña')], 'Las contraseñas no coinciden'),
})

const { defineField, handleSubmit, errors, isSubmitting } = useForm({
  validationSchema: schema,
})

const [usuario, usuarioProps] = defineField('nombre')
const [correo, correoProps] = defineField('correo')
const [contraseña, contraseñaProps] = defineField('contraseña')
const [contraseñaRepetir, contraseñaRepetirProps] = defineField('contraseña_repetir')

onMounted(() => {
  nombreInput.value?.focus()
})

const onSubmit = handleSubmit(async (data) => {
  const success = await authStore.registrarUsuario(data)

  if (success) await router.push({ name: 'login' })
})
</script>

<template>
  <form @submit.prevent="onSubmit">
    <div class="flex flex-col">
      <label for="nombre">Usuario</label>
      <input
        ref="nombreInput"
        type="text"
        name="nombre"
        id="nombre"
        placeholder="Introduce nombre de usuario"
        v-model="usuario"
        v-bind="usuarioProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p v-if="errors.nombre" class="text-error flex items-center gap-1 mt-1">
        <CircleXIcon :size="18" />
        {{ errors.nombre }}
      </p>
    </div>

    <div class="flex flex-col mt-4">
      <label for="correo">Correo electrónico</label>
      <input
        type="email"
        name="correo"
        id="correo"
        placeholder="Introduce tu correo"
        v-model="correo"
        v-bind="correoProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p v-if="errors.correo" class="text-error flex items-center gap-1 mt-1">
        <CircleXIcon :size="18" />
        {{ errors.correo }}
      </p>
    </div>

    <div class="flex flex-col mt-4">
      <label for="contraseña">Contraseña</label>
      <input
        type="password"
        name="contraseña"
        id="contraseña"
        placeholder="Introduce una contraseña"
        v-model="contraseña"
        v-bind="contraseñaProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p v-if="errors.contraseña" class="text-error flex items-center gap-1 mt-1">
        <CircleXIcon :size="18" />
        {{ errors.contraseña }}
      </p>
    </div>

    <div class="flex flex-col mt-4">
      <label for="contraseña-repetir">Repetir contraseña</label>
      <input
        type="password"
        name="contraseña-repetir"
        id="contraseña-repetir"
        placeholder="Repite la contraseña"
        v-model="contraseñaRepetir"
        v-bind="contraseñaRepetirProps"
        class="border border-gray-300 rounded-md p-2 w-full transition-all hover:border-slate-400 focus:outline-none focus:border-slate-400 focus:shadow-md"
      />
      <p v-if="errors.contraseña_repetir" class="text-error flex items-center gap-1 mt-1">
        <CircleXIcon :size="18" />
        {{ errors.contraseña_repetir }}
      </p>
    </div>

    <button type="submit" class="btn btn-primary w-full mt-4" :disabled="isSubmitting">
      <span class="loading loading-spinner" v-if="isSubmitting"></span>
      {{ isSubmitting ? 'Cargando...' : 'Registrarse' }}
    </button>
  </form>
</template>
