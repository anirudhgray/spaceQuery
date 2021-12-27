<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="col-4">
            <img src="../assets/images/roasted_planet.jpg" />
          </div>
          <div class="col-4 col-offset-2 flex relative">
            <router-link to="/user/you"
              ><Button
                class="absolute top-0 mt-8 p-button-text p-button-rounded"
                icon="pi pi-undo"
                label="Back to profile"
              ></Button
            ></router-link>
            <form
              class="flex flex-column my-auto w-full"
              @submit.prevent="resetForm"
            >
              <div class="field align-self-end">
                <h1>Reset Password</h1>
              </div>

              <div class="field">
                <Password
                  v-model="oldPass"
                  class="inputfield w-full"
                  inputClass="inputfield
                w-full"
                  toggleMask
                  :feedback="false"
                  placeholder="Old Password"
                />
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
                <Button type="submit" class="w-full" label="Send"></Button>
              </div>
            </form>

            <Message
              class="absolute bottom-0 right-0 left-0"
              :closable="false"
              severity="error"
              v-if="errors.length"
            >
              <p v-for="error in errors" :key="error">{{ error }}</p>
            </Message>

            <Message
              class="absolute bottom-0 right-0 left-0"
              :closable="false"
              severity="success"
              v-if="success"
            >
              <p>Your password has been reset successfully.</p>
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
    Message
  },
  data () {
    return {
      oldPass: '',
      newPass: '',
      newPassRep: '',
      errors: [],
      success: false
    }
  },
  methods: {
    async resetForm () {
      this.errors = []
      this.success = false

      if (!this.$store.state.isAuthenticated) {
        this.errors.push('You are not logged in.')
      }
      if (this.oldPass === '') {
        this.errors.push('The old password is missing.')
      }
      if (this.newPass.length < 8) {
        this.errors.push('The new password is too short.')
      }
      if (this.newPass !== this.newPassRep) {
        this.errors.push('The new passwords do not match.')
      }

      if (!this.errors.length) {
        const resetData = { oldPass: this.oldPass, newPass: this.newPass }
        await axios
          .post('/api/v1/users/actions/reset/', resetData)
          .then(response => {
            this.success = true
            this.oldPass = ''
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
