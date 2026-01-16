import { eliminarCategoria, getCategorias, insertarCategoria } from '@/api/categorias.api'
import { useMutation, useQuery, useQueryClient } from '@tanstack/vue-query'
import { toast } from 'vue-sonner'

export function useGetCategorias() {
  return useQuery({
    queryKey: ['categorias'],
    queryFn: () => getCategorias(),
  })
}

export function useInsertarCategoria() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (data) => insertarCategoria(data),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['categorias'] })
      toast.success(data.msg || 'Se ha insertado la categoría correctamente')
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ha ocurrido un error al insertar la categoría')
    },
  })
}

export function useDeleteCategoria() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: (id) => eliminarCategoria(id),
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['categorias'] })
      toast.success(data.msg || 'Se ha eliminado la categoría correctamente')
    },
    onError: (e) => {
      toast.error(e.response?.data?.error || 'Ha ocurrido un error al eliminar la categoría')
    },
  })
}
