<template>
  <Button @click="logout" class="p-button-danger" label="Log Out"></Button>
  <Footer></Footer>
</template>

<script>
import Button from 'primevue/button'
import Footer from '../components/Footer.vue'
import axios from 'axios'

export default {
  name: 'Profile',
  components: {
    Button,
    Footer
  },
  methods: {
    async logout () {
      await axios
        .get('/api/v1/users/logout/')
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      this.$store.commit('removeToken')

      this.$router.push('/')
    }
  }
}
</script>
