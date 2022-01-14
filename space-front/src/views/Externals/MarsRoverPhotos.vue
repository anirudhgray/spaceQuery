<template>
  <div class="grey flex flex-column">
    <Navbar></Navbar>
    <Skeleload v-if="pageLoad"></Skeleload>
    <Card class="card md:col-8 md:col-offset-2 my-4 px-2">
      <template #header>
        <router-link class="link" to="/explore/external/"
          ><i class="pi pi-undo"></i> Back to all APIs</router-link
        >
      </template>
      <template #title>
        <h1>Mars Rover Photos</h1>
      </template>
      <template #subtitle>
        <p>
          Image data gathered by NASA's Perseverance, Curiosity, Opportunity and
          Spirit rovers on Mars. Credit:
          <a href="https://github.com/chrisccerami/mars-photo-api"
            >Chris Cerami</a
          >
        </p>
      </template>
      <template #content>
        <form @submit.prevent="sendQuery">
          <p>Rover</p>
          <div class="field">
            <Dropdown
              id="roverdrop"
              v-model="rover"
              :options="roverDetails"
              optionLabel="name"
              placeholder="Select a rover"
              @change="selectRover"
            />
          </div>

          <p>Date Filter</p>
          <div class="field grid mobcol align-items-center">
            <div class="p-inputgroup md:col-5">
              <span class="p-inputgroup-addon">
                <RadioButton
                  name="dayFilterChoice"
                  value="Mars Sol"
                  v-model="dayFilterChoice"
                  id="day-mars"
                />
              </span>
              <InputText placeholder="Mars Sol" v-model="dayMars" />
            </div>
            <div class="p-inputgroup md:col-5">
              <span class="p-inputgroup-addon">
                <RadioButton
                  name="dayFilterChoice"
                  value="Earth Day"
                  v-model="dayFilterChoice"
                  id="day-earth"
                />
              </span>
              <Calendar
                placeholder="Earth Days"
                v-model="dayEarth"
                dateFormat="yy-mm-dd"
              />
            </div>
            <div class="md:col-2">
              <RadioButton
                name="dayFilterChoice"
                id="day-latest"
                value="Latest"
                v-model="dayFilterChoice"
              />
              <label class="ml-2" for="day-latest">Latest</label>
            </div>
          </div>

          <p>Camera</p>
          <div class="field">
            <Dropdown
              placeholder="Select a camera"
              v-model="camera"
              :options="cameraList"
              optionLabel="name"
            />
          </div>

          <p class="text-center">OR</p>

          <div class="field">
            <InputText
              v-model="query"
              class="inputfield w-full"
              placeholder="Direct Query"
            />
          </div>

          <div class="field">
            <Button
              type="submit"
              label="Go looking for little green men."
              class="w-full"
            />
          </div>
        </form>
      </template>
    </Card>

    <i
      v-if="results.length && !queryFail"
      class="align-self-center pi pi-check-circle text-4xl mb-2"
    ></i>
    <i
      v-if="queryFail"
      class="align-self-center pi pi-exclamation-triangle text-4xl mb-2"
    ></i>
    <i
      v-if="loading"
      class="align-self-center pi pi-spin pi-spinner text-4xl mb-2"
    ></i>

    <div v-if="results.length" class="flex flex-column">
      <Card class="card md:col-8 md:col-offset-2 px-2 mb-4">
        <template #header>
          <img :src="results[index].img_src" />
        </template>
        <template #content>
          <p>#{{ index }}</p>
          <p>Sol: {{ results[index].sol }}</p>
          <p>Earth Date: {{ results[index].earth_date }}</p>
          <p>
            Camera:
            {{ results[index].camera.name }} ({{
              results[index].camera.full_name
            }})
          </p>
          <p>Rover: {{ results[index].rover.name }}</p>
        </template>

        <template #footer>
          <div class="relative">
            <Button
              v-if="index > 0"
              label="Previous"
              class="mr-4"
              @click="nextResult(-1)"
            />
            <Button
              v-if="index < results.length - 1"
              label="Next"
              @click="nextResult(1)"
            />
            <Button
              v-if="bookmarked.includes(index)"
              class="absolute right-0 p-button-success"
              icon="pi pi-check"
              label="Added to profile"
            />
            <Button
              @click="saveResult"
              v-else
              class="absolute right-0"
              icon="pi pi-bookmark"
            />
          </div>
        </template>
      </Card>
    </div>

    <div v-if="results.length">
      <Card
        v-for="(rover, i) in roverInfoDisplay"
        :key="i"
        class="card md:col-8 md:col-offset-2 my-4 px-2"
      >
        <template #title>
          <p>{{ rover.name }}</p></template
        >
        <template #content>
          <p>Launch Date: {{ rover.launch_date }}</p>
          <p>Landing Date: {{ rover.landing_date }}</p>
          <p>Status: {{ rover.status }}</p>
          <p>Last Contact: {{ rover.max_date }}</p>
          <p>Total Sols Active: {{ rover.max_sol }}</p>
          <p>Total Photos: {{ rover.total_photos }}</p>
        </template>
      </Card>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Button from 'primevue/button'
