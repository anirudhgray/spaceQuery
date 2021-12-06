<template>
  <div class="h-auto overflow-auto">
    <Card>
      <template #title>
        <h3 class="text-center">spaceQuery</h3>
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
