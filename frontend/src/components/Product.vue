<template>
  <td @mouseenter="showAddToChart" @mouseleave="hideAddToChart"> {{ data.productName }}</td>
  <td @mouseenter="showAddToChart" @mouseleave="hideAddToChart"> {{ data.cost }}  </td>
  <td @mouseenter="showAddToChart" @mouseleave="hideAddToChart" v-if="this.inCart !== true" >
    <div class="d-flex">
      <span class="w-50 text-end me-2"> {{ data.amountAvailable }} </span>
      <button @click="$store.commit('addProductToCart', data)" type="button" class="btn btn-sm btn-outline-secondary align-item-end" width="10" :style="{'display': displayAddToCart}" >Add to Cart</button>
    </div>
  </td>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
  props: {
    data: {
    },
    inCart: false,
  },
  data () {
    return {
      displayAddToCart: 'none'
    }
  },
  methods: {
    showAddToChart () {
      this.displayAddToCart = !this.inCart && this.data.amountAvailable > 0 ? 'block' : 'none'
    },
    hideAddToChart () {
      this.displayAddToCart = 'none'
    }
  }
})
export default class Product extends Vue {
  msg!: string
}

</script>
