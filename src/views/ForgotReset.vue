<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Skeleload v-if="loading"></Skeleload>
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="r-700-invis lg:col-4 md:col-6">
            <img src="../assets/images/roasted_planet.jpg" />
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

              <div class="field">
                <Button type="submit" class="w-full" label="Reset"></Button>
              </div>
            </form>

            <Message
              class="absolute bottom-0 right-0"
              :closable="false"
              severity="error"
              v-if="errors.length"
            >
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </Message>

            <Message
              class="absolute bottom-0 right-0"
              :closable="false"
              severity="success"
              v-if="success"
            >
              <p>
                Your password has been reset successfully. Please
                <router-link to="/login">log in</router-link>
              </p>
            </Message>
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
import Message from 'primevue/message'
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'ResetPassword',
  components: {
    Footer,
    Card,
    Password,
    Button,
    Message,
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
      loading: false
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
      this.errors = []
      this.success = false

      if (this.newPass.length < 8) {
        this.errors.push('The new password is too short.')
      }
      if (this.newPass !== this.newPassRep) {
        this.errors.push('The new passwords do not match.')
      }
      if (!this.errors.length) {
        const resetData = { newPass: this.newPass, id: this.id, token: this.token }
        await axios
          .post('/api/v1/users/actions/token-check/', resetData)
          .then(response => {
            this.success = true
            this.newPass = ''
            this.newPassRep = ''
          })
          .catch(error => {
            if (error.response) {
              this.errors.push(error.response.data)
            } else if (error.message) {
              this.errors.push('Something went wrong.' + error)
            }
          })
      }
    }
  }
}
</script>
