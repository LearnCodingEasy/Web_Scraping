<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <div>
        <h1 class="title animate__animated animate__backInUp animate__delay-1sv">{{ title }}</h1>
        <p class="text animate__animated animate__backInUp animate__delay-2s">{{ description }}</p>
        <div class="data animate__animated animate__backInUp animate__delay-3s">
          <p class="info" v-for="d in data" :key="d">{{ d }}</p>
        </div>
      </div>
    </div>
  </header>

  <RouterView />
</template>
<script>
import axios from 'axios'

export default {
  data() {
    return {
      title: '',
      description: '',
      data: [],
    }
  },
  mounted() {
    // Call API from Django
    axios
      .get('http://127.0.0.1:8000/api/scrape/')
      .then((response) => {
        this.title = response.data.title
        this.description = response.data.description
        this.data = response.data.data
      })
      .catch((error) => {
        console.error('There was an error!', error)
      })
  },
}
</script>
