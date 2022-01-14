import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import UserSearch from '../views/UserSearch.vue'
import Explore from '../views/Explore.vue'
import MarsRoverPhotos from '../views/Externals/MarsRoverPhotos.vue'
import AsteroidsNeoWs from '../views/Externals/AsteroidsNeoWs.vue'
import ISSTracker from '../views/Externals/ISSTracker.vue'
import ExoplanetsArchive from '../views/Externals/ExoplanetsArchive.vue'
import Feedback from '../views/Feedback.vue'
import LogIn from '../views/LogIn.vue'
import Register from '../views/Register.vue'
import NotFound404 from '../views/NotFound404.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'
import ForgotReset from '../views/ForgotReset.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/forgot-reset',
    name: 'ForgotReset',
    component: ForgotReset,
    meta: {
      requireLogin: false
    }
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: ResetPassword,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/user/:id',
    name: 'Profile',
    component: Profile,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/user/search',
    name: 'UserSearch',
    component: UserSearch,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/explore/external',
    name: 'ExploreExternal',
    component: Explore,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/explore/external/mars-rover-photos',
    name: 'MarsRoverPhotos',
    component: MarsRoverPhotos,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/explore/external/asteroids-neows',
    name: 'AsteroidsNeoWs',
    component: AsteroidsNeoWs,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/explore/external/iss-tracker',
    name: 'ISSTracker',
    component: ISSTracker,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/explore/external/exoplanet-archive',
    name: 'ExoplanetsArchive',
    component: ExoplanetsArchive,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: Feedback,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:pathMatch(.*)',
    name: '404',
    component: NotFound404
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  store.commit('setTheme')
  window.scrollTo(0, 0)
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/')
  } else {
    next()
  }
})

export default router
