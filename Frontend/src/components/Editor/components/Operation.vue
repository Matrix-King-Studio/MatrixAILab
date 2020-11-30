<template>
  <div>
    <div
      v-for="operation in operations"
      :key="operation.id">
      <a-tooltip>
        <template
          slot="title">
          {{ operation.title }}
        </template>
        <a-button
          type="primary"
          shape="circle"
          size="small"
          style="float:left; margin-left: 7px"
          :icon="operation.icon"
          :loading="operation.loading"
          @click="operation.func(operation)"/>
      </a-tooltip>
    </div>
  </div>
</template>

<script>
import graphApi from "@/config/api/graph";
import {mapGetters} from "vuex";

export default {
  name: "Operation",
  data() {
    return {
      operations: [
        {id: 1, title: "保存", icon: "save", loading: false, func: this.saveGraph},
        {id: 2, title: "运行", icon: "caret-right", loading: false, func: this.runGraph}
      ]
    }
  },
  computed: {
    ...mapGetters(["graph"]),
    graph: {
      get() {
        return this.$store.state.graph.graph
      },
      set(graph) {
        this.$store.commit("graph/SetGraph", graph)
      }
    },
  },
  methods: {
    saveGraph(operation) {
      operation.loading = true
      this.$store.dispatch("graph/SaveGraph").then(res => {
        console.log(res);
        this.$message.success("保存成功！");
      }).catch(err => {
        console.log(err);
      })
      operation.loading = false
    },

    runGraph(operation) {
      operation.loading = true
      graphApi.runGraph(1).then(res => {
        console.log(res);
      }).catch(err => {
        console.log(err);
      })
      operation.loading = false
    }
  }
}
</script>

<style scoped>

</style>