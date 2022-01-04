<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="r-700-invis lg:col-4 md:col-6">
            <img src="../assets/images/flares_of_fury.jpg" />
          </div>
          <div class="md:col-4 lg:col-offset-2 md:col-offset-1 col-12 flex">
            <form
              @submit.prevent="forgot"
              class="flex flex-column my-auto w-full"
            >
              <div class="field flex justify-content-between">
                <router-link to="/login"
                  ><Button
                    class="p-button-text p-button-rounded"
                    icon="pi pi-undo"
                    label="Back to login"
                  ></Button
                ></router-link>
                <h1>Forgot Password</h1>
              </div>

              <div class="field">
                <p class="text-right">
                  We will send a reset link to your registered email address.
                </p>
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
                <Button type="submit" class="w-full" label="Send"></Button>
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
              Please check your inbox for the reset link.
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
import Button from 'primevue/button'
import Message from 'primevue/message'
import axios from 'axios'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  name: 'ForgotPassword',
  components: {
    Footer,
    Card,
    InputText,
    Button,
    Message
  },
  data () {
    return {
      email: '',
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
    async forgot () {
      const forgotData = { email: this.email }
      this.success = true
      this.email = ''
      await axios
        .post('/api/v1/users/actions/forgot/', forgotData)
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
</script>
