<template>
  <div class="m-4 grid">
    <div class="col mr-1">
      <Skeleton class="h-8rem mb-4"></Skeleton>
      <Skeleton class="mb-4"></Skeleton>
      <Skeleton class="mb-8"></Skeleton>
      <Skeleton class="w-3 mb-8"></Skeleton>
      <Skeleton class="h-8rem mb-4"></Skeleton>
      <Skeleton class="mb-4"></Skeleton>
      <Skeleton class="mb-8"></Skeleton>
      <Skeleton class="w-3"></Skeleton>
    </div>
    <div class="ml-1 col">
      <Skeleton shape="circle" size="8rem" class="h-8rem mb-4"></Skeleton>
      <Skeleton class="mb-4"></Skeleton>
      <Skeleton class="mb-8"></Skeleton>
      <Skeleton class="w-3 mb-8"></Skeleton>
      <Skeleton class="h-8rem mb-4"></Skeleton>
      <Skeleton class="mb-4"></Skeleton>
      <Skeleton class="mb-8"></Skeleton>
      <Skeleton class="w-3"></Skeleton>
    </div>
  </div>
</template>

<script>
import Skeleton from 'primevue/skeleton'

export default {
  name: 'Skeleload',
  components: {
    Skeleton
  }
}
</script>
