<template>
  <div>
    <div
      id="toolbarMountNode"
      style="height: 38px; width: 50%; float: left"></div>
    <div
      id="operationMountNode"
      style="height: 38px; width: 50%; float: right">
      <Operation></Operation>
    </div>
    <div
      id="graphMountNode">
      <ContextMenu
        ref="menu"></ContextMenu>
      <Parameter
        :fileList="fileList"
        :parameters="parameters"
        :parameterVisible="parameterVisible"
        @closeDrawer="closeDrawer"></Parameter>
    </div>
  </div>
</template>

<script>
import G6 from "@antv/g6"
import {mapGetters} from "vuex";
import file from "@/config/api/file";
import Parameter from "@/components/Editor/components/Parameter";
import Operation from "@/components/Editor/components/Operation";
import ContextMenu from "@/components/Editor/components/ContextMenu";

export default {
  name: "Editor",
  components: {
    Operation,
    Parameter,
    ContextMenu
  },
  data() {
    return {
      parameters: [],
      fileList: [],
      parameterVisible: false,
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
  mounted() {
    this.$nextTick(() => {
      this.init();
    });
  },
  methods: {
    init() {
      const toolbarMountNode = document.getElementById("toolbarMountNode")
      const toolbar = new G6.ToolBar({
        container: toolbarMountNode,
      })

      const graphMountNode = document.getElementById("graphMountNode")
      this.graph = new G6.Graph({
        container: graphMountNode,
        width: document.body.clientWidth,
        height: document.body.clientHeight - 38,
        minZoom: 0.4,
        maxZoom: 3,
        animate: true,
        plugins: [toolbar],
        defaultEdge: {
          shape: 'cubic',
        },
        modes: {
          default: [
            'drag-combo',
            'drag-canvas',
            'zoom-canvas',
            'drag-node',
            "hover-node",
            'click-select',
            'activate-relations',
            'brush-select',
            "select-node"],
          addEdge: ['add-edge', 'click-select']
        },
      })

      this.$store.dispatch("graph/GetGraph", 1).then(res => {
        this.graph.data(res.data)
        this.graph.render()
      }).catch(err => {
        console.log(err);
      })

      this.graph.on("node:dblclick", (event) => {
        // 双击节点 -> 显示参数设置
        this.parameterVisible = true
        // 获取节点参数
        this.parameters = []
        for (let i = 0; i < event.item._cfg.model.parameters.length; i++) {
          // 如果节点参数中需要用到文件则获取文件列表
          if (event.item._cfg.model.parameters[i].type.search("file") !== -1) {
            file.getDataSet(1).then(res => {
              this.fileList = res.data.file
            }).catch(err => {
              console.log(err);
            })
          }
          this.parameters.push(event.item._cfg.model.parameters[i])
        }
      })

      // eslint-disable-next-line no-unused-vars
      this.graph.on("canvas:click", (event) => {
        // 点击画布 -> 隐藏参数设置
        this.parameterVisible = false
      })

      this.graph.on("node:mouseenter", (event) => {
        const {item} = event
        this.graph.setItemState(item, 'hover', true)
      })

      this.graph.on("node:mouseleave", (event) => {
        const {item} = event
        this.graph.setItemState(item, 'hover', false)
      })

      // eslint-disable-next-line no-unused-vars
      this.graph.on("node:contextmenu", (event) => {
        event.preventDefault()
        this.$refs.menu.getContextMenu(event.x + 200, event.y + 64 + 38)
      })
    },

    closeDrawer() {
      this.parameterVisible = false
    },
  }
}

document.oncontextmenu = function () {
  return false;
}
</script>

<style>
.g6-component-toolbar {
  position: relative;
  height: 38px;
}

#graphMountNode {
  overflow: hidden;
  position: relative;
  border: 1px solid #ebedf0;
  borderRadius: 2px;
  textAlign: center;
  background: #fafafa;
}

#operationMountNode {
  position: relative;
  list-style-type: none;
  padding: 6px;
  right: 0;
  top: 0;
  background-color: rgba(255, 255, 255, 0.9);
  border: 1px solid #e2e2e2;
  border-radius: 4px;
  font-size: 12px;
  color: #545454;
  margin: 0;
}
</style>