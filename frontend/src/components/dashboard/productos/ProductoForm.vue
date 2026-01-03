<script setup>
import { configure, useForm } from 'vee-validate'
import * as yup from 'yup'
import ProductoField from './ProductoField.vue'

const props = defineProps({
  funcion: {
    type: Function,
    required: true,
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
  precio: yup
    .number()
    .required('El precio es obligatorio')
    .min(0.0, 'El precio no puede ser negativo')
    .max(99999999.99, 'Has superado el límite de precio'),
  stock: yup
    .number()
    .required('El stock es obligatorio')
    .integer('El stock no puede tener decimales')
    .typeError('El stock no puede tener decimales')
    .min(0, 'El stock no puede ser negativo'),
  url: yup
    .string()
    .required('La imagen es obligatoria')
    .max(500, 'El tamaño máximo de la url es de 500 caracteres'),
})

const { handleSubmit, isSubmitting } = useForm({
  validationSchema: schema,
  initialValues: {
    precio: 0.0,
    stock: 0,
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
      <ProductoField
        nombre="nombre"
        tipo="text"
        label="Nombre *"
        placeholder="Introduce el nombre del producto"
      />

      <ProductoField
        nombre="descripcion"
        tipo="text"
        label="Descripción *"
        placeholder="Introduce la descripción del producto"
      />

      <ProductoField nombre="precio" tipo="number" label="Precio *" :min="0" :step="0.01" />

      <ProductoField nombre="stock" tipo="number" label="Stock *" :min="0" />

      <ProductoField
        nombre="url"
        tipo="text"
        label="URL imagen *"
        placeholder="Introduce la imagen del producto"
      />
    </div>
  </form>
</template>
