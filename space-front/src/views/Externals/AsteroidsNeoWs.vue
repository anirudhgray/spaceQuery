<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Card class="card md:col-8 md:col-offset-2 my-4 px-2">
      <template #header>
        <router-link class="link" to="/explore/external/"
          ><i class="pi pi-undo"></i> Back to all APIs</router-link
        >
      </template>
      <template #title>
        <h1>Asteroids — NeoWs</h1>
      </template>
      <template #subtitle>
        <p>
          Near Earth Object Web Service. Credit:
          <a
            target="_blank"
            rel="noopener"
            href="https://github.com/SpaceRocks/"
            >The SpaceRocks Team</a
          >
        </p>
      </template>
      <template #content>
        <h2>TODO</h2>
        <img
          src="../../assets/images/space-page-under-construction.png"
          class="md:col-4 md:col-offset-4 no-pad"
        />
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
  },
  mounted () {
    this.notImplemented()
  },
  methods: {
    notImplemented () {
      this.$toast.add({ severity: 'error', summary: 'Not implemented yet.', detail: 'What a lazy dev...', life: 3000 })
    }
  }
}
</script>
