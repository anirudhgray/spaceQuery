<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Skeleload v-if="pageLoad"></Skeleload>
    <div class="h-auto overflow-auto">
      <form @submit.prevent="confirmEdit($store.state.user.id)">
        <Card class="card m-4">
          <template #content>
            <div class="grid tabcol">
              <div class="lg:col-3 col relative">
                <Button
                  class="absolute bottom-0 left-50"
                  icon="pi pi-refresh"
                  v-if="edit"
                  @click="changeAvatar"
                >
                </Button>
                <Avatar class="w-full h-auto" size="xlarge" :image="pfp">
                </Avatar>
              </div>
              <div class="lg:col-5 col text-center lg:text-left">
                <h1 class="text-2xl md:text-5xl">{{ email }}</h1>
                <div v-if="!edit">
                  <p><b>First name:</b> {{ firstname }}</p>
                  <p><b>Last name:</b> {{ lastname }}</p>
                  <p><b>Github:</b> {{ github }}</p>
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
                </div>
              </div>
              <div class="lg:col-2 col lg:text-right text-center">
                <p>Saved results</p>
                <p class="text-8xl">{{ saved }}</p>
              </div>
              <div class="lg:col-2 col lg:text-right text-center">
                <p>Queries made</p>
                <p class="text-8xl">{{ queries }}</p>
              </div>
            </div>
          </template>
          <template #footer>
            <div class="grid mobcol justify-content-between">
              <div class="grid mobcol" v-if="this.$route.params.id === 'you'">
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
                <router-link class="py-1" to="/reset-password"
                  ><Button
                    class="p-button-text p-button-danger"
                    label="Reset Password"
                    icon="pi pi-key"
                  ></Button
                ></router-link>
              </div>
              <div v-if="this.$route.params.id === 'you'">
                <Button
                  v-if="!historyToggle"
                  icon="pi pi-history"
                  label="Show History"
                  @click="getHistory"
                />
                <Button
                  v-if="historyToggle"
                  label="Hide History"
                  @click="hideHistory"
                />
              </div>
            </div>
          </template>
        </Card>
      </form>
    </div>

    <div>
      <div class="flex flex-column align-items-center">
        <i v-if="historyLoad" class="pi pi-spin pi-spinner text-4xl mb-2"></i>
      </div>
      <div v-if="historyToggle & !historyLoad">
        <div v-if="historyDisplays.length">
          <h2 class="text-center">History</h2>
          <div class="grid justify-content-evenly mx-4 my-4">
            <Card
              v-for="historyItem in historyDisplays"
              :key="historyItem.id"
              class="card relative col-12 md:col-5 lg:col-3 m-3 darker-card"
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
        <div v-else>
          <h2 class="text-center">You haven't made any queries yet.</h2>
        </div>
      </div>

      <div v-if="saveDisplays.length">
        <h2 class="text-center">Saved Results</h2>
        <div class="grid justify-content-evenly mx-4 my-4">
          <Card
            data-aos="fade-up"
            data-aos-offset="-900"
            v-for="(save, i) in saveDisplays"
            class="card relative col-12 md:col-5 lg:col-3 m-3"
            :key="save.id"
          >
            <template #title>
              <h2>{{ save.title }}</h2>
            </template>
            <template #content>
              <Image :src="JSON.parse(save.info).image" preview />
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
                class="absolute right-0 bottom-0 mr-4 mb-4 p-button-warning"
                @click="removeSaved(save.id, i)"
              />
            </template>
          </Card>
        </div>
      </div>
      <div v-else>
        <h2 v-if="this.$route.params.id === 'you'" class="text-center mb-4">
          API Queries you make will show up here once you save some.
        </h2>
        <h2 v-else class="text-center mb-4">
          This user has not saved any results yet.
        </h2>
      </div>
    </div>

    <img
      v-if="saveDisplays.length"
      src="../assets/images/077-student-colour.svg"
      class="col-2 col-offset-5 no-pad"
    />
    <img
      v-else
      src="../assets/images/078-student-monochrome.svg"
      class="col-2 col-offset-5 no-pad"
    />
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
import Image from 'primevue/image'
import Skeleload from '../components/Skeleload.vue'
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
      historyLoad: false,
      pageLoad: false,
      selectedAvatar: '',
      avatarList: [
        'default',
        'boy_black_specs',
        'boy_black_stache',
        'boy_white_earphones_hoodie',
        'boy_white_futuristic_brown',
        'girl_black_earrings',
        'girl_black_mask',
        'girl_white_green',
        'girl_white'
      ],
      avatarIndex: 0
    }
  },
  components: {
    Button,
    Footer,
    Card,
    InputText,
    Navbar,
    Avatar,
    Image,
    Skeleload
  },
  mounted () {
    this.pageLoad = true
    if (this.$route.params.id === 'you') {
      this.fetchProfile(this.$store.state.user.id)
    } else {
      this.fetchProfile(this.$route.params.id)
    }
  },
  methods: {
    changeAvatar () {
      this.avatarIndex++
      this.avatarIndex %= 9
      this.selectedAvatar = this.avatarList[this.avatarIndex]
      this.pfp = require('@/assets/images/avatars/' + this.selectedAvatar + '.png')
    },
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
          this.saved -= 1
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
        .patch(`/api/v1/users/profiles/${userid}/`, { avatar: this.avatarList[this.avatarIndex], first_name: this.firstname, last_name: this.lastname, github_username: this.github })
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
              this.pfp = require('@/assets/images/avatars/' + response.data.avatar + '.png')
              this.saved = response.data.saved_results
              this.queries = response.data.queries_made
            }),
          axios
            .get(`/api/v1/saves/?search=${userid}`)
            .then(response => {
              this.saveDisplays = response.data
              this.saveDisplays.reverse()
            })
        ])
        .catch(error => {
          console.log(JSON.stringify(error))
        })
      this.pageLoad = false
    }
  }
}
</script>
