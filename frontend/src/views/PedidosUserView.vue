<script setup>
import { useObtenerPedidoUsuario } from '@/queries/usePedidosQuery';
import LoadingSpinner from '@/components/common/LoadingSpinner.vue';
import ErrorMessage from '@/components/common/ErrorMessage.vue';

const {data, isLoading, error} = useObtenerPedidoUsuario()
</script>

<template>
  <div v-if="isLoading" class="h-screen grid place-content-center">
    <LoadingSpinner />
  </div>

  <ErrorMessage v-else-if="error">{{ error.resonse?.data?.error || "Error al obtener los pedidos" }}</ErrorMessage>

  <main v-else class="min-h-screen py-20 px-4">
    <ul>
      <li v-for="pedido of data.pedidos" :key="pedido.id">{{ pedido.id }}</li>
    </ul>
  </main>
</template>
