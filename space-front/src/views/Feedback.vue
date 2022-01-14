<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Card class="card m-4 px-2">
      <template #content>
        <div class="grid tabcol">
          <div class="lg:col-7 col">
            <form @submit.prevent="submit" class="h-full flex flex-column">
              <div class="field">
                <h1>Feedback Toime</h1>
              </div>
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
                    disabled
                    required
                  />
                </div>
              </div>
              <div class="field">
                <Dropdown
                  :options="feedbackCats"
                  placeholder="Feedback Category"
                  required
                  v-model="category"
                />
              </div>
              <div class="field flex-grow-1">
                <Textarea
                  style="resize: none"
                  class="h-full w-full"
                  v-model="desc"
                  required
                />
              </div>
              <div class="field">
                <label for="slider"
                  >How would you rate your overall experience?</label
                >
                <Slider name="slider" v-model="rate" :step="10" required />
              </div>
              <div class="field">
                <Button v-if="!success" type="submit" label="Submit" />
                <Button v-else icon="pi pi-check" class="p-button-success" />
              </div>
            </form>
          </div>
          <div class="lg:col-5 col">
            <img src="../assets/images/feedback-humaaans.svg" />
          </div>
        </div>
      </template>
    </Card>
    <Message
      class="absolute bottom-0 right-0"
      :closable="false"
      severity="success"
      v-if="success"
    >
      Your feedback has been submitted successfully.
    </Message>
    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Footer from '../components/Footer.vue'
import Navbar from '../components/Navbar.vue'
import InputText from 'primevue/inputtext'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import Button from 'primevue/button'
import Slider from 'primevue/slider'
import axios from 'axios'
import Message from 'primevue/message'

export default {
  name: 'AsteroidsNeoWs',
  components: {
    Footer,
    Navbar,
    Card,
    InputText,
    Textarea,
    Dropdown,
    Button,
    Slider,
    Message
  },
  data () {
    return {
      feedbackCats: [
        'Bug',
        'New API',
        'Feature Request',
        'UI/UX',
        'Other'
      ],
      rate: 0,
      email: this.$store.state.user.email,
      category: null,
      desc: null,
      errors: [],
      success: false
    }
  },
  methods: {
    async submit () {
      if (!this.errors.length) {
        const data = { email: this.email, rate: this.rate, category: this.category, desc: this.desc }
        this.success = true
        this.rate = 0
        this.category = null
        this.desc = null
        await axios
          .post('/api/v1/users/actions/feedback/', data)
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
