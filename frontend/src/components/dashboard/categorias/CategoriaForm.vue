<script setup>
import { configure, useForm } from 'vee-validate'
import * as yup from 'yup'
import FormField from '../FormField.vue'

const props = defineProps({
  funcion: {
    type: Function,
    required: true,
  },
  categoria: {
    type: Object,
  },
})

configure({
  validateOnInput: false,
})

const schema = yup.object({
  nombre: yup
    .string()
    .required('El nombre es obligatorio')
    .max(50, 'El tamaño máximo es de 50 carateres'),
  descripcion: yup
    .string()
    .required('La descripción es obligatoria')
    .max(500, 'El tamaño máximo es de 500 caracteres'),
})

const { handleSubmit, isSubmitting } = useForm({
  validationSchema: schema,
  initialValues: {
    nombre: props.categoria?.nombre || '',
    descripcion: props.categoria?.descripcion || '',
  },
})

const onSubmit = handleSubmit(async (data) => {
  await props.funcion(data)
})

defineExpose({ onSubmit, isSubmitting })
</script>

<template>
  <form @submit.prevent="onSubmit">
    <div class="space-y-2">
      <FormField
        nombre="nombre"
        tipo="text"
        label="Nombre *"
        placeholder="Introduce el nombre de la categoría"
      />

      <FormField
        nombre="descripcion"
        tipo="text"
        label="Descripción *"
        placeholder="Introduce la descripción de la categoría"
      />
    </div>
  </form>
</template>
