<template>
  <div class="w-100 account row w-100 h-100">
    <div v-if="!$store.state.user" class="w-100 h-100 text-center d-flex flex-column justify-content-center align-items-center">
      <p>You are not logged in</p>
    </div>
    <div v-if="$store.state.user" class="col-12 col-md-6 text-start mt-3">
      <div class="d-flex flex-column align-items-center mb-5">
        <span class="material-icons" style="font-size: 100px">
          person
        </span>
        <p class="mt-2 fs-5"> {{ $store.state.user?.username }}  | {{ $store.state.user?.role }}</p>
      </div>
    </div>
    <div class="col-12 col-md-6 text-start mt-2" v-if="$store.state.user?.role == 'Buyer' ">
      <div class="d-flex flex-column align-items-center mb-5">
        <p class="fs-1 fw-bolder"> {{ $store.state.user?.deposit }}</p>
        <p> Current balance </p>
          <button type="button" class="btn btn-sm btn-outline-primary" @click="$store.dispatch('reset')">Reset</button>
      </div>
        <span class="mb-2">Deposit in your account</span>
        <select class="form-control mt-4" name="usertype" v-model="payload.amount">
          <option value="0" selected="selected" disabled>Select amount...</option>
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="20">20</option>
          <option value="50">50</option>
          <option value="100">100</option>
        </select>
        <button type="button" class="form-control btn btn-sm btn-outline-primary mt-3" @click="$store.dispatch('deposit', {payload})">Deposit</button>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
  components: {
  },
  data () {
    return {
      payload: {
        amount: 0,
      }
    }
  }
})
export default class MyAccount extends Vue {}

</script>

<style scoped>
.account {
    border: 1px solid blue;
}
</style>