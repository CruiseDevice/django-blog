/* eslint-disable */
import axios from 'axios'

const state = {
  posts: JSON.parse(localStorage.getItem('posts')) || []
}

const mutations = {
  UPDATE_BLOG_POSTS(state, payload) {
    state.posts = payload
  }
}

const actions = {
  fetchblogs(state) {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/posts/',
      headers: {
          'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        state.commit('UPDATE_BLOG_POSTS', response.data)
        localStorage.setItem('posts', JSON.stringify(response.data))
      })
  },
}

const getters = {
  getposts: state => state.posts,
  postById: state => (id) => {
    return state.posts.find(post => post.id === id)
  }
}

const blogListModule = {
  state,
  mutations,
  actions,
  getters
}

export default blogListModule
