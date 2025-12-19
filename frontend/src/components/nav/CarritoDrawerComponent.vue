<script setup>
import { ShoppingCartIcon } from 'lucide-vue-next'
</script>

<template>
  <div class="drawer drawer-end flex items-center justify-end border-r border-neutral-500 pr-5">
    <input id="my-drawer-5" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex items-center">
      <!-- Page content here -->
      <label for="my-drawer-5" class="indicator drawer-button cursor-pointer">
        <ShoppingCartIcon :size="20" />
        <span class="badge badge-sm rounded-full indicator-item">8</span>
      </label>
    </div>
    <div class="drawer-side">
      <label for="my-drawer-5" aria-label="close sidebar" class="drawer-overlay"></label>
      <ul class="menu bg-base-200 min-h-full w-xl p-4">
        <!-- Sidebar content here -->
        <li><a>Sidebar Item 1</a></li>
        <li><a>Sidebar Item 2</a></li>
      </ul>
    </div>
  </div>
</template>
