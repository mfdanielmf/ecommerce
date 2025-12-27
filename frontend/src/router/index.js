import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const ProductsView = () => import('@/views/ProductsView.vue')
const ProductDetailsView = () => import('@/views/ProductDetailsView.vue')
const AuthLayout = () => import('@/layouts/AuthLayout.vue')
const LoginView = () => import('@/views/LoginView.vue')
const RegisterView = () => import('@/views/RegisterView.vue')
const NotFoundView = () => import('@/views/NotFoundView.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
      path: '/:pathMatch(.*)*',
      name: 'not_found',
      component: NotFoundView,
    },
  ],
})

export default router
