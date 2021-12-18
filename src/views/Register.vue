<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="col-4">
            <img src="../assets/images/zombie_psr.jpg" />
          </div>
          <div class="col-4 col-offset-2 flex relative">
            <router-link to="/"
              ><Button
                class="absolute top-0 mt-8 p-button-text p-button-rounded"
                icon="pi pi-undo"
              ></Button
            ></router-link>
            <form
              class="flex flex-column my-auto w-full"
              @submit.prevent="submitRegisterForm"
            >
              <div class="field align-self-end">
                <h1>Register</h1>
              </div>

              <div class="field">
                <div class="p-inputgroup">
                  <span class="p-inputgroup-addon">
                    <i class="pi pi-user"></i>
                  </span>
                  <InputText
                    id="login-email"
                    type="email"
                    v-model="email"
                    class="inputfield w-full"
                    placeholder="Email"
                  />
                </div>
              </div>

              <div class="field">
                <Password
                  id="login-pwd"
                  v-model="password"
                  class="inputfield w-full"
                  inputClass="inputfield w-full"
                  toggleMask
                  placeholder="Password"
                >
                </Password>
              </div>

              <div class="field">
                <Password
                  id="login-pwd-repeat"
                  v-model="password2"
                  class="inputfield w-full"
                  inputClass="inputfield w-full"
                  toggleMask
                  :feedback="false"
                  placeholder="Repeat Password"
                >
                </Password>
              </div>

              <div class="field">
                <Button type="submit" class="w-full" label="Register"></Button>
              </div>

              <div class="field mt-auto mb-0 align-self-end">
                <p class="text-right">
                  Already have an account?
                  <router-link to="/login">
                    <Button label="Log in." class="p-button-text p-0"></Button>
                  </router-link>
                </p>
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
              <p>Account created successfully. You can log in now.</p>
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
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'AsteroidsNeoWs',
  components: {
    Footer,
    Card,
    InputText,
    Button,
    Password,
    Message
  },
  data () {
    return {
      email: '',
      password: '',
      password2: '',
      errors: [],
      success: false
    }
  },
  mounted () {
    this.checkUser()
  },
  methods: {
    checkUser () {
      if (this.$store.state.isAuthenticated) {
        console.log('ok')
        this.$router.push({ path: '/user/you' })
      }
    },
    async submitRegisterForm () {
      this.errors = []
      this.success = false

      if (this.email === '') {
        this.errors.push('The email is missing.')
      }
      if (this.password.length < 8) {
        this.errors.push('The password is too short.')
      }
      if (this.password !== this.password2) {
        this.errors.push('The passwords do not match.')
      }

      if (!this.errors.length) {
        const formData = {
          email: this.email,
          password: this.password
        }
        this.email = ''
        this.password = ''
        this.password2 = ''

        await axios
          .post('/api/v1/users/auths/', formData)
          .then(response => {
            this.success = true
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else if (error.message) {
              this.errors.push('Something went wrong.' + error)
            }
          })
      }
    }
  }
}

</script>
