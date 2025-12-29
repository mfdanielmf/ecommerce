<script setup>
import AsideItem from '@/components/dashboard/AsideItem.vue'
import {
  FolderTreeIcon,
  LayoutDashboardIcon,
  PackageIcon,
  PanelLeftOpenIcon,
  ShoppingCartIcon,
} from 'lucide-vue-next'

// ------------ACORDARME DE IMPLEMENTAR LÓGICA PARA NO PERMITIR EL ACCESO AL DASH MIENTRAS NO SE CARGUE EL USUARIO Y NO SEA ADMIN!!!!!!!!!! (PONDRÉ UN SPINNER O ALGO ASÍ. YA VERÉ) ---------------------
</script>

<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <!-- Navbar -->
      <nav class="navbar w-full bg-base-300">
        <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
          <PanelLeftOpenIcon :size="24" />
        </label>

        <div class="px-4">Test</div>
      </nav>

      <!-- Contenido principal -->
      <RouterView class="p-4" />
    </div>

    <div class="drawer-side is-drawer-close:overflow-visible">
      <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
      <div
        class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-14 is-drawer-open:w-64"
      >
        <!-- Contenido sidebar -->
        <ul class="menu w-full grow">
          <AsideItem :icon="LayoutDashboardIcon" label="Dashboard" name-path="admin_dashboard" />

          <AsideItem :icon="PackageIcon" label="Productos" name-path="admin_productos" />

          <AsideItem :icon="FolderTreeIcon" label="Categorías" name-path="admin_categorias" />

          <AsideItem :icon="ShoppingCartIcon" label="Pedidos" name-path="admin_pedidos" />
        </ul>
      </div>
    </div>
  </div>
</template>
