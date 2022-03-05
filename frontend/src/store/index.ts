import { createStore } from 'vuex'
import axios from 'axios'
import router from '@/router'
import { useToast } from 'vue-toastification'

const SERVER_URL = "http://127.0.0.1:8000"
const toast = useToast()

export default createStore({
  state: {
    products: {},
    userProducts: Array(),
    cart: Array(),
    user: null,
    countProduct: 0,
    prevProducts: '',
    nextProducts: '',
    signIn: true,
    signUp: false,
    userAuth: undefined,
    totalAmountInCart: 0,
    totalProductsInCart: 0
  },
  mutations: {
    setUser (state, user) {
      state.user = user
    },
    setUserAuth (state, auth) {
      state.userAuth = auth
    },
    setProducts (state, products) {
      state.products = products
    },
    setUserProducts (state, products) {
      state.userProducts = products
    },
    setCountProduct (state, count) {
      state.countProduct = count
    },
    setPrevProduct (state, prev) {
      state.prevProducts = prev
    },
    setNextProduct (state, next) {
      state.nextProducts = next
    },
    addProductToCart (state, product) {
      state.totalProductsInCart++
      const productInCart = state.cart.find(p => p.id === product.id)
      if (productInCart) {
        const index = state.cart.indexOf(productInCart, 0)
        if (index > -1) {
          state.cart.splice(index, 1)
        }
        productInCart.amount++
        state.cart.push(productInCart)
      } else {
        product.amount = 1
        state.cart.push(product)
      }
      let total = 0
      state.cart.forEach( (product) => {
          total = product.amount * product.cost
      });
      state.totalAmountInCart = total
    },
    removeFromCart (state, product) {
      state.totalProductsInCart--
      const productInCart = state.cart.find(p => p.id === product.id)
      const index = state.cart.indexOf(productInCart, 0)
      state.cart[index].amount = state.cart[index].amount - 1
      if (state.cart[index].amount <= 0) {
        state.cart.splice(index, 1)
      }

      let total = 0
      state.cart.forEach( (product) => {
          total = product.amount * product.cost
      });
      state.totalAmountInCart = total
    },
    showLogin (state) {
      state.signIn = false
      state.signUp = true
    },
    clearCart (state) {
      state.cart = []
    },
  },
  actions: {
    async getUser ({ commit, state }) {
      const res = await axios.get(SERVER_URL + '/user/', {auth: state.userAuth})
      if (res.status == 200) {
        commit('setUser', res.data)
      }
    },
    async signUp ({ commit }, { payload }) {
      await axios.post(SERVER_URL + '/user/create/', payload).then(
        function(res) {
          commit('setUser', res.data)
          const auth = {username: payload.username, password: payload.password}
          commit('setUserAuth', auth)
          router.push('/myaccount')
        }
      )
      .catch(
        function(error) {
          if (error.response) {
            for (let key in error.response.data) {
              toast.error(key + ' : ' + error.response.data[key][0])
            }
          } else if (error.request) {
            toast.error(error.request)
          } else {
            toast.error(error.message)
          }
        }
      );
    },
    async getProducts ({ commit }) {
      const res = await axios.get(SERVER_URL + '/product/')
      commit('setProducts', res.data.results)
      commit('setCountProduct', res.data.count)
      commit('setPrevProduct', res.data.previous)
      commit('setNextProduct', res.data.next)
    },
    async getPrevProducts ({ commit, state }) {
      const res = await axios.get(state.prevProducts)
      commit('setProducts', res.data.results)
      commit('setCountProduct', res.data.count)
      commit('setPrevProduct', res.data.previous)
      commit('setNextProduct', res.data.next)
    },
    async getNextProducts ({ commit, state }) {
      const res = await axios.get(state.nextProducts)
      commit('setProducts', res.data.results)
      commit('setCountProduct', res.data.count)
      commit('setPrevProduct', res.data.previous)
      commit('setNextProduct', res.data.next)
    },
    async getUserProducts ({ commit, state }) {
      await axios.get(SERVER_URL + '/product/user/', {auth: state.userAuth}).then(
        function (res) {
          commit('setUserProducts', res.data)
        }
      ).catch( function (error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async createNewProduct ({ dispatch, state }, payload) {
      await axios.post(SERVER_URL + '/product/', payload, {auth: state.userAuth}).then(
        function (res) {
          dispatch('getUserProducts')
        }
      ).catch( function (error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async modifyProduct ({ dispatch, state }, payload) {
      await axios.patch(`http://127.0.0.1:8000/product/${payload.id}/`, payload, {auth: state.userAuth}).then(
        function (res) {
          dispatch('getUserProducts')
        }
      ).catch( function (error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async signIn ({ commit }, { payload }) {
      await axios.get(SERVER_URL + '/user/', {auth: payload}).then(
        function (res) {
          commit('setUserAuth', payload)
          commit('setUser', res.data)
          router.push('/myaccount')
        }
      ).catch( function (error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async signOut ({ commit, dispatch }) {
      commit('setUser', undefined)
      commit('setUserAuth', undefined)
      dispatch('getProducts')
      router.push('/')
    },
    async deposit ({ commit, state }, {payload}) {
      const res = await axios.post(SERVER_URL + '/user/deposit/', payload, {auth: state.userAuth}).then(
        function (res) {
          commit('setUser', res.data)
        }
      ).catch( function(error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async reset ({ commit, state }) {
      await axios.get(SERVER_URL + '/user/reset/', {auth: state.userAuth})
      .then(
        function (res) {
          commit('setUser', res.data)
        }
      ).catch( function(error) {
        if (error.response) {
          for (let key in error.response.data) {
            toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
    async buy ({ commit, dispatch, state }) {
      let payload = state.cart
      payload.forEach( (product) => {
          product.productId = product.id;
      });
      await axios.post(SERVER_URL + '/user/buy/', {products: payload}, {auth: state.userAuth}).then(
        function (res) {
          commit('clearCart')
          commit('setUser', res.data)
          dispatch('getUser')
          router.push('/cart')
        }
      ).catch( function(error) {
        if (error.response) {
          for (let key in error.response.data) {
              toast.error(key + ' : ' + error.response.data[key])
          }
        } else if (error.request) {
          toast.error(error.request)
        } else {
          toast.error(error.message)
        }
      })
    },
  },
  modules: {
  }
})
