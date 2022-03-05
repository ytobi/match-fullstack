<template>
  <div class="d-flex flex-column align-items-center mb-5">
    <p class="fs-1">Sign In</p>
    <input class="form-control m-2 w-50" type="text" placeholder="username" v-model="payload.username">
    <input class="form-control m-2 w-50" type="password" placeholder="password" v-model="payload.password">
    <button type="button" class="btn btn-outline-danger w-50" @click="requsting=true; $store.dispatch('signIn', {payload})">
      <span v-show="requsting">
        <div class="spinner-border spinner-border-sm text-danger me-3" role="status">
          <span class="visually-hidden">Loading...</span>
        </div>
      </span>
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
      requsting: false,
      payload: {
      },
    }
  },

})
export default class SignIn extends Vue {
}

</script>