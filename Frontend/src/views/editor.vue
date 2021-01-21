<template>
  <a-layout>
    <a-layout-header>
      <Header></Header>
    </a-layout-header>
    <a-layout>
      <a-layout-sider>
        <MenuTree></MenuTree>
      </a-layout-sider>
      <a-layout-content>
        <Editor></Editor>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>
import Header from "@/components/Editor/components/Header";
import MenuTree from "@/components/Editor/components/MenuTree";
import Editor from "@/components/Editor/components/Editor";
import modelRectNode from "@/config/graph/modelRectNode";
import addEdge from "@/config/behavior/add-edge";
import hoverNode from "@/config/behavior/hover-node";
import selectNode from "@/config/behavior/select-node";
import {mapGetters} from "vuex";
import customEdge from "@/config/graph/customEdge";

export default {
  name: "editor",
  components: {
    Header,
    MenuTree,
    Editor
  },
  data() {
    return {
      addNodeEdge: false,
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
  created() {
    this.init()
  },
  methods: {
    init() {
      modelRectNode.init()
      addEdge.init()
      customEdge.init()
      hoverNode.init()
      selectNode.init()
    },
  },
  
}
</script>

<style scoped>
.ant-layout-header, .ant-layout-sider {
  padding: 0;
  background: white;
}
</style>