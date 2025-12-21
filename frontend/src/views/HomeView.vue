<script setup>
import { MoveRightIcon } from 'lucide-vue-next'
import BlackButton from '@/components/common/BlackButton.vue'
</script>

<template>
  <main>
    <section class="flex items-center py-20 min-h-screen">
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-12 items-center">
          <div class="space-y-8">
            <div class="inline-block px-4 py-2 bg-neutral-200/100 rounded-full">
              <p class="text-gray-700">Descubre nuestros últimos productos</p>
            </div>

            <div class="space-y-4">
              <h1 class="text-xl text-blue-500">Líderes en tecnología</h1>
              <p class="max-w-md">
                Encuentra los mejores productos tecnológicos con precios increíbles. ¡Nuevas ofertas
                cada semana!
              </p>
            </div>

            <div class="flex items-center flex-wrap gap-4">
              <BlackButton class="group btn-lg font-normal">
                <p>Productos destacados</p>
                <MoveRightIcon :size="20" class="group-hover:translate-x-2 transition-transform" />
              </BlackButton>

              <RouterLink
                :to="{ name: 'lista_productos' }"
                class="btn btn-outline btn-lg font-normal"
                >Ver Catálogo</RouterLink
              >
            </div>

            <div class="flex gap-8">
              <div>
                <p>50+</p>
                <p>Productos</p>
              </div>

              <div>
                <p>10k+</p>
                <p>Clientes</p>
              </div>

              <div>
                <p>100%</p>
                <p>Satisfacción</p>
              </div>
            </div>
          </div>
          <div class="aspect-3/4 rounded-lg shadow-2xl overflow-hidden">
            <img
              src="../assets/img/main-image.jpeg"
              alt="Foto landing"
              class="w-full h-full object-cover"
              fetchpriority="high"
            />
          </div>
        </div>
      </div>
    </section>
  </main>
</template>
