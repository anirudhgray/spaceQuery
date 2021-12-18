<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="col-4">
            <img src="../assets/images/rains_of_terror.jpg" />
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
              @submit.prevent="submitLoginForm"
            >
              <div class="field align-self-end">
                <h1>Log In</h1>
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
                  :feedback="false"
                  placeholder="Password"
                >
                </Password>
              </div>

              <div class="field">
                <Button type="submit" class="w-full" label="Log In"></Button>
              </div>

              <router-link class="ml-auto" to="/forgot-password"
                ><Button class="p-button-text p-0"
                  >Forgot Password?</Button
                ></router-link
              >
              <p class="my-2 mx-auto">or</p>

              <div class="field">
                <Button class="w-full github-button"
                  ><p class="mx-auto">
                    <i class="pi pi-github mr-2"></i> Log in with GitHub
                  </p></Button
                >
              </div>

              <div class="field mt-auto mb-0 align-self-end">
                <p class="text-right">
                  Logging in is necessary to use this web app. Don't have an
                  account?
                  <router-link to="/register">
                    <Button
                      label="Register here."
                      class="p-button-text p-0"
                    ></Button>
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
    async submitLoginForm () {
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')

      this.errors = []
      this.success = false

      if (this.email === '') {
        this.errors.push('The email is missing.')
      }
      if (this.password.length < 8) {
        this.errors.push('The password is too short.')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.email,
          password: this.password
        }

        await axios
          .post('/api-token-auth/', formData)
          .then(response => {
            const token = response.data.token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common.Authorization = 'Token ' + token
            localStorage.setItem('token', token)
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

        await axios
          .get('/api/v1/users/me')
          .then(response => {
            this.$store.commit('setUser', { id: response.data[0].id, email: response.data[0].email })
            localStorage.setItem('email', response.data[0].email)
            localStorage.setItem('userid', response.data[0].id)

            this.$router.push('/user/you')
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
}
</script>
