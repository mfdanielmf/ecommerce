import { useAuthStore } from '@/stores/authStore'
import { createRouter, createWebHistory } from 'vue-router'

const MainLayout = () => import('@/layouts/MainLayout.vue')
const AuthLayout = () => import('@/layouts/AuthLayout.vue')
const DashboardLayout = () => import('@/layouts/DashboardLayout.vue')

const HomeView = () => import('@/views/HomeView.vue')
const ProductsView = () => import('@/views/ProductsView.vue')
const ProductDetailsView = () => import('@/views/ProductDetailsView.vue')
const LoginView = () => import('@/views/LoginView.vue')
const RegisterView = () => import('@/views/RegisterView.vue')
const NotFoundView = () => import('@/views/NotFoundView.vue')
const AdminDashboardView = () => import('@/views/admin/AdminDashboardView.vue')
const AdminProductosView = () => import('@/views/admin/AdminProductosView.vue')
const AdminCategoriasView = () => import('@/views/admin/AdminCategoriasView.vue')
const AdminPedidosView = () => import('@/views/admin/AdminPedidosView.vue')
const ForbiddenView = () => import('@/views/ForbiddenView.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: MainLayout,
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView,
        },
        {
          path: '/productos',
          name: 'lista_productos',
          component: ProductsView,
        },
        {
          path: '/productos/:id',
          name: 'detalles_producto',
          component: ProductDetailsView,
          props: true,
        },
        {
          path: '/auth',
          component: AuthLayout,
          redirect: { name: 'login' },
          children: [
            {
              path: 'login',
              name: 'login',
              component: LoginView,
              meta: {
                esLogin: true,
              },
            },
            {
              path: 'register',
              name: 'register',
              component: RegisterView,
              meta: {
                esLogin: false,
              },
            },
          ],
        },
        {
          path: '/forbidden',
          name: 'forbidden',
          component: ForbiddenView,
        },
        {
          path: '/:pathMatch(.*)*',
          name: 'not_found',
          component: NotFoundView,
        },
      ],
    },
    {
      path: '/admin',
      component: DashboardLayout,
      redirect: { name: 'admin_dashboard' },
      meta: { authRequired: true, adminRequired: true },
      children: [
        {
          path: 'dashboard',
          name: 'admin_dashboard',
          component: AdminDashboardView,
          meta: {
            titulo: 'Dashboard',
          },
        },
        {
          path: 'productos',
          name: 'admin_productos',
          component: AdminProductosView,
          meta: {
            titulo: 'Productos',
          },
        },
        {
          path: 'categorias',
          name: 'admin_categorias',
          component: AdminCategoriasView,
          meta: {
            titulo: 'Categorías',
          },
        },
        {
          path: 'pedidos',
          name: 'admin_pedidos',
          component: AdminPedidosView,
          meta: {
            titulo: 'Pedidos',
          },
        },
      ],
    },
  ],
})

router.beforeEach(async (to) => {
  const authStore = useAuthStore()

  if (to.meta.authRequired) {
    await authStore.cargarUsuario()

    if (!authStore.usuarioCargado) {
      return { name: 'login', query: { redirect: to.fullPath } }
    }

    if (authStore.usuario.rol !== 'admin') return { name: 'forbidden' }
  }
})

export default router
