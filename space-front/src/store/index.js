import { createStore } from 'vuex'
import axios from 'axios'
import router from '../router'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      email: ''
    }
  },
  mutations: {
    initializeStore (state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.email = localStorage.getItem('email')
        state.user.id = localStorage.getItem('userid')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.email = ''
        state.user.id = 0
      }
    },
    setToken (state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken (state, token) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser (state, user) {
      state.user = user
    }
  },
  actions: {
    async logout (context) {
      await axios
        .get('/api/v1/users/actions/logout/')
        .catch(error => {
          console.log(JSON.stringify(error))
        })
      axios.defaults.headers.common.Authorization = ''
      localStorage.removeItem('token')
      localStorage.removeItem('email')
      localStorage.removeItem('userid')
      context.commit('removeToken')

      router.push('/login')
    }
  },
  modules: {
  }
})
