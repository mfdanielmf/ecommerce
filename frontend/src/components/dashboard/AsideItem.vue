<script setup>
defineProps({
  label: {
    type: String,
    required: true,
  },
  icon: {
    required: true,
  },
})
</script>

<template>
  <li>
    <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" :data-tip="label">
      <component :is="icon" :size="16" />
      <span class="is-drawer-close:hidden">{{ label }}</span>
    </button>
  </li>
</template>
