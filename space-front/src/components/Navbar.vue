<template>
  <router-link class="r-900-vis landing-link mx-auto" to="/"
    >spaceQuery</router-link
  >
  <Button
    icon="pi pi-bars"
    @click="togglenav"
    class="r-700-vis mx-auto mt-4"
  ></Button>
  <Card class="card r-700-vis col-8 mt-3 col-offset-2" v-if="mobnav">
    <template #content>
      <div class="flex flex-column text-center">
        <p
          class="paralink navlink mx-2 my-2 p-2"
          to="/explore/external"
          @click="toggleExternal"
        >
          Explore APIs
        </p>
        <Menu ref="menu" :model="items" :popup="true">
          <template #item="{ item }">
            <div @click="externalMenuPush(item.to)" class="px-3 py-2 linkhover">
              <router-link :to="item.to">{{ item.label }}</router-link>
            </div>
          </template>
        </Menu>
        <router-link class="navlink mx-2 my-2 p-2" to="/user/search"
          >Search Users</router-link
        >
        <Button
          :icon="{
            'pi pi-moon': this.$store.state.light,
            'pi pi-sun': !this.$store.state.light,
          }"
          @click="changeTheme"
          class="px-auto mx-auto p-button-rounded p-button-text my-2 text-2xl"
        />
        <router-link to="/user/you" class="navlink my-2 p-2">{{
          $store.state.user.email
        }}</router-link>
        <Button
          @click="logout"
          class="p-button-danger my-2 p-2"
          label="Log Out"
        ></Button>
      </div>
    </template>
  </Card>
  <div class="r-700-invis grid justify-content-between mt-4 mx-4">
    <nav class="grid align-items-center">
      <router-link class="r-900-invis landing-link mx-2" to="/"
        >spaceQuery</router-link
      >
      <p
        class="paralink navlink mx-2"
        to="/explore/external"
        @click="toggleExternal"
      >
        Explore APIs
      </p>
      <Menu ref="menu" :model="items" :popup="true">
        <template #item="{ item }">
          <div @click="externalMenuPush(item.to)" class="px-3 py-2 linkhover">
            <router-link :to="item.to">{{ item.label }}</router-link>
          </div>
        </template>
      </Menu>
      <router-link class="navlink mx-2" to="/user/search"
        >Search Users</router-link
      >
    </nav>
    <nav class="grid align-items-center">
      <Button
        :icon="{
          'pi pi-moon': this.$store.state.light,
          'pi pi-sun': !this.$store.state.light,
        }"
        @click="changeTheme"
        class="p-button-rounded p-button-text"
      />
      <router-link to="/user/you" class="navlink mx-4">{{
        $store.state.user.email
      }}</router-link>
      <Button @click="logout" class="p-button-danger" label="Log Out"></Button>
    </nav>
  </div>
</template>

<style>
:root {
  --purple: purple;
}
.darkmode {
  --purple: rgb(214, 50, 214);
}
.landing-link {
  font-size: 2rem;
}
.navlink.router-link-exact-active::after {
  content: " ";
  display: block;
  width: 100%;
  height: 2px;
  background-color: var(--purple);
  transition: width 300ms;
}
.navlink {
  color: var(--purple);
  text-decoration: none;
  font-family: sans-serif;
}
.navlink::after {
  content: " ";
  display: block;
  width: 0;
  height: 2px;
  background-color: var(--purple);
  transition: width 300ms;
}
.navlink:hover::after {
  width: 100%;
}
ul {
  padding: 0;
}
li {
  list-style-type: none;
}
.linkhover:hover {
  background: rgb(230, 230, 230);
  cursor: pointer;
}
.paralink {
  cursor: pointer;
}
</style>

<script>
import Button from 'primevue/button'
import Menu from 'primevue/menu'
import Card from 'primevue/card'
import axios from 'axios'

export default {
  name: 'Navbar',
  components: {
    Button,
    Menu,
    Card
  },
  data () {
    return {
      items: [
        { label: 'See all', to: '/explore/external/' }
      ],
      mobnav: false
    }
  },
  mounted () {
    this.fetchAPIS()
  },
  methods: {
    notImplemented () {
      this.$toast.add({ severity: 'error', summary: 'Not implemented yet.', detail: 'What a lazy dev...', life: 3000 })
    },
    changeTheme () {
      this.$store.commit('changeTheme')
    },
    togglenav () {
      this.mobnav = !this.mobnav
    },
    externalMenuPush (to) {
      this.$router.push(to)
    },
    toggleExternal (event) {
      this.$refs.menu.toggle(event)
    },
    logout () {
      this.$store.dispatch('logout')
    },
    async fetchAPIS () {
      await axios
        .get('/api/v1/externals/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.items.push({ label: response.data[i].name, to: `/explore/external/${response.data[i].url_name}` })
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
