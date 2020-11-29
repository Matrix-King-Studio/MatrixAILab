<template>
  <div id="app">
    <editor></editor>
  </div>
</template>

<script>
import editor from "@/components/Editor/editor";

export default {
  name: 'App',
  components: {
    editor
  }
}
</script>

<style>
/* 隐藏滚动条 */
::-webkit-scrollbar {
  width: 0;
}
</style>
