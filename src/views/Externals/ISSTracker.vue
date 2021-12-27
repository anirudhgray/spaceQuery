<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Skeleload v-if="pageLoad"></Skeleload>
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
          NOTE: SECURE THE API KEY FOR THIS
          https://www.freecodecamp.org/news/private-api-keys/ Where is the ISS
          right now? Get coordinates and satellite imagery. Credit:
          <a href="https://github.com/open-notify">Open Notify</a>
        </p>
      </template>
      <template #content>
        <h2>Longitude</h2>
        <p>{{ longitude }}</p>
        <h2>Latitude</h2>
        <p>{{ latitude }}</p>
        <h2>Timezone</h2>
        <p>{{ timezone }}</p>
        <p>{{ time_offset }} UTC</p>
        <h2>Country Code</h2>
        <p>{{ country_code }}</p>
        <h2>Map</h2>
        <iframe
          class="w-full h-30rem"
          loading="lazy"
          allowfullscreen
          :src="map_url"
        ></iframe>
      </template>
      <template #footer>
        <Button label="Poll Again" class="w-full" @click="getISS" />
      </template>
    </Card>
    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Button from 'primevue/button'
import Footer from '../../components/Footer.vue'
import Navbar from '../../components/Navbar.vue'
import Skeleload from '../../components/Skeleload.vue'
import axios from 'axios'

export default {
  name: 'AsteroidsNeoWs',
  components: {
    Footer,
    Navbar,
    Card,
    Skeleload,
    Button
  },
  data () {
    return {
      longitude: null,
      latitude: null,
      timestamp: null,
      timezone: null,
      time_offset: null,
      country_code: null,
      map_url: null,
      pageLoad: false
    }
  },
  mounted () {
    this.getISS()
  },
  methods: {
    async getISS () {
      this.pageLoad = true
      await axios
        .get('https://cors-anywhere.herokuapp.com/https://api.wheretheiss.at/v1/satellites/25544')
        .then(response => {
          this.longitude = response.data.longitude
          this.latitude = response.data.latitude
          this.timestamp = response.data.timestamp
        })
        .catch(error => {
          console.log(error)
        })
      await axios
        .get(`https://cors-anywhere.herokuapp.com/https://api.wheretheiss.at/v1/coordinates/${this.latitude},${this.longitude}`)
        .then(response => {
          this.timezone = response.data.timezone_id
          this.time_offset = response.data.offset
          this.country_code = response.data.country_code
          this.map_url = `https://www.google.com/maps/embed/v1/search?q=${this.latitude},${this.longitude}&key=AIzaSyCeK3RSCp2QXCWOLzTYrUuG8sncd0dheME`
        })
        .catch(error => {
          console.log(error)
        })
      this.pageLoad = false
    }
  }
}
</script>
