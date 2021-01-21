<template>
  <div>
    <a-modal
      :width="modalWidth"
      :footer="null"
      :forceRender="true"
      v-model="modalVisible"
      title="运行结果">
      <div v-show="data.type === 'float'">
        <h1>{{ data.value }}</h1>
      </div>
      <div v-show="data.type === 'DataFrame'">
        <a-button
          type="primary"
          icon="download"
          size="large"
          @click="downloadFile()">
          Download
        </a-button>
        <div id="dataFrameChartMountNode"></div>
      </div>
    </a-modal>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import graphApi from "@/config/api/graph";
import G2 from "@antv/g2";

export default {
  name: "ContextMenu",
  data() {
    return {
      chart: null,
      modalWidth: 520,
      data: {type: null, value: null},
      modalVisible: false,
    }
  },
  computed: {
    ...mapGetters(["graphId", "selectNode"]),
    selectNode: {
      get() {
        return this.$store.state.graph.selectNode
      },
      set(node) {
        this.$store.commit("graph/SetSelectNode", node)
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
      const graphMountNode = document.getElementById("dataFrameChartMountNode")
      this.chart = new G2.Chart({
        container: graphMountNode,
        width: 1000,
        height: 400
      });
    },

    downloadFile() {
      window.location.href = "http://127.0.0.1:8000/media/file/submisson.csv"
      // graphApi.getRunGraphNodeFile(this.graphId, this.selectNode._cfg.id).then(res => {
      //   console.log(res);
      // }).catch(err => {
      //   console.log(err);
      // })
    },

    getContextMenu(x, y) {
      let data = {
        x: x-400,
        y: y,
        minWidth: 230,
        items: [
          {
            label: '运行结果',
            onClick: () => {
              graphApi.getRunGraphNodeResult(this.graphId, this.selectNode._cfg.id).then(res => {
                this.modalVisible = true
                this.data = res.data
                if (this.data.type === "DataFrame") {
                  this.modalWidth = 1100
                  this.chart.source(this.data.value);
                  this.chart.tooltip({
                    showTitle: false,
                    crosshairs: {
                      type: 'cross'
                    },
                    itemTpl: '<li data-index={index} style="margin-bottom:4px;">' +
                      '<span style="background-color:{color};" class="g2-tooltip-marker"></span>' +
                      '{name}<br/>' + '{value}' + '</li>'
                  });
                  this.draw("Id", "SalePrice")
                }
              }).catch(err => {
                console.log(err);
              })
            },
            disabled: false,
          },
        ]
      }
      this.$contextmenu(data)
    },

    draw(x, y) {
      this.chart.clear()
      this.chart.point().position(`${x}*${y}`).size(4).shape('circle').opacity(0.65)
        .tooltip(`Id*${x}*${y}`, function (Id, param1, param2) {
          return {
            name: Id,
            value: param1 + ', ' + param2 + ''
          };
        });
      this.chart.render();
    },
  }
}
</script>

<style scoped>

</style>