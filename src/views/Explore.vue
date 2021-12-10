<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <div class="grid grid-nogutter justify-content-evenly m-4">
      <Card
        v-for="(api, i) in apiDetails"
        :key="i"
        class="m-2 px-2 -pb-1 result-card"
      >
        <template #header>
          <Image
            :alt="api.name"
            :src="api.image"
            class="card-header-imgs"
            preview
          />
        </template>
        <template #title>
          <router-link :to="'/explore/external/' + api.url_name">{{
            api.name
          }}</router-link>
        </template>
        <template #content>
          {{ api.description }}
        </template>
        <template #footer>
          <a :href="api.link">{{ api.credit }}</a>
        </template>
      </Card>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from '../components/Footer.vue'
import Navbar from '../components/Navbar.vue'
import Image from 'primevue/image'
import Card from 'primevue/card'

import axios from 'axios'

export default {
  name: 'Explore',
  data () {
    return {
      apiDetails: [
      ]
    }
  },
  components: {
    Footer,
    Navbar,
    Card,
    Image
  },
  mounted () {
    this.fetchAPIS()
  },
  methods: {
    async fetchAPIS () {
      await axios
        .get('/api/v1/externals/')
        .then(response => {
          this.apiDetails = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
