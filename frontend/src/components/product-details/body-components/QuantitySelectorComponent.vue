<script setup>
import { MinusIcon, PlusIcon } from 'lucide-vue-next'
import { ref, watch } from 'vue'

const props = defineProps({
  stock: {
    type: Number,
    required: true,
  },
})

const valor = ref(1)

function validarCantidad(nuevoValor) {
  if (nuevoValor > props.stock) {
    valor.value = props.stock
  } else if (!nuevoValor || nuevoValor < 1) {
    valor.value = 1
  } else {
    valor.value = nuevoValor
  }
}

watch(valor, (nuevoValor) => {
  validarCantidad(nuevoValor)
})
</script>

<template>
  <p class="block my-2 text-sm text-slate-800">Elige una cantidad (max {{ stock }}):</p>

  <div class="relative">
    <button
      class="absolute h-8 w-8 right-10 top-1 my-auto px-2 flex items-center justify-center cursor-pointer bg-white rounded transition-colors hover:bg-slate-200"
      type="button"
      @click="valor--"
    >
      <MinusIcon />
    </button>

    <input
      type="number"
      name="cantidad"
      min="1"
      :max="stock"
      v-model.number="valor"
      class="w-full pl-4 h-10 pr-3 py-2 bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-400 shadow-sm focus:shadow-md"
    />

    <button
      class="absolute h-8 w-8 right-1 top-1 my-auto px-2 flex items-center justify-center cursor-pointer bg-white rounded transition-colors hover:bg-slate-200"
      type="button"
      @click="valor++"
    >
      <PlusIcon />
    </button>
  </div>
</template>
