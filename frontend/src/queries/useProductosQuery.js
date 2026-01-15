import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import {
  añadirProducto,
  editarProducto,
  eliminarProductoId,
  getProductos,
} from '@/api/productos.api'
import { toast } from 'vue-sonner'

export function useGetProductos() {
  return useQuery({
    queryKey: ['productos'],
    queryFn: () => getProductos(),
  })
}

export function useInsertarProducto() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (data) => añadirProducto(data),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['productos'] })
      toast.success(data.msg || 'Se ha insertado el producto correctamente')
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al insertar el producto')
    },
  })
}

export function useDeleteProducto() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (id) => eliminarProductoId(id),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['productos'] })
      toast.success(data.msg || 'Se ha eliminado el producto correctamente')
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al eliminar el producto')
    },
  })
}

export function useEditarProducto() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }) => editarProducto(id, data),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['productos'] })
      toast.success(data.msg || 'Se ha editado correctamente el producto')
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ocurrió un error inesperado al editar el producto')
    },
  })
}
