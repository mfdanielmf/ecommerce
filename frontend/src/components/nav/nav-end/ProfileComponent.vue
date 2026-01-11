<script setup>
import { ref } from 'vue'
import {
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuPortal,
  DropdownMenuRoot,
  DropdownMenuTrigger,
} from 'radix-vue'
import { LayoutDashboardIcon, LogOutIcon } from 'lucide-vue-next'
import { useAuthStore } from '@/stores/authStore'
import { useRouter } from 'vue-router'

const props = defineProps({
  usuario: {
    type: Object,
    required: true,
  },
})

const router = useRouter()

const toggleState = ref(false)

async function handleLogout() {
  const success = await useAuthStore().cerrarSesion()

  if (success) await router.push({ name: 'login' })
}
</script>

<template>
  <DropdownMenuRoot v-model:open="toggleState">
    <DropdownMenuTrigger
      class="avatar avatar-online avatar-placeholder cursor-pointer"
      aria-label="Opciones perfil"
    >
      <div class="bg-neutral text-neutral-content w-10 rounded-full">
        <span class="text-md">{{ props.usuario.nombre[0] }}</span>
      </div>
    </DropdownMenuTrigger>

    <DropdownMenuPortal>
      <DropdownMenuContent
        class="min-w-55 mr-1 z-50 outline-none bg-white rounded-md p-1.25 shadow-[0px_10px_38px_-10px_rgba(22,23,24,0.35),0px_10px_20px_-15px_rgba(22,23,24,0.2)] space-y-1"
        :side-offset="5"
      >
        <DropdownMenuItem v-if="usuario.rol === 'admin'" value="Dashboard" as-child>
          <RouterLink
            :to="{ name: 'admin_dashboard' }"
            class="cursor-pointer text-[13px] leading-none font-semibold rounded-[3px] flex items-center gap-1 h-6.25 px-2 select-none outline-none data-disabled:pointer-events-none data-highlighted:bg-neutral-200 transition-colors"
          >
            <LayoutDashboardIcon :size="20" />
            Dashboard
          </RouterLink>
        </DropdownMenuItem>

        <DropdownMenuItem
          value="Cerrar sesion"
          class="cursor-pointer text-[13px] leading-none text-red-500 font-semibold rounded-[3px] flex items-center gap-1 h-6.25 px-2 select-none outline-none data-disabled:pointer-events-none data-highlighted:bg-neutral-200 data-highlighted:text-red-600 transition-colors"
          @click="handleLogout"
        >
          <LogOutIcon :size="20" />
          Cerrar sesión
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenuPortal>
  </DropdownMenuRoot>
</template>
