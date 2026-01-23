import { hacerPedido, obtenerPedidosUsuario } from "@/api/pedidos.api";
import { carritoStore } from "@/stores/carrito.store";
import { useMutation, useQuery, useQueryClient } from "@tanstack/vue-query";
import { useRouter } from "vue-router";
import { toast } from "vue-sonner";

const carrito = carritoStore()

export function useHacerPedido() {
  const queryClient = useQueryClient()
  const router = useRouter()

  return useMutation({
    mutationFn: (data) => hacerPedido(data),
    onSuccess: (r) => {
      carrito.carrito = []
      queryClient.invalidateQueries({ queryKey: ["pedidos"] })
      toast.success(r.response?.data?.msg || "Pedido realizado correctamente!")
    },
    onError: (e) => {
      if (e.response?.status === 401) {
        router.push({ name: "login" })
        toast.warning("Inicia sesión para hacer el pedido")
      } else {
        toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al hacer el pedido')
      }

    }
  })
}

export function useObtenerPedidoUsuario() {
  return useQuery({
    queryKey: ["pedidos"],
    queryFn: () => obtenerPedidosUsuario()
  })
}
