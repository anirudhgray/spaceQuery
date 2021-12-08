<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <div class="h-auto overflow-auto">
      <form @submit.prevent="confirmEdit($store.state.user.id)">
        <Card class="m-4">
          <template #title>
            <Avatar size="xlarge" icon="pi pi-user"></Avatar>
            <h1>{{ email }}</h1>
          </template>
          <template #content>
            <div v-if="!edit">
              <p>First name: {{ firstname }}</p>
              <p>Last name: {{ lastname }}</p>
              <p>Github: {{ github }}</p>
              <p>Saved results: {{ saved }}</p>
              <p>Queries made: {{ queries }}</p>
            </div>
            <div v-else>
              <div class="field">
                <InputText placeholder="Firstname" v-model="firstname" />
              </div>
              <div class="field">
                <InputText placeholder="Lastname" v-model="lastname" />
              </div>
              <div class="field">
                <InputText placeholder="Github" v-model="github" />
              </div>
              <p>Saved results: {{ saved }}</p>
              <p>Queries made: {{ queries }}</p>
            </div>
          </template>
          <template #footer>
            <div v-if="this.$route.params.id === 'you'">
              <Button
                v-if="!edit"
                class="p-button-text"
                label="Edit Profile"
                icon="pi pi-user-edit"
                @click="toggleEdit"
              ></Button>
              <Button
                v-else
                type="submit"
                class="p-button-text"
                label="Confirm"
                icon="pi pi-check"
              ></Button>
            </div>
          </template>
        </Card>
      </form>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Button from 'primevue/button'
import Card from 'primevue/card'
import Footer from '../components/Footer.vue'
import InputText from 'primevue/inputtext'
import Navbar from '../components/Navbar.vue'
import Avatar from 'primevue/avatar'
import axios from 'axios'

export default {
  name: 'Profile',
  data () {
    return {
      email: '',
      pfp: '',
      firstname: '-',
      lastname: '-',
      github: '-',
      saved: '-',
      queries: '-',
      edit: false
    }
  },
  components: {
    Button,
    Footer,
    Card,
    InputText,
    Navbar,
    Avatar
  },
  mounted () {
    if (this.$route.params.id === 'you') {
      this.fetchProfile(this.$store.state.user.id)
    } else {
      this.fetchProfile(this.$route.params.id)
    }
  },
  methods: {
    toggleEdit () {
      this.edit = !this.edit
    },
    async confirmEdit (userid) {
      await axios
        .patch(`/api/v1/users/profiles/${userid}/`, { first_name: this.firstname, last_name: this.lastname, github_username: this.github })
        .then(() => {
          this.toggleEdit()
        })
    },
    async fetchProfile (userid) {
      await axios
        .get(`/api/v1/users/profiles/${userid}/`)
        .then(response => {
          this.email = response.data.email
          if (response.data.first_name !== '') {
            this.firstname = response.data.first_name
          }
          if (response.data.last_name !== '') {
            this.lastname = response.data.last_name
          }
          if (response.data.github_username !== '') {
            this.github = response.data.github_username
          }
          this.saved = response.data.saved_results
          this.queries = response.data.queries_made
        })
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }
}
</script>
