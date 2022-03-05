<template>
  <div class="products w-100 h-100">
    <div style="height: calc(100% - 60px); overflow-x: hidden; overflow-y: scroll;">
    <table v-if="!newProduct" class="table table-striped table-hover">
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
        <tr v-for="(product, key) in $store.state.userProducts" :key=key >
            <ProductEdit :data="product" />
        </tr>
      </tbody>
    </table>
    <div v-if="newProduct" class="d-flex flex-column align-items-center mt-3">
      <p class="fs-1">Create new product</p>
      <input class="form-control m-2 w-50" type="text" placeholder="Product name" v-model="newProduct.productName">
      <input class="form-control m-2 w-50" type="number" placeholder="Cost" v-model="newProduct.cost">
      <input class="form-control m-2 w-50" type="number" placeholder="Amount available" v-model="newProduct.amountAvailable">
      <button type="button" class="btn btn-outline-success w-50" @click="requsting=true; $store.dispatch('createNewProduct', newProduct); newProduct=undefined">
        <span v-if="requsting">
          <div class="spinner-border spinner-border-sm text-success me-3" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </span>
        <span>Add</span>
      </button>
    </div>
    </div>
    <div v-if="!newProduct"  class="w-100 text-start d-flex justify-content-end">
      <button type="button" class="btn btn-outline-success me-3" @click="newProduct={}">Add Product</button>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'
import ProductEdit from '@/components/ProductEdit.vue'

@Options({
  components: {
    ProductEdit
  },
  data () {
    return {
      newProduct: undefined,
      requsting: false
    }
  }
})
export default class MyProducts extends Vue {}

</script>

<style scoped>
.products {
    border: 1px solid gray;
}
</style>
