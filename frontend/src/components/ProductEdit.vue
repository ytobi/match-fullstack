<template>
  <td> 
    <input @change="showSaveBtn" type="text" class="form-control" v-model="data.productName">
  </td>
  <td> 
    <input @change="showSaveBtn" type="number" class="form-control" v-model="data.cost">
  </td>
  <td >
    <div class="d-flex">
      <span class="w-50 text-end me-2"> 
        <input @change="showSaveBtn" type="number" class="form-control" v-model="data.amountAvailable">
      </span>
      <button @click="$store.dispatch('modifyProduct', data); displaySave='none'" type="button" class="btn btn-sm btn-outline-success align-item-end" width="10" :style="{'display': displaySave}" >Save</button>
    </div>
  </td>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
  props: {
    data: {
    },
  },
  data () {
    return {
      displaySave: 'none'
    }
  },
  methods: {
    showSaveBtn () {
      this.displaySave = 'block'
    },
    hideSaveBtn () {
      this.displaySave = 'none'
    }
  }
})
export default class Product extends Vue {
  msg!: string
}

</script>
