<template>
  <div class="h-auto overflow-auto">
    <Card class="card">
      <template #title>
        <h3 class="text-center">spaceQuery</h3>
      </template>
      <template #content>
        <div class="grid tabcol grid-no-gutter">
          <div class="col">
            <ul>
              <li class="w-max mr-auto tabcenter">Illustrations by/from:</li>
              <li class="w-max lg:mt-0 mt-2 mr-auto tabcenter">
                <a
                  class="link"
                  href="https://icons8.com/illustrations/author/6103782c1781404355b65f35"
                  >Anna Yashina</a
                >
                from
                <a class="link" href="https://icons8.com/illustrations"
                  >Ouch!</a
                >
              </li>
              <li class="w-max mr-auto tabcenter">
                <a href="https://icons8.com">Icons8</a>
              </li>
              <li class="w-max mr-auto tabcenter">
                <a class="link" href="https://drawkit.com/">Drawkit</a>
              </li>
              <li class="w-max mr-auto tabcenter">
                <a class="link" href="https://exoplanets.nasa.gov/">NASA</a>
              </li>
              <li class="w-max mr-auto tabcenter">
                <a class="link" href="https://www.humaaans.com/">Humaaans</a>
              </li>
            </ul>
          </div>
          <div class="col">
            <ul class="mx-auto w-max text-center">
              <li class="w-max mx-auto">
                <a class="link" href="https://api.nasa.gov/">NASA Open APIs</a>
              </li>
              <li class="w-max mx-auto">
                <a class="link" href="https://wheretheiss.at/"
                  >Where is the ISS?</a
                >
              </li>
              <li class="w-max mx-auto">
                <a class="link" href="https://github.com/SpaceRocks/"
                  >SpaceRocks</a
                >
              </li>
              <li class="w-max mx-auto">
                <a
                  class="link"
                  href="https://github.com/chrisccerami/mars-photo-api"
                  >Mars Rover Photo API</a
                >
              </li>
              <li class="w-max mx-auto">
                <a
                  class="link"
                  href="https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html"
                  >Exoplanet Archive (Caltech)</a
                >
              </li>
            </ul>
          </div>
          <div class="col">
            <ul>
              <p class="md:text-right text-center">
                A webapp to easily query NASA and other space APIs, and save the
                results.
              </p>
              <router-link
                v-if="$store.state.isAuthenticated"
                to="/feedback"
                class="w-max ml-auto tabcenter block link"
              >
                Feedback <i class="text-3xl pi pi-info-circle"></i>
              </router-link>
              <a
                class="w-max ml-auto tabcenter block link"
                href="https://github.com/anirudhgray/spaceQuery"
              >
                View on GitHub <i class="text-3xl pi pi-github"></i>
              </a>
              <a
                @click="notImplemented"
                class="w-max ml-auto tabcenter block link"
              >
                Watch demo on YouTube <i class="text-3xl pi pi-youtube"></i>
              </a>
              <a
                class="w-max ml-auto tabcenter block link"
                href="https://spacequery-api.herokuapp.com/api/v1/"
              >
                REST API <i class="text-3xl pi pi-server"></i>
              </a>
            </ul>
          </div>
        </div>
      </template>
      <template #footer>
        <p class="text-center">
          Made for
          <a class="link" href="https://cs50.harvard.edu/web/2020/">CS50W.</a>
        </p>
      </template>
    </Card>
  </div>
</template>
<script>
import Card from 'primevue/card'

export default {
  name: 'Footer',
  components: {
    Card
  },
  methods: {
    notImplemented () {
      this.$toast.add({ severity: 'error', summary: 'Not implemented yet.', detail: 'What a lazy dev...', life: 3000 })
    }
  }
}
</script>

<style>
@media (max-width: 700px) {
  .tabcenter {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
