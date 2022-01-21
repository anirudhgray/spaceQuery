<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Skeleload v-if="loading"></Skeleload>
    <Card class="card m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="r-700-invis lg:col-4 md:col-6">
            <img src="../assets/images/planet-with-no-star.jpg" />
          </div>
          <div class="md:col-4 lg:col-offset-2 md:col-offset-1 col-12 flex">
            <form
              class="flex flex-column my-auto w-full"
              @submit.prevent="resetForm"
            >
              <div class="field flex justify-content-between">
                <h1>Reset Password</h1>
              </div>

              <div class="field">
                <Password
                  v-model="newPass"
                  class="inputfield w-full"
                  inputClass="inputfield
                w-full"
                  toggleMask
                  :feedback="true"
                  placeholder="New Password"
                />
              </div>

              <div class="field">
                <Password
                  v-model="newPassRep"
                  class="inputfield w-full"
                  inputClass="inputfield
                w-full"
                  toggleMask
                  :feedback="false"
                  placeholder="Repeat New Password"
                />
              </div>

              <div v-if="!resetLoad" class="field">
                <Button type="submit" class="w-full" label="Reset"></Button>
              </div>
              <div v-else class="field">
                <Button class="w-full" icon="pi pi-spin pi-spinner"></Button>
              </div>

              <div v-if="success" class="field">
                <Button
                  class="w-full p-button-success"
                  label="Proceed to Log In"
                ></Button>
              </div>
            </form>
          </div>
        </div>
      </template>
    </Card>
    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Footer from '../components/Footer.vue'
import Skeleload from '../components/Skeleload.vue'
import Password from 'primevue/password'
import Button from 'primevue/button'
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'ForgotReset',
  components: {
    Footer,
    Card,
    Password,
    Button,
    Skeleload
  },
  data () {
    return {
      newPass: '',
      newPassRep: '',
      errors: [],
      success: false,
      id: '',
      token: '',
      loading: false,
      resetLoad: false
    }
  },
  mounted () {
    const urlParams = new URLSearchParams(window.location.search)
    this.id = urlParams.get('ID')
    this.token = urlParams.get('token')
    this.checkValidity()
  },
  methods: {
    checkValidity () {
      if (!this.id | !this.token) {
        this.$router.push('/')
      } else if (this.id.length !== 16 | this.token.length !== 16) {
        this.$router.push('/')
      }
    },
    async resetForm () {
      this.resetLoad = true
      this.errors = []
      this.success = false

      if (this.newPass.length < 8) {
        this.errors.push('The new password is too short.')
      }
      if (this.newPass !== this.newPassRep) {
        this.errors.push('The new passwords do not match.')
      }
      if (this.errors.length) {
        for (let i = 0; i < this.errors.length; i++) {
          this.$toast.add({ severity: 'error', summary: 'Oops.', detail: this.errors[i], life: 3000 })
        }
      }
      if (!this.errors.length) {
        const resetData = { newPass: this.newPass, id: this.id, token: this.token }
        await axios
          .post('/api/v1/users/actions/token-check/', resetData)
          .then(response => {
            this.success = true
            this.$toast.add({ severity: 'success', summary: 'Your password has been reset successfully. Please log in now.', detail: 'Yay.', life: 3000 })
            this.newPass = ''
            this.newPassRep = ''
          })
          .catch(error => {
            if (error.response) {
              console.log(error.response.data)
              this.$toast.add({ severity: 'error', summary: 'Error Response', detail: error.response.data, life: 3000 })
            } else if (error.message) {
              console.log(error)
              this.$toast.add({ severity: 'error', summary: 'Something went wrong.', detail: error, life: 3000 })
            }
          })
      }
      this.resetLoad = false
    }
  }
}
</script>
