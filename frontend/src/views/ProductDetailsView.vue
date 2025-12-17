<script setup>
import { productStore } from '@/stores/productosStore'
import { computed, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import ErrorMessage from '@/components/common/ErrorMessage.vue'
import { MinusIcon, PlusIcon, ShoppingCartIcon } from 'lucide-vue-next'

const props = defineProps({
  id: {
    required: true,
  },
})

const almacenProductos = productStore()

const producto = computed(() => {
  return almacenProductos.getProductoPorId(Number(props.id))
})

onMounted(async () => {
  almacenProductos.error = null

  if (!producto.value) {
    await almacenProductos.fetchProductoId(Number(props.id))
  }
})
</script>

<template>
  <div v-if="almacenProductos.cargando" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="almacenProductos.error">{{ almacenProductos.error }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4 grid place-content-center">
    <div v-if="producto" class="grid lg:grid-cols-2 gap-12 mb-16">
      <div class="rounded-2xl overflow-hidden">
        <img :src="producto.img_url" :alt="producto.nombre" class="w-full h-full bg-cover" />
      </div>
      <div class="flex flex-col justify-center not-lg:items-center">
        <div class="mb-4">
          <span
            class="bg-blue-100 rounded-full font-semibold text-blue-600 px-3 py-1 tracking-wider"
            >Categoría</span
          >
        </div>

        <h1 class="text-4xl font-semibold mb-4">{{ producto.nombre }}</h1>

        <div class="flex items-center gap-2 mb-6">
          <div class="flex">
            <svg
              v-for="(i, l) in 5"
              :key="l"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 640 640"
              class="w-5 h-5"
            >
              <path
                d="M341.5 45.1C337.4 37.1 329.1 32 320.1 32C311.1 32 302.8 37.1 298.7 45.1L225.1 189.3L65.2 214.7C56.3 216.1 48.9 222.4 46.1 231C43.3 239.6 45.6 249 51.9 255.4L166.3 369.9L141.1 529.8C139.7 538.7 143.4 547.7 150.7 553C158 558.3 167.6 559.1 175.7 555L320.1 481.6L464.4 555C472.4 559.1 482.1 558.3 489.4 553C496.7 547.7 500.4 538.8 499 529.8L473.7 369.9L588.1 255.4C594.5 249 596.7 239.6 593.9 231C591.1 222.4 583.8 216.1 574.8 214.7L415 189.3L341.5 45.1z"
              />
            </svg>
          </div>

          <p class="text-neutral-700">5.0 (342 reseñas)</p>
        </div>

        <span
          class="lg:self-start text-2xl bg-neutral-50 py-2 px-4 border-2 rounded-md border-neutral-200"
        >
          {{ producto.precio }}€
        </span>

        <p
          v-if="producto.descripcion"
          class="mt-8 border-t border-neutral-200 pt-4 text-neutral-600"
        >
          {{ producto.descripcion }}
        </p>

        <div class="w-[250px] max-w-sm relative mt-4">
          <p class="block mb-1 text-sm text-slate-800">Elige una cantidad:</p>

          <div class="relative">
            <button
              class="absolute h-8 w-8 right-10 top-1 my-auto px-2 flex items-center justify-center cursor-pointer bg-white rounded transition-colors hover:bg-slate-200"
              type="button"
            >
              <MinusIcon />
            </button>

            <input
              type="number"
              id="seleccion-cantidad"
              name="cantidad"
              min="1"
              :max="producto.stock"
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

          <button
            class="flex items-center justify-center gap-4 font-semibold px-4 py-3 mt-6 rounded-md w-full cursor-pointer bg-blue-500 text-white transition-all hover:bg-blue-600 hover:shadow-md"
          >
            <ShoppingCartIcon />
            <p>Añadir al carrito</p>
          </button>
        </div>
      </div>
    </div>
  </main>
</template>
