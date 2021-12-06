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
      <h1 class="text-8xl text-center">spaceQuery</h1>
      <div class="flex flex-column align-items-center">
        <div class="grid">
          <Button class="mx-2" label="Log in" />
          <Button class="mx-2" label="Learn more" />
          <Button class="mx-2" label="Github" />
        </div>
        <p class="mt-8">Powered by the NASA open APIs.</p>
      </div>
    </div>

    <div class="h-auto overflow-auto">
      <Card class="col-8 col-offset-2 mb-8 h-auto text-center p-5">
        <template #title>
          <h2>So, how does this work?</h2>
        </template>
        <template #subtitle>
          <p>Very well, then.</p>
        </template>
        <template #content>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Pellentesque id cursus tortor. Donec congue lobortis ante, nec
            maximus ex faucibus vitae. Nunc nec sodales risus. Curabitur
            volutpat, erat eu facilisis scelerisque, metus turpis iaculis erat,
            vel egestas dolor nisl at lorem. Donec id quam tellus.
          </p>
          <img
            class="my-4 col-8 col-offset-2"
            src="https://picsum.photos/600/400"
          />
          <p>
            Donec imperdiet lacinia erat, non sodales erat posuere placerat.
            Class aptent taciti sociosqu ad litora torquent per conubia nostra,
            per inceptos himenaeos. Nullam urna quam, cursus in ultrices ut,
            vulputate non ex.
          </p>
        </template>
        <template #footer>
          <p>A-ha!</p>
        </template>
      </Card>
    </div>

    <div class="h-auto overflow-auto">
      <Card v-if="logFlipped" class="col-8 col-offset-2 mb-8 h-auto p-5">
        <template #content>
          <div class="grid">
            <div class="col-6 flex flex-column">
              <h3 class="text-5xl mb-4">Register</h3>
              <div class="field">
                <label for="firstname1">Firstname</label>
                <input id="firstname1" type="text" class="inputfield w-full" />
              </div>
              <div class="field">
                <label for="lastname1">Lastname</label>
                <input id="lastname1" type="text" class="inputfield w-full" />
              </div>
              <div class="field">
                <Button label="Log In" class="w-full"></Button>
              </div>
              <div class="field mt-auto mb-0">
                <p>
                  Already have an account?
                  <Button
                    @click="flip"
                    class="p-button-text pb-0"
                    label="Log in."
                  ></Button>
                </p>
              </div>
            </div>
            <img src="https://picsum.photos/400/400" class="col-6" />
          </div>
        </template>
      </Card>

      <Card v-else class="col-8 col-offset-2 mb-8 h-auto p-5">
        <template #content>
          <div class="grid">
            <img src="https://picsum.photos/400/400" class="col-6" />
            <div class="col-6 flex flex-column">
              <h3 class="text-5xl text-right mb-4">Log In</h3>
              <div class="field">
                <label for="firstname1">Firstname</label>
                <input id="firstname1" type="text" class="inputfield w-full" />
              </div>
              <div class="field">
                <label for="lastname1">Lastname</label>
                <input id="lastname1" type="text" class="inputfield w-full" />
              </div>
              <div class="field">
                <Button label="Log In" class="w-full"></Button>
              </div>
              <div class="field mt-auto mb-0">
                <p>
                  Logging in is necessary to use this web app. Don't have an
                  account?
                  <Button
                    @click="flip"
                    label="Register here."
                    class="p-button-text pb-0"
                  ></Button>
                </p>
              </div>
            </div>
          </div>
        </template>
      </Card>
    </div>

    <div class="h-auto overflow-auto">
      <img
        src="https://picsum.photos/1000/500"
        class="col-8 col-offset-2 no-pad"
      />
    </div>

    <div class="h-auto overflow-auto">
      <Card>
        <template #title>
          <h3 class="text-center">spaceQuery</h3>
          <div class="grey col-6 col-offset-3">
            <h3 class="mb-4">Feedback</h3>
            <div class="field">
              <label for="firstname1">Firstname</label>
              <input id="firstname1" type="text" class="inputfield w-full" />
            </div>
            <div class="field">
              <label for="lastname1">Lastname</label>
              <input id="lastname1" type="text" class="inputfield w-full" />
            </div>
            <div class="field">
              <Button label="Submit" class="w-full"></Button>
            </div>
          </div>
        </template>
        <template #content>
          <div class="flex justify-content-between">
            <p class="col-3">
              A webapp to easily query NASA and other space APIs, and save the
              results.
            </p>
            <ul>
              <li>NASA Open APIs</li>
              <li>Google Earth</li>
              <li>Where is the ISS?</li>
            </ul>
            <p>View on GitHub</p>
          </div>
        </template>
        <template #footer>
          <p class="text-center">Made with love by Anirudh for CS50W.</p>
        </template>
      </Card>
    </div>
  </div>
</template>

<script>
import Card from 'primevue/card'
import Button from 'primevue/button'

export default {
  name: 'Home',
  components: {
    Card,
    Button
  },
  data () {
    return {
      logFlipped: false
    }
  },
  methods: {
    flip () {
      this.logFlipped = !this.logFlipped
    }
  }
}
</script>

<style>
.grey {
  background: rgb(247, 247, 247);
}
.no-pad {
  padding: 0;
}
</style>
