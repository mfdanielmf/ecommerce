import { useMutation, useQuery, useQueryClient } from "@tanstack/vue-query";
import { añadirProducto, eliminarProductoId, getProductos } from "@/api/productos.api";
import { toast } from "vue-sonner";

export function useGetProductos() {
  return useQuery({
    queryKey: ["productos"],
    queryFn: getProductos,
  })
}

export function useInsertarProducto() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: añadirProducto,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["productos"] })
      toast.success(data.msg || "Se ha insertado el producto correctamente")
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || "Ocurrió un error inesperado al insertar el producto")
    }
  })
}

export function useDeleteProducto() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: eliminarProductoId,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["productos"] })
      toast.success(data.msg || "Se ha eliminado el producto correctamente")
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al eliminar el producto')
    }
  })
}
