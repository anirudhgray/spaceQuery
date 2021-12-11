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

    <div>
      <div class="flex flex-column align-items-center">
        <Button
          v-if="this.$route.params.id === 'you' && !historyToggle"
          class="mb-4"
          label="Show History"
          @click="getHistory"
        />
        <Button
          v-if="this.$route.params.id === 'you' && historyToggle"
          class="mb-4"
          label="Hide History"
          @click="hideHistory"
        />
        <i v-if="historyLoad" class="pi pi-spin pi-spinner text-4xl mb-2"></i>
      </div>
      <div v-if="historyToggle">
        <h2 class="text-center">History</h2>
        <div class="grid justify-content-evenly mx-4 my-4">
          <Card
            v-for="historyItem in historyDisplays"
            :key="historyItem.id"
            class="relative col-12 md:col-5 lg:col-3 mb-4 md:mb-0 darker-card"
          >
            <template #title>
              <h2>{{ historyItem.title }}</h2>
            </template>
            <template #subtitle>
              <p>{{ historyItem.search_time }}</p>
            </template>
            <template #content>
              <p
                v-for="(item, j) in Object.keys(JSON.parse(historyItem.info))"
                :key="j"
              >
                {{ item }}: {{ JSON.parse(historyItem.info)[item] }}
              </p>
            </template>
          </Card>
        </div>
      </div>

      <div>
        <h2 class="text-center">Saved Results</h2>
        <div class="grid justify-content-evenly mx-4 my-4">
          <Card
            v-for="(save, i) in saveDisplays"
            class="relative col-12 md:col-5 lg:col-3 mb-4 md:mb-0"
            :key="save.id"
          >
            <template #title>
              <h2>{{ save.title }}</h2>
            </template>
            <template #content>
              <img :src="JSON.parse(save.info).image" />
              <p
                v-for="(item, j) in Object.keys(JSON.parse(save.info).text)"
                :key="j"
              >
                {{ item }}: {{ JSON.parse(save.info).text[item] }}
              </p>
            </template>
            <template #footer>
              <Button
                v-if="this.$route.params.id === 'you'"
                icon="pi pi-trash"
                class="absolute right-0 bottom-0 mr-4 mb-4"
                @click="removeSaved(save.id, i)"
              />
            </template>
          </Card>
        </div>
      </div>
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
      edit: false,
      saveDisplays: [],
      historyDisplays: [],
      historyToggle: false,
      historyLoad: false
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
    hideHistory () {
      this.historyToggle = false
    },
    async getHistory () {
      this.historyToggle = true
      this.historyLoad = true
      await axios
        .get('api/v1/history/')
        .then(response => {
          this.historyDisplays = response.data.reverse()
          this.historyLoad = false
        })
        .catch(error => {
          console.log(error)
        })
    },
    async removeSaved (id, index) {
      this.saveDisplays.splice(index, 1)
      await axios
        .delete(`/api/v1/saves/${id}`)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },
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
        .all([
          axios
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
            }),
          axios
            .get(`/api/v1/saves/?search=${userid}`)
            .then(response => {
              this.saveDisplays = response.data
            })
        ])
        .catch(error => {
          console.log(JSON.stringify(error))
        })
    }
  }
}
</script>
