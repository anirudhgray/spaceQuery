<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <div class="my-8 flex flex-column">
      <img class="w-4 mx-auto" src="../assets/images/space-error.png" />
      <h1 class="mx-auto">You seem lost.</h1>
      <router-link class="mx-auto" to="/"
        ><Button label="Head Home"
      /></router-link>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from '../components/Footer.vue'
import Navbar from '../components/Navbar.vue'
import Button from 'primevue/button'

export default {
  name: 'NotFound404',
  components: {
    Footer,
    Navbar,
    Button
  }
}
</script>
