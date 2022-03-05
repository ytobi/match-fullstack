<template>
  <div class="cart w-100 h-100">
    <div style="height: calc(100% - 60px)">
      <table class="table table-striped table-hover">
        <thead>
          <tr>
          <th scope="col">Product name</th>
          <th scope="col">Cost</th>
          <th scope="col">
            Amount
          </th>
          </tr>
        </thead>
        <tbody >
          <tr v-for="(product, key) in $store.state.cart" :key=key>
            <td> {{ product.productName }}</td>
            <td> {{ product.cost }}  </td>
            <td >
              <div class="d-flex">
                <span class="w-50 text-end me-2"> {{ product.amount }} </span>
                <button @click="$store.commit('removeFromCart', product);" type="button" class="btn btn-sm btn-outline-success align-item-end" width="10" >Remove</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="w-100 text-start d-flex justify-content-between">
      <span class="fw-bold ms-2"> Total: {{ $store.state.totalAmountInCart }} USD </span>
      <button type="button" class="btn btn-outline-success me-3" @click="$store.dispatch('buy')">Checkout</button>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
  components: {
  }
})
export default class MyAccount extends Vue {}

</script>

<style scoped>
.cart {
    border: 1px solid lightseagreen;
}
</style>