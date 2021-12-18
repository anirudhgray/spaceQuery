<template>
  <div class="grey flex flex-column">
    <router-link class="landing-link w-min ml-4 mt-3" to="/"
      >spaceQuery</router-link
    >
    <Card class="m-4 px-2">
      <template #content>
        <div class="grid">
          <div class="col-4">
            <img src="../assets/images/flares_of_fury.jpg" />
          </div>
          <div class="col-4 col-offset-2 flex relative">
            <router-link to="/login"
              ><Button
                class="absolute top-0 mt-8 p-button-text p-button-rounded"
                icon="pi pi-undo"
                label="Back to login"
              ></Button
            ></router-link>
            <form class="flex flex-column my-auto w-full">
              <div class="field align-self-end">
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
    }
  }
}
</script>
