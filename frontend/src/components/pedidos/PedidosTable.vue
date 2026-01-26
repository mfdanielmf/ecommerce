<script setup>
const props = defineProps({
  pedidos: {
    required: true
  }
})
</script>

<template>
  <!-- PERMITIR CANCELAR EL PEDIDO SI NO ESTÁ ENTREGADO O EN REPARTO
      EVITAR QUE SE VEAN LOS PEDIDOS DE OTRA PERSONA CUANDO CAMBIAMOS DE SESIÓN O CADUCA
      MEJORAR ESTILOS TABLA
      MOSTRAR UN MENSAJE SI NO HAY PEDIDOS
      NO PEDIR LOS PRODUCTOS DEL PEDIDO HASTA QUE QUIERA VER LOS DETALLES (para ahorrar carga de datos)
  -->

  <div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
  <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Total Pedido</th>
        <th>Estado</th>
        <th>Fecha Pedido</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <!-- body -->
    <tbody>
      <tr v-for="pedido of props.pedidos" :key="pedido.id">
        <th>{{ pedido.id }}</th>
        <td>{{ pedido.total }}€</td>
        <td>{{ pedido.status.charAt(0).toUpperCase() + pedido.status.slice(1) }}</td>
        <td>{{ pedido.fecha_creacion }}</td>
        <td class="flex items-center flex-wrap gap-4">
          <a class="link link-primary">Ver detalles</a>
          <button class="btn btn-error">Cancelar</button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
</template>
