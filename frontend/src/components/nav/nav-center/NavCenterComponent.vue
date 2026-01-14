<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <div class="navbar-center hidden lg:flex">
    <ul class="menu menu-horizontal px-1">
      <li>
        <RouterLink :to="{ name: 'home' }">Inicio</RouterLink>
      </li>
      <li>
        <RouterLink :to="{ name: 'lista_productos' }">Productos</RouterLink>
      </li>
      <li>
        <RouterLink :to="{ name: 'lista_categorias' }">Categorías</RouterLink>
      </li>
    </ul>
  </div>
</template>
