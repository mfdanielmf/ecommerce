import { useMutation, useQuery, useQueryClient } from "@tanstack/vue-query";
import { eliminarProductoId, getProductos } from "@/api/productos.api";
import { toast } from "vue-sonner";

export function useGetProductos(){
  return useQuery({
    queryKey: ["productos"],
    queryFn: getProductos,
  })
}

export function useDeleteProducto(){
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (id) => eliminarProductoId(id),
    onSuccess: (data) => {
      queryClient.invalidateQueries({queryKey: ["productos"]})
      toast.success(data.msg)
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al eliminar el producto')
    }
  })
}
