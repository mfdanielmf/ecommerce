<script setup>
defineProps({
  label: {
    type: String,
    required: true,
  },
  icon: {
    required: true,
  },
  namePath: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <li>
    <RouterLink
      :to="{ name: namePath }"
      class="is-drawer-close:tooltip is-drawer-close:tooltip-right"
      :data-tip="label"
      active-class="menu-active"
    >
      <component :is="icon" :size="16" />
      <span class="is-drawer-close:hidden">{{ label }}</span>
    </RouterLink>
  </li>
</template>
