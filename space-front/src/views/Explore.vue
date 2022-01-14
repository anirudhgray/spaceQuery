<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Skeleload v-if="pageLoad"></Skeleload>
    <div class="grid grid-nogutter justify-content-evenly m-4">
      <Card
        data-aos="fade-up"
        data-aos-offset="-900"
        v-for="(api, i) in apiDetails"
        :key="i"
        class="m-2 px-2 -pb-1 result-card"
      >
        <template #header>
          <Image
            :alt="api.name"
            :src="require(`@/assets/images/${api.image}`)"
            preview
          />
        </template>
        <template #title>
          <router-link class="link" :to="'/explore/external/' + api.url_name">{{
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
import Skeleload from '../components/Skeleload.vue'
import Image from 'primevue/image'
import Card from 'primevue/card'

import axios from 'axios'

export default {
  name: 'Explore',
  data () {
    return {
      apiDetails: [
      ],
      pageLoad: false
    }
  },
  components: {
    Footer,
    Navbar,
    Card,
    Image,
    Skeleload
  },
  mounted () {
    this.fetchAPIS()
  },
  methods: {
    async fetchAPIS () {
      this.pageLoad = true
      await axios
        .get('/api/v1/externals/')
        .then(response => {
          this.apiDetails = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.pageLoad = false
    }
  }
}
</script>
