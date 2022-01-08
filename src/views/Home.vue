<template>
  <div class="grey">
    <div
      class="
        h-screen
        flex flex-column
        justify-content-evenly
        align-items-center
      "
    >
      <h1 class="md:text-8xl text-5xl text-center">spaceQuery</h1>
      <div class="flex flex-column align-items-center">
        <div class="grid mobcol">
          <router-link class="mx-2 flex" to="/login"
            ><Button class="mx-auto" label="Log in"
          /></router-link>
          <Button class="mx-2" label="Learn more" @click="scrollAbout" />
          <a class="mx-2 flex" href="https://github.com/anirudhgray/space-front"
            ><Button class="mx-auto" label="Github"
          /></a>
        </div>
        <p class="mt-8">Powered by the NASA open APIs.</p>
      </div>
    </div>

    <div class="h-auto overflow-auto" ref="about">
      <Card class="md:col-8 md:col-offset-2 mb-4 h-auto text-center md:p-5 p-1">
        <template #title>
          <h2>So, how does this work?</h2>
        </template>
        <template #subtitle>
          <p>Figure it out. Nah, I'm kidding.</p>
        </template>
        <template #content>
          <p>
            At its core, this webapp acts as a frontend for querying a bunch of
            awesome space related APIs (more info below). It doesn't sound
            nearly as awesome now that I have written it down, but yeah. Why do
            I need to be logged in, you ask? Well, I've added some nifty
            functionality which allows you to save any query results that you
            particularly like to your user profile for later reference — can't
            do that without having you signed in. This also allows you to look
            up other users and look at their saved posts. I'm not entirely sure
            why I added this, and what purpose it serves, but it's there.
            ¯\(°_o)/¯
          </p>
          <div class="my-4 col-8 col-offset-2">
            <img src="https://picsum.photos/600/400" />
            <p>
              Here's a random image. I should probably add something useful
              here.
            </p>
          </div>
          <p>Anyway. The flow is pretty simple:</p>
          <div class="grid">
            <p class="col-4 text-6xl text-right">1</p>
            <p class="col-8 m-auto text-left">
              <router-link to="/login">Log in</router-link> in or
              <router-link to="/register">register</router-link>.
            </p>
          </div>
          <div class="grid">
            <p class="col-8 m-auto text-right">
              Head over to the Explore page from the navbar.
            </p>
            <p class="col-4 text-6xl text-left">2</p>
          </div>
          <div class="grid">
            <p class="col-4 text-6xl text-right">3</p>
            <p class="col-8 m-auto text-left">
              Select whichever API tickles your fancy.
            </p>
          </div>
          <div class="grid">
            <p class="col-8 m-auto text-right">Enter the query paramters.</p>
            <p class="col-4 text-6xl text-left">4</p>
          </div>
          <div class="grid">
            <p class="col-4 text-6xl text-right">5</p>
            <p class="col-8 m-auto text-left">buttonbuttonbutton.</p>
          </div>
          <div class="grid">
            <p class="col-8 m-auto text-right">Await great knowledge.</p>
            <p class="col-4 text-6xl text-left">6</p>
          </div>
          <div class="grid">
            <p class="col-4 text-6xl text-right">7</p>
            <p class="col-8 m-auto text-left">
              Save cool results to your profile.
            </p>
          </div>
        </template>
        <template #footer>
          <p>
            Enjoy, and let me know what you think (feedback link in the footer).
          </p>
        </template>
      </Card>
      <Card class="md:col-8 md:col-offset-2 mb-4 h-auto text-center -p-3 pt-5">
        <template #title> APIs available </template>
        <template #footer>
          <div class="grid">
            <div class="col h-15rem" v-for="(api, index) in apis" :key="index">
              <div
                class="h-full"
                @mouseenter="toggleAPI(index)"
                v-show="!api.visible"
              >
                <p class="text-6xl">
                  {{ api.letter }}
                </p>
              </div>
              <div
                class="h-full"
                @mouseleave="toggleAPI(index)"
                v-show="api.visible"
              >
                <p class="text-6xl">{{ api.letter }}</p>
                <p class="md:text-2xl text-xl">{{ api.name }}</p>
                <img :src="api.imgsrc" class="w-min m-auto mt-5" />
              </div>
            </div>
          </div>
        </template>
      </Card>
    </div>

    <div class="h-auto mb-4 overflow-auto flex flex-column">
      <img
        src="../assets/images/space-coming-soon.png"
        class="md:col-4 md:col-offset-4 no-pad"
      />
      <router-link class="mx-auto" to="/login"
        ><Button label="Get Started"></Button
      ></router-link>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Button from 'primevue/button'
import Footer from '../components/Footer.vue'

export default {
  name: 'Home',
  components: {
    Card,
    Button,
    Footer
  },
  data () {
    return {
      apis: [
        {
          letter: 'A',
          name: 'Asteroids',
          visible: false,
          imgsrc: require('@/assets/images/icons8-asteroid-64.png')
        },
        {
          letter: 'I',
          name: 'ISS',
          visible: false,
          imgsrc: require('@/assets/images/icons8-space-station-64.png')
        },
        {
          letter: 'M',
          name: 'Mars',
          visible: false,
          imgsrc: require('@/assets/images/icons8-mars-60.png')
        },
        {
          letter: 'E',
          name: 'Exoplanets',
          visible: false,
          imgsrc: require('@/assets/images/icons8-radar-64.png')
        }
      ]
    }
  },
  methods: {
    toggleAPI (index) {
      for (let i = 0; i < this.apis.length; i++) {
        if (i === index) {
          this.apis[index].visible = !this.apis[index].visible
        } else {
          this.apis[i].visible = false
        }
      }
    },
    scrollAbout () {
      console.log(this.$refs.about)
      this.$refs.about.scrollIntoView({ behavior: 'smooth' })
    }
  }
}
</script>
