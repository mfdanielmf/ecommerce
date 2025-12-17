<script setup>
import { MinusIcon, PlusIcon } from 'lucide-vue-next'

defineProps({
  stock: {
    required: true,
  },
})
</script>

<template>
  <p class="block my-2 text-sm text-slate-800">Elige una cantidad:</p>

  <div class="relative">
    <button
      class="absolute h-8 w-8 right-10 top-1 my-auto px-2 flex items-center justify-center cursor-pointer bg-white rounded transition-colors hover:bg-slate-200"
      type="button"
    >
      <MinusIcon />
    </button>

    <input
      type="number"
      name="cantidad"
      min="1"
      :max="stock"
      value="1"
      class="w-full pl-4 h-10 pr-3 py-2 bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md"
    />

    <button
      class="absolute h-8 w-8 right-1 top-1 my-auto px-2 flex items-center justify-center cursor-pointer bg-white rounded transition-colors hover:bg-slate-200"
      type="button"
    >
      <PlusIcon />
    </button>
  </div>
</template>
