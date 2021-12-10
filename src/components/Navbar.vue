<template>
  <div class="grid justify-content-between mt-4 mx-4">
    <nav class="grid align-self-center">
      <router-link class="navlink mx-2" to="/">Landing</router-link>
      <router-link class="navlink mx-2" to="/user/you"
        >Your Profile</router-link
      >
      <router-link class="navlink mx-2" to="/explore/external"
        >Explore APIs</router-link
      >
      <router-link class="navlink mx-2" to="#">Internal Content</router-link>
      <router-link class="navlink mx-2" to="/user/search"
        >Search Users</router-link
      >
    </nav>
    <Button @click="logout" class="p-button-danger" label="Log Out"></Button>
  </div>
</template>

<style>
.navlink.router-link-exact-active::after {
  content: " ";
  display: block;
  width: 100%;
  height: 2px;
  background-color: purple;
  transition: width 300ms;
}
.navlink {
  color: purple;
  text-decoration: none;
  font-family: sans-serif;
}
.navlink::after {
  content: " ";
  display: block;
  width: 0;
  height: 2px;
  background-color: purple;
  transition: width 300ms;
}
.navlink:hover::after {
  width: 100%;
}
</style>

<script>
import Button from 'primevue/button'

export default {
  name: 'Navbar',
  components: {
    Button
  },
  methods: {
    logout () {
      this.$store.dispatch('logout')
    }
  }
}
</script>
