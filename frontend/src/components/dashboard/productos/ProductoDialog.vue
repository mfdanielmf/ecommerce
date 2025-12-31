<script setup>
import { XIcon } from 'lucide-vue-next'
import {
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogOverlay,
  DialogPortal,
  DialogRoot,
  DialogTitle,
} from 'radix-vue'
import ProductoForm from './ProductoForm.vue'

defineProps({
  open: {
    type: Boolean,
    required: true,
  },
})

const emit = defineEmits(['update:open'])
</script>

<template>
  <DialogRoot :open="open" @update:open="emit('update:open', $event)">
    <DialogPortal>
      <DialogOverlay class="bg-black/50 fixed inset-0 z-30" />
      <DialogContent
        class="fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-112.5 translate-x-[-50%] translate-y-[-50%] rounded-md bg-white p-6.25 shadow-[hsl(206_22%_7%/35%)_0px_10px_38px_-10px,hsl(206_22%_7%/20%)_0px_10px_20px_-15px] focus:outline-none z-100"
      >
        <DialogTitle class="m-0 text-[17px] font-semibold"> Crear un nuevo producto </DialogTitle>

        <DialogDescription class="mt-2.5 mb-5 text-[15px] leading-normal">
          Introduce los datos del producto
        </DialogDescription>

        <!-- Formulario para introducir el producto -->
        <ProductoForm />

        <div class="mt-6.25 flex justify-end gap-3">
          <DialogClose as-child>
            <button class="btn">Cancelar</button>
          </DialogClose>

          <DialogClose as-child>
            <button class="btn bg-neutral-800 text-white hover:bg-neutral-900">
              Añadir Producto
            </button>
          </DialogClose>
        </div>

        <DialogClose
          class="btn btn-circle btn-ghost w-7.5 h-7.5 hover:bg-neutral-200 focus:shadow-green-500 absolute top-2.5 right-2.5"
          aria-label="Close"
        >
          <XIcon class="cursor-pointer" :size="18" />
        </DialogClose>
      </DialogContent>
    </DialogPortal>
  </DialogRoot>
</template>
