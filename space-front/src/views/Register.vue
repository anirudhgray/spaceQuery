<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="card m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="r-700-invis lg:col-4 md:col-6">
            <img src="../assets/images/zombie_psr.jpg" />
          </div>
          <div class="md:col-4 lg:col-offset-2 md:col-offset-1 col-12 flex">
            <form
              class="flex flex-column my-auto w-full"
              @submit.prevent="submitRegisterForm"
            >
              <div class="field flex justify-content-between">
                <router-link to="/"
                  ><Button
                    class="p-button-text p-button-rounded"
                    icon="pi pi-undo"
                  ></Button
                ></router-link>
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

              <div v-if="!regLoad" class="field">
                <Button type="submit" class="w-full" label="Register"></Button>
              </div>
              <div v-else class="field">
                <Button class="w-full" icon="pi pi-spin pi-spinner"></Button>
              </div>

              <p class="my-2 mx-auto">or</p>

              <div class="field">
                <Button @click="notImplemented" class="w-full github-button"
                  ><p class="mx-auto">
                    <i class="pi pi-github mr-2"></i> Register with GitHub
                  </p></Button
                >
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
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'Register',
  components: {
    Footer,
    Card,
    InputText,
    Button,
    Password
  },
  data () {
    return {
      email: '',
      password: '',
      password2: '',
      errors: [],
      success: false,
      regLoad: false
    }
  },
  mounted () {
    this.checkUser()
  },
  methods: {
    notImplemented () {
      this.$toast.add({ severity: 'error', summary: 'Not implemented yet.', detail: 'What a lazy dev...', life: 3000 })
    },
    checkUser () {
      if (this.$store.state.isAuthenticated) {
        console.log('ok')
        this.$router.push({ path: '/user/you' })
      }
    },
    async submitRegisterForm () {
      this.regLoad = true
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
      if (this.errors.length) {
        for (let i = 0; i < this.errors.length; i++) {
          this.$toast.add({ severity: 'error', summary: 'Oops.', detail: this.errors[i], life: 3000 })
        }
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
            this.$toast.add({ severity: 'success', summary: 'Account created successfully.', detail: 'You can log in now.', life: 3000 })
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                console.log(`${property}: ${error.response.data[property]}`)
                this.$toast.add({ severity: 'error', summary: property, detail: error.response.data[property], life: 3000 })
              }
            } else if (error.message) {
              console.log(error)
              this.$toast.add({ severity: 'error', summary: 'Something went wrong.', detail: error, life: 3000 })
            }
          })
      }
      this.regLoad = false
    }
  }
}

</script>
