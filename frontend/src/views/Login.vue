<template>
  <div class="login w-100 h-100">
    <div v-if="toggle">
      <SignIn />
      <div class="mt-2">
          <span>Do not have an account?</span>
          <span class="text-primary" @click="toggleLogin" style="cursor: pointer" > Sign Up </span>
        </div>
    </div>
    <div v-else>
     <SignUp  />
      <div class="">
          <span>Already have an account?</span>
          <span class="text-primary" @click="toggleLogin" style="cursor: pointer" > Sign In </span>
        </div>
    </div>
  </div>
</template>

<script lang="ts">

import { Options, Vue } from 'vue-class-component'
import SignUp from '@/components/SignUp.vue'
import SignIn from '@/components/SignIn.vue'

@Options({
  components: {
    SignUp,
    SignIn
  },
  data () {
    return {
      toggle: true,
    }
  },
  methods: {
    toggleLogin () {
      this.toggle = !this.toggle
    }
  }
})
export default class Login extends Vue {}

</script>

<style scoped>
.login {
    border: 1px solid red;
}
</style>
