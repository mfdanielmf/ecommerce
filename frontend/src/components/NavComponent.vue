<script setup lang="ts">
import { LogInIcon, MenuIcon } from 'lucide-vue-next'
import BlackButton from './common/BlackButton.vue'
</script>

<template>
  <div class="navbar bg-white/80 shadow-sm fixed top-0 backdrop-blur-md z-30">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <MenuIcon :size="20" />
        </div>
        <ul
          tabindex="-1"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li><a>Inicio</a></li>
          <li><a>Productos</a></li>
          <li>
            <a>Categorías</a>
            <ul class="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </li>
        </ul>
      </div>
      <a class="btn btn-ghost text-xl text-blue-600">TechStore</a>
    </div>

    <div class="navbar-center hidden lg:flex">
      <ul class="menu menu-horizontal px-1">
        <li><a>Inicio</a></li>
        <li><a>Productos</a></li>
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
    <div class="navbar-end">
      <BlackButton class="group flex items-center gap-2.5">
        <LogInIcon class="group-hover:translate-x-1 transition" />
        <p>Iniciar sesión</p>
      </BlackButton>
    </div>
  </div>
</template>
