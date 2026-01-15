import { getCategorias } from "@/api/categorias.api";
import { useQuery } from "@tanstack/vue-query";

export function useGetCategorias() {
  return useQuery({
    queryKey: ["categorias"],
    queryFn: () => getCategorias()
  })
}
