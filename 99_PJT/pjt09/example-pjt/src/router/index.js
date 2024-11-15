import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'
import CartView from '@/views/CartView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name : 'home',
      component : HomeView
    },
    {
      path : '/cart',
      name : 'cart',
      component : CartView
    },
    {
      path : '/:product_id',
      name : 'productdetail',
      component : ProductView
    }
  ],
})

export default router
