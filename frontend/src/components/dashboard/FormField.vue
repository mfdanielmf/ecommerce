<script setup>
import { Field } from 'vee-validate'
import { CircleXIcon } from 'lucide-vue-next'

defineProps({
  nombre: {
    required: true,
    type: String,
  },
  tipo: {
    required: true,
    type: String,
  },
  label: {
    required: true,
    type: String,
  },
  placeholder: {
    type: String,
  },
  min: {
    type: Number,
  },
  step: {
    type: Number,
  },
})
</script>

<template>
  <Field :name="nombre" v-slot="{ field, errorMessage, meta }">
    <div class="flex flex-col gap-2">
      <label :for="nombre">{{ label }}</label>

      <select
        v-if="tipo === 'select'"
        :id="nombre"
        class="select appearance-none w-full"
        :class="{
          'select-error': errorMessage,
          'select-success': (meta.valid && meta.dirty) || meta.valid,
        }"
        v-bind="field"
      >
        <slot></slot>
      </select>

      <input
        v-else
        :type="tipo"
        :id="nombre"
        class="input w-full"
        :class="{
          'input-error': errorMessage,
          'input-success': (meta.valid && meta.dirty) || (meta.valid && tipo === 'number'),
        }"
        :placeholder="placeholder"
        v-bind="field"
        :min="min"
        :step="step"
      />
      <p class="text-error flex items-center gap-1" v-if="errorMessage">
        <CircleXIcon :size="18" />
        {{ errorMessage }}
      </p>
    </div>
  </Field>
</template>
