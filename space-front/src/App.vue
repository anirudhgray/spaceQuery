<template>
  <router-view :key="$route.fullPath" />
  <Toast
    position="bottom-right"
    :breakpoints="{ '920px': { width: '100%', right: '0', left: '0' } }"
  ></Toast>
  <ScrollTop class="scrolltop" :threshold="600" />
</template>

<script>
import Toast from 'primevue/toast'
import axios from 'axios'
import ScrollTop from 'primevue/scrolltop'

export default {
  name: 'App',
  components: {
    Toast,
    ScrollTop
  },
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

:root {
  --bg-colour: rgb(247, 247, 247);
  --card-color: white;
  --card-color-darker: rgb(220, 220, 220);
  --primary-text-colour: black;
  --secondary-text-colour: rgb(82, 82, 82);
  --anim-link-colour: purple;
  --skele-bg: white;
  --link-hover-colour: black;
  --scrolltop-colour: rgba(0, 0, 0, 0.7);
}
.darkmode {
  --bg-colour: rgb(20, 20, 20);
  --card-color: rgb(34, 34, 34);
  --card-color-darker: rgb(48, 48, 48);
  --primary-text-colour: white;
  --secondary-text-colour: rgb(175, 174, 174);
  --anim-link-colour: rgb(214, 50, 214);
  --skele-bg: rgb(68, 68, 68);
  --link-hover-colour: white;
  --scrolltop-colour: rgba(214, 50, 214, 0.7);
}
.p-scrolltop.p-link {
  background: var(--scrolltop-colour);
}
.grey {
  background: var(--bg-colour);
}
.card {
  background: var(--card-color);
  color: var(--primary-text-colour);
}
.skele {
  background: var(--skele-bg);
}
html {
  background: var(--bg-colour);
}
.navlink.router-link-exact-active::after {
  content: " ";
  display: block;
  width: 100%;
  height: 2px;
  background-color: var(--anim-link-colour);
  transition: width 300ms;
}
.navlink {
  color: var(--anim-link-colour);
  text-decoration: none;
  font-family: sans-serif;
}
.navlink:hover {
  color: var(--link-hover-colour);
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
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}

/* set up the body */
body {
  color: var(--primary-text-colour);
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
.no-pad {
  padding: 0;
}
.result-card {
  position: relative;
  z-index: 1;
  max-width: 35rem;
}
.result-card:hover {
  cursor: pointer;
  background: var(--card-color-darker);
}
a {
  text-decoration: none;
  color: var(--secondary-text-colour);
}
.darker-card {
  background: var(--card-color-darker);
}
.link {
  text-decoration: none;
  color: var(--secondary-text-colour);
}
.link:hover {
  color: var(--link-hover-colour);
}

.github-button {
  background: black;
  color: white;
  border: none;
}
.github-button:hover {
  background: rgb(39, 39, 39);
}
.r-900-vis {
  display: none;
}
.r-700-vis {
  display: none;
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
@media (max-width: 900px) {
  .r-900-vis {
    display: block;
  }
  .r-900-invis {
    display: none;
  }
}
@media (max-width: 700px) {
  .r-700-vis {
    display: block;
  }
  .r-700-invis {
    display: none;
  }
  .tabcol {
    flex-direction: column;
    gap: 1rem;
  }
}
@media (max-width: 425px) {
  .mobcol {
    flex-direction: column;
    align-content: center;
    gap: 2rem;
  }
}
</style>
