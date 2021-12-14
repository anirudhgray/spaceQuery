<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Card class="col-8 col-offset-2 my-4 px-2">
      <template #header>
        <router-link class="link" to="/explore/external/"
          ><i class="pi pi-undo"></i> Back to all APIs</router-link
        >
      </template>
      <template #title>
        <h1>ISS Tracker</h1>
      </template>
      <template #subtitle>
        <p>
          Where is the ISS right now? Get coordinates and satellite imagery.
          Credit:
          <a href="https://github.com/open-notify">Open Notify</a>
        </p>
      </template>
      <template #content>
        <h2>TODO</h2>
      </template>
    </Card>
    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Footer from '../../components/Footer.vue'
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'AsteroidsNeoWs',
  components: {
    Footer,
    Navbar,
    Card
  }
}
</script>
