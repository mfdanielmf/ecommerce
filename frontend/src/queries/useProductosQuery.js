import { useQuery } from "@tanstack/vue-query";
import { getProductos } from "@/api/productos.api";

export function useGetProductos(){
  return useQuery({
    queryKey: ["productos"],
    queryFn: getProductos,
  })
}
