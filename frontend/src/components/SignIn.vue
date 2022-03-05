<template>
  <div class="d-flex flex-column align-items-center mb-5">
    <p class="fs-1">Sign In</p>
    <input class="form-control m-2 w-50" type="text" placeholder="username" v-model="payload.username">
    <input class="form-control m-2 w-50" type="password" placeholder="password" v-model="payload.password">
    <button type="button" class="btn btn-outline-danger w-50" @click="$store.dispatch('signIn', {payload})">
      <span>Sign In</span>
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
      },
    }
  },

})
export default class SignIn extends Vue {
}

</script>