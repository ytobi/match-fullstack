<template>
  <div id="nav" class="d-flex ">
    <div class="nv-lnk m-2">
      <router-link to="/" @click="$store.dispatch('getProducts')" >Products</router-link>
    </div>
    <div class="nv-lnk m-2">
      <router-link to="/login" v-if="!$store.state.user">Login</router-link>
      <router-link to="/login" v-else @click="$store.dispatch('signOut')"> Logout</router-link>
    </div>
    <div class="nv-lnk m-2" v-if="$store.state.user" >
      <router-link to="/myaccount" >My Account</router-link>
    </div>
    <div class="nv-lnk m-2" v-if="$store.state.user?.role == 'Seller'" >
      <router-link to="/myproducts" @click="$store.dispatch('getUserProducts', prev=false, next=false)">My Products</router-link>
    </div>
    <div v-if="$store.state.user?.role !== 'Seller'" class="nv-lnk m-2 d-flex">
      <router-link to="/cart">
        Cart
        <span class="badge bg-success"> {{$store.state.totalProductsInCart}} </span>
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
})
export default class NavBar extends Vue {
}

</script>

<style scoped>
.nv-lnk {
    margin: 5px;
}
</style>
