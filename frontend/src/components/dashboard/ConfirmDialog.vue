<script setup>
import { Trash2Icon, XIcon } from 'lucide-vue-next'
import {
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogOverlay,
  AlertDialogPortal,
  AlertDialogRoot,
  AlertDialogTitle,
} from 'radix-vue'

const emit = defineEmits(['confirmarEliminar'])

defineProps({
  eliminando: {
    type: Boolean,
    required: true,
  },
})
</script>

<template>
  <AlertDialogRoot>
    <AlertDialogPortal>
      <AlertDialogOverlay
        class="bg-black/50 data-[state=open]:animate-overlayShow fixed inset-0 z-30"
      />
      <AlertDialogContent
        class="fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-112.5 translate-x-[-50%] translate-y-[-50%] rounded-md bg-white p-6.25 shadow-[hsl(206_22%_7%/35%)_0px_10px_38px_-10px,hsl(206_22%_7%/20%)_0px_10px_20px_-15px] focus:outline-none z-100"
      >
        <AlertDialogTitle class="m-0 text-[17px] font-semibold">
          <slot>¿Seguro que quieres eliminar?</slot>
        </AlertDialogTitle>

        <AlertDialogDescription class="mt-2.5 mb-5 text-[15px] leading-normal">
          Elige una opción
        </AlertDialogDescription>

        <div class="mt-6.25 flex justify-end gap-3">
          <AlertDialogCancel as-child>
            <button class="btn">Cancelar</button>
          </AlertDialogCancel>

          <button class="btn btn-error" @click="emit('confirmarEliminar')" :disabled="eliminando">
            <Trash2Icon :size="18" v-if="!eliminando" />
            <span class="loading loading-spinner" v-else></span>
            {{ eliminando ? 'Eliminando...' : 'Eliminar' }}
          </button>
        </div>

        <AlertDialogCancel
          class="btn btn-circle btn-ghost w-7.5 h-7.5 hover:bg-neutral-200 focus:shadow-green-500 absolute top-2.5 right-2.5"
          aria-label="Close"
        >
          <XIcon class="cursor-pointer" :size="18" />
        </AlertDialogCancel>
      </AlertDialogContent>
    </AlertDialogPortal>
  </AlertDialogRoot>
</template>
