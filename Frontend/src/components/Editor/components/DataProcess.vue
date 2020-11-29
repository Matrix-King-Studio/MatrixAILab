<template>
  <div>
    <a-tabs
      default-active-key="1">
      <a-tab-pane
        key="1"
        tab="预览">
        <a-table
          size="small"
          :pagination="false"
          :scroll="{x: 10000, y: 400}"
          :columns="columns"
          :data-source="data">
        </a-table>
      </a-tab-pane>
      <a-tab-pane
        key="3"
        tab="可视化"
        :forceRender="true">
        <span>X:</span>
        <a-select
          v-model="xLabel"
          style="width: 120px">
          <a-select-option
            v-for="column in columns"
            :value="column.key"
            :key="column.key">
            {{ column.key }}
          </a-select-option>
        </a-select>
        <a-divider type="vertical"/>
        <span>Y:</span>
        <a-select
          v-model="yLabel"
          style="width: 120px">
          <a-select-option
            v-for="column in columns"
            :value="column.key"
            :key="column.key">
            {{ column.key }}
          </a-select-option>
        </a-select>
        <div
          id="chartMountNode"></div>
      </a-tab-pane>
    </a-tabs>
  </div>
</template>

<script>
import G2 from '@antv/g2';
import file from "@/config/api/file";
import {mapGetters} from "vuex";

export default {
  name: "DataProcess",
  props: ["fileId"],
  data() {
    return {
      columns: [],
      data: [],
      xLabel: "",
      yLabel: ""
    }
  },
  computed: {
    ...mapGetters(["chart"]),
    chart: {
      get() {
        return this.$store.state.chart.chart
      },
      set(chart) {
        this.$store.commit("chart/SetChart", chart)
      }
    },
  },
  watch: {
    xLabel(value) {
      this.draw(value, this.yLabel)
    },
    yLabel(value) {
      this.draw(this.xLabel, value)
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.init();
    });
  },
  methods: {
    init() {
      this.readFile()

      const graphMountNode = document.getElementById("chartMountNode")
      this.chart = new G2.Chart({
        container: graphMountNode,
        width: 1000,
        height: 400
      });
    },
    readFile() {
      file.readFile(this.fileId).then(res => {
        this.data = res.data.data
        this.columns = res.data.columns

        this.chart.source(this.data);
        this.chart.tooltip({
          showTitle: false,
          crosshairs: {
            type: 'cross'
          },
          itemTpl: '<li data-index={index} style="margin-bottom:4px;">' +
            '<span style="background-color:{color};" class="g2-tooltip-marker"></span>' +
            '{name}<br/>' + '{value}' + '</li>'
        });

        this.xLabel = "LotArea"
        this.yLabel = "SalePrice"
        this.draw(this.xLabel, this.yLabel)
      }).catch(err => {
        console.log(err);
      })
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
    selectX(x) {
      this.xLabel = x
      this.draw(x, this.yLabel)
    },
    selectY(y) {
      this.yLabel = y
      this.draw(this.xLabel, y)
    }
  }
}
</script>

<style scoped>
.ant-table td {
  white-space: nowrap;
}
</style>