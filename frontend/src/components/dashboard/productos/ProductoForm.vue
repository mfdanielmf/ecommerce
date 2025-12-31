<template>
  <form>
    <div class="flex flex-col gap-2">
      <label for="nombre">Nombre *</label>
      <input
        type="text"
        name="nombre"
        id="nombre"
        class="input"
        placeholder="Introduce el nombre del producto"
      />
    </div>

    <div class="flex flex-col gap-2 mt-2">
      <label for="descripcion">Descripción *</label>
      <input
        type="text"
        name="descripcion"
        id="descripcion"
        class="input"
        placeholder="Introduce la descripción del producto"
      />
    </div>

    <div class="flex flex-col gap-2 mt-2">
      <label for="precio">Precio *</label>
      <input
        type="text"
        name="precio"
        id="precio"
        class="input"
        placeholder="Introduce un precio"
      />
    </div>

    <div class="flex flex-col gap-2 mt-2">
      <label for="stock">Stock *</label>
      <input
        type="number"
        name="stock"
        id="stock"
        class="input"
        min="0"
        value="0"
        placeholder="Introduce el stock"
      />
    </div>

    <div class="flex flex-col gap-2 mt-2">
      <label for="url">URL img *</label>
      <input
        type="text"
        name="url"
        id="url"
        class="input"
        placeholder="Introduce la url de la imagen del producto"
      />
    </div>
  </form>
</template>
