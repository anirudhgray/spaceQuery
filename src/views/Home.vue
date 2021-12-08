<template>
  <div class="grey">
    <div
      class="
        h-screen
        flex flex-column
        justify-content-evenly
        align-items-center
      "
    >
      <h1 class="text-8xl text-center">spaceQuery</h1>
      <div class="flex flex-column align-items-center">
        <div class="grid">
          <Button class="mx-2" label="Log in" />
          <Button class="mx-2" label="Learn more" />
          <Button class="mx-2" label="Github" />
        </div>
        <p class="mt-8">Powered by the NASA open APIs.</p>
      </div>
    </div>

    <div class="h-auto overflow-auto">
      <Card class="col-8 col-offset-2 mb-8 h-auto text-center p-5">
        <template #title>
          <h2>So, how does this work?</h2>
        </template>
        <template #subtitle>
          <p>Very well, then.</p>
        </template>
        <template #content>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Pellentesque id cursus tortor. Donec congue lobortis ante, nec
            maximus ex faucibus vitae. Nunc nec sodales risus. Curabitur
            volutpat, erat eu facilisis scelerisque, metus turpis iaculis erat,
            vel egestas dolor nisl at lorem. Donec id quam tellus.
          </p>
          <img
            class="my-4 col-8 col-offset-2"
            src="https://picsum.photos/600/400"
          />
          <p>
            Donec imperdiet lacinia erat, non sodales erat posuere placerat.
            Class aptent taciti sociosqu ad litora torquent per conubia nostra,
            per inceptos himenaeos. Nullam urna quam, cursus in ultrices ut,
            vulputate non ex.
          </p>
        </template>
        <template #footer>
          <p>A-ha!</p>
        </template>
      </Card>
    </div>

    <div v-if="!$store.state.isAuthenticated" class="h-auto overflow-auto">
      <Card v-if="logFlipped" class="col-8 col-offset-2 mb-8 h-auto p-5">
        <template #content>
          <div class="grid">
            <form
              class="col-6 flex flex-column"
              @submit.prevent="submitRegisterForm"
            >
              <h3 class="text-5xl mb-4">Register</h3>

              <div class="field">
                <div class="p-inputgroup">
                  <span class="p-inputgroup-addon">
                    <i class="pi pi-user"></i>
                  </span>
                  <InputText
                    id="reg-email"
                    type="email"
                    v-model="email"
                    class="inputfield w-full"
                    placeholder="Email"
                  />
                </div>
              </div>

              <div class="field">
                <Password
                  id="reg-pwd"
                  type="password"
                  v-model="password"
                  class="inputfield w-full"
                  inputClass="inputfield w-full"
                  toggleMask
                  placeholder="Password"
                />
              </div>

              <div class="field">
                <Password
                  id="reg-pwd-rep"
                  type="password"
                  v-model="password2"
                  class="inputfield w-full"
                  inputClass="inputfield w-full"
                  toggleMask
                  :feedback="false"
                  placeholder="Repeat Password"
                />
              </div>

              <Message :closable="false" severity="error" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </Message>
              <Message :closable="false" severity="success" v-if="success">
                <p>Account created successfully. You can log in now.</p>
              </Message>

              <div class="field">
                <Button type="submit" label="Register" class="w-full"></Button>
              </div>

              <div class="field mt-auto mb-0">
                <p>
                  Already have an account?
                  <Button
                    @click="flip"
                    class="p-button-text pb-0"
                    label="Log in."
                  ></Button>
                </p>
              </div>
            </form>
            <img src="https://picsum.photos/400/550" class="col-6" />
          </div>
        </template>
      </Card>

      <Card v-else class="col-8 col-offset-2 mb-8 h-auto p-5">
        <template #content>
          <div class="grid">
            <img src="https://picsum.photos/400/550" class="col-6" />
            <form
              class="col-6 flex flex-column"
              @submit.prevent="submitLoginForm"
            >
              <h3 class="text-5xl text-right mb-4">Log In</h3>

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
                  type="password"
                  v-model="password"
                  class="inputfield w-full"
                  inputClass="inputfield w-full"
                  toggleMask
                  :feedback="false"
                  placeholder="Password"
                >
                </Password>
              </div>

              <Message :closable="false" severity="error" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
              </Message>

              <div class="field">
                <Button type="submit" label="Log In" class="w-full"></Button>
              </div>

              <div class="field mt-auto mb-0">
                <p>
                  Logging in is necessary to use this web app. Don't have an
                  account?
                  <Button
                    @click="flip"
                    label="Register here."
                    class="p-button-text pb-0"
                  ></Button>
                </p>
              </div>
            </form>
          </div>
        </template>
      </Card>
    </div>

    <div v-else>
      <Card class="col-8 col-offset-2 mb-8 h-auto p-5">
        <template #title>
          <h3 class="text-5xl text-right mb-4">You are already logged in.</h3>
        </template>
        <template #content>
          <p class="text-right">As {{ $store.state.user.email }}</p>
        </template>
        <template #footer>
          <div class="p-buttonset">
            <Button
              @click="logout"
              label="Log out"
              class="p-button-danger col-6"
            ></Button>
            <router-link to="/profile/you"
              ><Button label="Enter" class="p-button-success col-6"></Button
            ></router-link>
          </div>
        </template>
      </Card>
    </div>

    <div class="h-auto overflow-auto">
      <img
        src="https://picsum.photos/1000/500"
        class="col-8 col-offset-2 no-pad"
      />
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Button from 'primevue/button'
import Footer from '../components/Footer.vue'
import Message from 'primevue/message'
import Password from 'primevue/password'
import InputText from 'primevue/inputtext'
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'Home',
  components: {
    Card,
    Button,
    Footer,
    Message,
    Password,
    InputText
  },
  data () {
    return {
      logFlipped: false,
      email: '',
      password: '',
      password2: '',
      errors: [],
      success: false,
      curr: ''
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
    },
    flip () {
      this.logFlipped = !this.logFlipped
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

            this.$router.push('/profile/you')
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
}
</script>
