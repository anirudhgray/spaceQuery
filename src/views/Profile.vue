<template>
  <div class="grey flex flex-column">
    <div class="grid justify-content-between mt-4 mx-4">
      <nav>
        <router-link class="mx-2" to="/">Landing</router-link>
        <router-link class="mx-2" to="/profile/you">Your Profile</router-link>
        <router-link class="mx-2" to="#">Explore APIs</router-link>
        <router-link class="mx-2" to="#">Internal Content</router-link>
        <router-link class="mx-2" to="#">Search Users</router-link>
      </nav>
      <Button @click="logout" class="p-button-danger" label="Log Out"></Button>
    </div>
    <div class="h-auto overflow-auto">
      <Card class="m-4">
        <template #title>
          <h1>{{ $store.state.user.email }}</h1>
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
          <Button
            v-if="!edit"
            class="p-button-text"
            label="Edit Profile"
            icon="pi pi-user-edit"
            @click="toggleEdit"
          ></Button>
          <Button
            v-else
            class="p-button-text"
            label="Confirm"
            icon="pi pi-check"
            @click="confirmEdit($store.state.user.id)"
          ></Button>
        </template>
      </Card>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Button from 'primevue/button'
import Card from 'primevue/card'
import Footer from '../components/Footer.vue'
import InputText from 'primevue/inputtext'
import axios from 'axios'

export default {
  name: 'Profile',
  data () {
    return {
      firstname: 'nil',
      lastname: 'nil',
      github: 'nil',
      saved: 'nil',
      queries: 'nil',
      edit: false
    }
  },
  components: {
    Button,
    Footer,
    Card,
    InputText
  },
  mounted () {
    this.fetchProfile(this.$store.state.user.id)
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
    logout () {
      this.$store.dispatch('logout')
    },
    async fetchProfile (userid) {
      await axios
        .get(`/api/v1/users/profiles/${userid}/`)
        .then(response => {
          this.firstname = response.data.first_name
          this.lastname = response.data.last_name
          this.github = response.data.github_username
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
