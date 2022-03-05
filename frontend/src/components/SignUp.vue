<template>
  <div class="d-flex flex-column align-items-center mb-5">
    <p class="fs-1">Sign up</p>
    <select class="form-control m-2 w-50" name="usertype" @change="changeUserType">
      <option value="0" selected="selected" disabled>Select user type...</option>
      <option value="Buyer">Buyer</option>
      <option value="Seller">Seller</option>
    </select>
    <input class="form-control m-2 w-50" type="text" placeholder="username" v-model="payload.username">
    <input class="form-control m-2 w-50" type="password" placeholder="password" v-model="payload.password">
    <input class="form-control m-2 w-50" type="password" placeholder="repeat password" v-model="payload.password2">
    <button type="button" class="btn btn-outline-danger w-50" @click="$store.dispatch('signUp', {payload})">
      <span>Sign Up</span>
    </button>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'

@Options({
  props: {
  },
  data () {
    return {
      payload: {
        type: 'Select user role'
      },
    }
  },
  methods: {
    changeUserType (event: any) {
      this.payload.role = event.target.value
    }
  }

})
export default class SignUp extends Vue {
}

</script>