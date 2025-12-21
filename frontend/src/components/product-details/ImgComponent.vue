<script setup>
const props = defineProps({
  img_url: {
    type: String,
    required: true,
  },
  alt: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <div class="rounded-2xl overflow-hidden">
    <img
      :src="props.img_url"
      :alt="props.alt"
      class="w-full h-full bg-cover"
      fetchpriority="high"
    />
  </div>
</template>
