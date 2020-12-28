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
        {id: 2, title: "运行", icon: "caret-right", loading: false, func: this.runGraph},
        {id: 3, title: "下载code", icon: "download", loading: false, func: this.downloadCode},
        {id: 4, title: "下载model", icon: "download", loading: false, func: this.downloadModel},
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
    },

    downloadCode(operation) {
      operation.loading = true
      let url = "http://127.0.0.1:8000/media/file/%E6%B3%A2%E5%A3%AB%E9%A1%BF%E6%88%BF%E4%BB%B7%E9%A2%84%E6%B5%8B.py"
      this.$axios({
        method: "get",
        url: url,
        responseType: "blob"
      }).then(res => {
        let blob = new Blob([res.data], {type: 'application/octet-stream'})
        let href = window.URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.style.display = 'none'
        link.href = href
        link.download = "波士顿房价预测.py"
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
      })
      // graphApi.getGraphCode(1).then(res => {
      //   console.log(res);
      // }).catch(err => {
      //   console.log(err);
      // })
      operation.loading = false
    },

    downloadModel(operation) {
      operation.loading = true
      let url = "http://127.0.0.1:8000/media/file/model.pkl"
      this.$axios({
        method: "get",
        url: url,
        responseType: "blob"
      }).then(res => {
        let blob = new Blob([res.data], {type: 'application/octet-stream'})
        let href = window.URL.createObjectURL(blob)
        const link = document.createElement('a')
        link.style.display = 'none'
        link.href = href
        link.download = "model.pkl"
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
      })
      // graphApi.getGraphCode(1).then(res => {
      //   console.log(res);
      // }).catch(err => {
      //   console.log(err);
      // })
      operation.loading = false
    }
  }
}
</script>

<style scoped>

</style>