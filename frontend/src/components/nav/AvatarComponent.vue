<script setup>
const props = defineProps({
  nombre: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="avatar avatar-online avatar-placeholder">
    <div class="bg-neutral text-neutral-content w-10 rounded-full">
      <span class="text-md">{{ props.nombre }}</span>
    </div>
  </div>
</template>
