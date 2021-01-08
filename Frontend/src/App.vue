<template>
  <div id="app">
    <router-link to="/"></router-link>
    <router-link to="/login"></router-link>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
/* 隐藏滚动条 */
::-webkit-scrollbar {
  width: 0;
}
</style>
