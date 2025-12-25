<script setup>
  import { RouterLink } from 'vue-router';
</script>

<template>
  <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li>
          <RouterLink :to="{name: 'home'}">Inicio</RouterLink>
        </li>
        <li>
          <RouterLink :to="{name: 'lista_productos'}">Productos</RouterLink>
        </li>
        <li>
          <details>
            <summary>Categorías</summary>
            <ul class="p-2 bg-base-200 w-40 z-1">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </details>
        </li>
      </ul>
    </div>
</template>
