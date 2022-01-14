<template>
  <div class="grey flex flex-column justify-content-between">
    <div>
      <Navbar></Navbar>
      <form
        @submit.prevent="searchUsers"
        class="p-inputgroup col-6 col-offset-3 my-4"
      >
        <InputText
          v-model="search"
          placeholder="Search Users by Email"
        ></InputText>
        <Button type="submit" icon="pi pi-search"></Button>
      </form>
      <div class="grid grid-nogutter justify-content-evenly mb-2">
        <Card
          data-aos="fade-up"
          v-for="user in results"
          :key="user.user"
          class="card m-2 px-2 -pb-1 result-card"
          @click="routerUserPage(user.user)"
        >
          <template #content>
            <div class="grid -mb-2">
              <Avatar
                :image="
                  require('@/assets/images/avatars/' + user.avatar + '.png')
                "
              ></Avatar>
              <p class="ml-2">{{ user.email }}</p>
            </div>
          </template>
        </Card>
      </div>
    </div>
    <img
      src="../assets/images/031-drawkit-phone-conversation-colour.svg"
      class="col-2 col-offset-5 no-pad"
    />
    <Footer class="block"></Footer>
  </div>
</template>

<script>
import Footer from '../components/Footer.vue'
import InputText from 'primevue/inputtext'
import Navbar from '../components/Navbar.vue'
import Button from 'primevue/button'
import axios from 'axios'
import Card from 'primevue/card'
import Avatar from 'primevue/avatar'

export default {
  name: 'UserSearch',
  data () {
    return {
      search: '',
      results: []
    }
  },
  components: {
    Footer,
    InputText,
    Navbar,
    Button,
    Card,
    Avatar
  },
  methods: {
    async searchUsers () {
      await axios
        .get(`/api/v1/users/profiles?search=${this.search}`)
        .then(response => {
          this.results = response.data
        })
    },
    routerUserPage (id) {
      this.$router.push(`/user/${id}`)
    }
  }
}
</script>
