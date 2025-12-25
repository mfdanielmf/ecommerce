<script setup>
  import { MenuIcon } from 'lucide-vue-next';
  import { RouterLink } from 'vue-router';
</script>

<template>
  <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <MenuIcon :size="20" />
        </div>
        <ul
          tabindex="-1"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li>
            <RouterLink :to="{name: 'home'}">Inicio</RouterLink>
          </li>
          <li>
            <RouterLink :to="{name: 'lista_productos'}">Productos</RouterLink>
          </li>
          <li>
            <a>Categorías</a>
            <ul class="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </li>
        </ul>
      </div>
      <RouterLink :to="{name: 'home'}" class="btn btn-ghost text-xl text-blue-600">TechStore</RouterLink>
    </div>
</template>
