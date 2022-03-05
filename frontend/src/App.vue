<template>
  <div class="row m-0 d-flex flex-column justify-content-center align-items-center" style="height: 100vh" >
    <div style="height: 700px; max-height: 100vh; max-width: 740px;">
      <div class="row m-0" >
        <div class="d-flex" style="margin: 0 auto;" >
          <NavBar />
        </div>
        <ToastNotification/>
      </div>
      <div class="row m-0">
        <div class="d-flex" style="margin: 0 auto; min-height: 400px">
          <router-view/>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">

import NavBar from '@/components/NavBar.vue'

export default {
  components: {
    NavBar,
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  /* padding: 30px; */
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
