<template>
  <router-view />
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate () {
    this.$store.commit('initializeStore')

    if (this.$store.state.token) {
      axios.defaults.headers.common.Authorization = 'Token ' + this.$store.state.token
    } else {
      axios.defaults.headers.common.Authorization = ''
    }
  }
}
</script>

<style lang="scss">
/* box sizing */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* reset margin */
body,
h1,
h2,
h3,
h4,
h5,
p,
img,
figure,
picture {
  margin: 0;
}

h1,
h2,
h3,
h4,
h5,
h6,
p {
  font-weight: 400;
}

/* set up the body */
body {
  font-family: var(--ff-sans-normal);
  font-size: var(--fs-400);
  color: hsl(var(--clr-white));
  background-color: hsl(var(--clr-dark));
  line-height: 1.5;
  min-height: 100vh;
}

/* make images easier to work with */
img,
picture {
  max-width: 100%;
  display: block;
}

/* make forms elements easier to work with */
input,
button,
textarea,
select {
  font: inherit;
}

/* remove animations for people who've turned them off */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
</style>
