<template>
  <div class="h-auto overflow-auto">
    <Card>
      <template #title>
        <h3 class="text-center">spaceQuery</h3>
      </template>
      <template #content>
        <div class="grid">
          <p class="col">
            A webapp to easily query NASA and other space APIs, and save the
            results.
          </p>
          <div class="col">
            <ul class="mx-auto w-max">
              <li class="text-center">
                <a class="link" href="https://api.nasa.gov/">NASA Open APIs</a>
              </li>
              <li class="text-center">
                <a
                  class="link"
                  href="https://developers.google.com/earth-engine/"
                  >Google Earth Engine</a
                >
              </li>
              <li class="text-center">
                <a class="link" href="https://github.com/open-notify"
                  >Where is the ISS?</a
                >
              </li>
              <li class="text-center">
                <a class="link" href="https://github.com/SpaceRocks/"
                  >SpaceRocks</a
                >
              </li>
              <li class="text-center">
                <a
                  class="link"
                  href="https://github.com/chrisccerami/mars-photo-api"
                  >Mars Rover Photo API</a
                >
              </li>
              <li class="text-center">
                <a
                  class="link"
                  href="https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html"
                  >Exoplanet Archive (Caltech)</a
                >
              </li>
            </ul>
          </div>
          <div class="col">
            <router-link to="/feedback" class="w-max ml-auto block link">
              Feedback <i class="text-3xl pi pi-info-circle"></i>
            </router-link>
            <a
              class="w-max ml-auto block link"
              href="https://github.com/anirudhgray/space-front"
            >
              View on GitHub <i class="text-3xl pi pi-github"></i>
            </a>
            <a class="w-max ml-auto block link">
              Watch demo on YouTube <i class="text-3xl pi pi-youtube"></i>
            </a>
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
  }
}
</script>