import Card from 'primevue/card'
import Dropdown from 'primevue/dropdown'
import RadioButton from 'primevue/radiobutton'
import Calendar from 'primevue/calendar'
import Footer from '../../components/Footer.vue'
import InputText from 'primevue/inputtext'
import Navbar from '../../components/Navbar.vue'
import Skeleload from '../../components/Skeleload.vue'
import axios from 'axios'

export default {
  name: 'MarsRoverPhotos',
  components: {
    Button,
    Card,
    Footer,
    InputText,
    Navbar,
    Dropdown,
    RadioButton,
    Calendar,
    Skeleload
  },
  data () {
    return {
      queryFail: false,
      roverDetails: null,
      query: null,
      rover: null,
      dayFilterChoice: 'Mars Sol',
      dayEarth: null,
      dayMars: null,
      camera: null,
      cameraList: null,
      results: [],
      index: 0,
      roverInfoDisplay: null,
      loading: false,
      bookmarked: [],
      pageLoad: false
    }
  },
  mounted () {
    this.pageLoad = true
    this.getRovers()
  },
  methods: {
    async saveHistory () {
      const title = 'Mars Rover Photos'
      const info = JSON.stringify({
        Rover: this.rover.name,
        DayFilter: this.dayFilterChoice,
        DayEarth: this.dayEarth,
        DayMars: this.dayMars,
        Camera: this.camera
      })
      await axios
        .post('api/v1/history/', { title: title, info: info })
        .catch(error => {
          console.log(error)
        })
    },
    async saveResult () {
      const title = 'Mars Rover Photos'
      const info = JSON.stringify({
        image: this.results[this.index].img_src,
        text: {
          Rover: this.results[this.index].rover.name,
          EarthDate: this.results[this.index].earth_date,
          MarsSol: this.results[this.index].sol,
          Camera: this.results[this.index].camera.name1
        }
      })
      await axios
        .post('/api/v1/saves/', { title: title, info: info })
        .then(() => {
          this.bookmarked.push(this.index)
        })
        .catch(error => {
          console.log(error)
        })
    },
    resultCheck () {
      if (!this.results.length) {
        this.queryFail = true
      }
    },
    roverInfo (n, rover = null) {
      if (n) {
        this.roverInfoDisplay = this.roverDetails
      } else {
        for (let i = 0; i < this.roverDetails.length; i++) {
          const iter = this.roverDetails[i]
          if (iter.name === rover) {
            this.roverInfoDisplay = [iter]
          }
        }
      }
    },
    nextResult (n) {
      this.index += n
    },
    async getRovers () {
      await axios
        .get('https://mars-photos.herokuapp.com/api/v1/rovers/')
        .then(response => {
          this.roverDetails = response.data.rovers
          this.rover = this.roverDetails[3]
          this.cameraList = this.rover.cameras
        })
      this.pageLoad = false
    },
    selectRover () {
      for (let i = 0; i < this.roverDetails.length; i++) {
        const rover = this.roverDetails[i]
        if (rover.name === this.rover.name) {
          this.cameraList = rover.cameras
        }
      }
    },
    async sendQuery () {
      this.saveHistory()
      this.bookmarked = []
      this.queryFail = false
      this.loading = true
      this.index = 0
      this.results = []
      const queryRover = this.rover.name
      let queryURL
      if (this.query) {
        queryURL = this.query
      } else {
        let baseURL = 'https://mars-photos.herokuapp.com/api/v1/rovers'
        baseURL += '/' + this.rover.name
        const params = {}
        if (this.dayFilterChoice === 'Latest') {
          baseURL += '/' + 'latest_photos'
        } else {
          baseURL += '/photos'
          if (this.dayFilterChoice === 'Earth Day' && this.dayEarth) {
            const dayEarthList = String(this.dayEarth).split(' ')
            const year = dayEarthList[3]
            const month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].indexOf(dayEarthList[1])
            const day = dayEarthList[2]
            params.earth_date = year + '-' + month + '-' + day
          } else if (this.dayFilterChoice === 'Mars Sol') {
            params.sol = this.dayMars
          }
        }
        if (this.camera) {
          params.camera = this.camera.name
        }
        const paramString = new URLSearchParams(params)
        queryURL = baseURL + `?${paramString.toString()}`
      }
      this.roverInfo(0, queryRover)
      await axios
        .get(queryURL)
        .then(response => {
          this.loading = false
          if (this.dayFilterChoice === 'Latest') {
            this.results = response.data.latest_photos
          } else {
            this.results = response.data.photos
          }
          this.resultCheck()
        })
    }
  }
}
</script>
