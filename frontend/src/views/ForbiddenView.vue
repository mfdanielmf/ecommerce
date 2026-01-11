<template>
  <main class="h-screen grid place-content-center text-center">
    <p class="text-[64px] font-semibold text-neutral-700">403</p>
    <h1 class="tracking-widest font-medium text-[20px]">ACCESO DENEGADO</h1>

    <div class="divider divider-warning my-6">¿Volvemos?</div>

    <div>
      <RouterLink :to="{ name: 'home' }" class="btn btn-outline rounded-3xl"
        >Volver al inicio</RouterLink
      >
    </div>
  </main>
</template>
