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

    <div class="h-auto overflow-auto"></div>
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
  }
}
</script>

<style>
.grey {
  background: rgb(247, 247, 247);
}
</style>
