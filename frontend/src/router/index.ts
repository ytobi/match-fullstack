import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Products from '../views/Products.vue'
import MyProducts from '../views/MyProducts.vue'
import Login from '../views/Login.vue'
import MyAccount from '../views/MyAccount.vue'
import Cart from '../views/Cart.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Products',
    component: Products
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/myproducts',
    name: 'MyProducts',
    component: MyProducts
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
