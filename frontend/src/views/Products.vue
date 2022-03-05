<template>
  <div class="products w-100">
    <div style="height: calc(100% - 35px); overflow-x: hidden; overflow-y: scroll;">
      <table class="table table-striped table-hover">
      <thead>
        <tr>
        <th scope="col">Product name</th>
        <th scope="col">Cost</th>
        <th scope="col">
          Amount available
        </th>
        </tr>
      </thead>
      <tbody >
        <tr v-for="(product, key) in $store.state.products" :key=key>
          <Product :data="product" />
        </tr>
      </tbody>
      </table>
    </div>
    <div class="d-flex justify-content-center">
      <button v-if="$store.state.prevProducts" @click="$store.dispatch('getPrevProducts'); currentPage--" type="button" class="btn btn-sm btn-outline-secondary me-2" width="10" >Prev</button>
      <span class="fs-5"> {{currentPage}} / {{parseInt(Math.ceil($store.state.countProduct / 10))}} </span>
      <button v-if="$store.state.nextProducts" @click="$store.dispatch('getNextProducts'); currentPage++" type="button" class="btn btn-sm btn-outline-secondary ms-2" width="10" >Next</button>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'
import Product from '@/components/Product.vue'

@Options({
  components: {
    Product
  },
  data () {
    return {
      currentPage: 1
    }
  }
})
export default class Products extends Vue {}

</script>

<style scoped>
.products {
    border: 1px solid gray;
}
</style>
