<template>
  <div id="app">
    <HeaderMenu/>

  </div>
</template>

<script>
import HeaderMenu from './components/HeaderMenu.vue'

export default {
  name: 'App',
  components: {
    HeaderMenu
  },
  data () {

  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Google+Sans");

#app {
  font-family: "Google Sans" , sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

:root {
  --primary: #06BBCC;
  --light: #F0FBFC;
  --dark: #181d38;
}

.fw-medium {
  font-weight: 600 !important;
}

.fw-semi-bold {
  font-weight: 700 !important;
}

.back-to-top {
  position: fixed;
  display: none;
  right: 45px;
  bottom: 45px;
  z-index: 99;
}

ul {
  list-style: none;
  padding-left: 0;
}

/*** Button ***/
.btn {
  font-family: 'Nunito', sans-serif;
  font-weight: 600;
  transition: .5s;
}

.btn.btn-primary {
  color: #FFFFFF;
  background-color: var(--primary);
  border: none;
}

.btn.btn-primary:hover {
  color: var(--primary);
  background-color: #FFFFFF;
}

.btn-square {
    width: 38px;
    height: 38px;
}

.btn-sm-square {
    width: 32px;
    height: 32px;
}

.btn-lg-square {
    width: 48px;
    height: 48px;
}

.btn-square,
.btn-sm-square,
.btn-lg-square {
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: normal;
    border-radius: 0px;
}

</style>
