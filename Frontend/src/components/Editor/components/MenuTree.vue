<template>
  <div>
    <a-input-search
      style="margin-bottom: 8px"
      placeholder="Search"
      @change="onChange"/>
    <a-tree
      showLine
      v-if="treeData.length > 0"
      :style="treeStyle"
      :defaultExpandAll="false"
      :draggable="true"
      :tree-data="treeData"
      @dragend="dragend"
      @dragover="dragover"
      @dragenter="dragenter"
      @dragleave="dragleave"
      @dragstart="dragstart"
      @expand="onExpand">
      <template slot="name" slot-scope="{ name }">
        <span v-if="name.indexOf(searchValue) > -1">
          {{ name.substr(0, name.indexOf(searchValue)) }}
          <span style="color: #f50">{{ searchValue }}</span>
          {{ name.substr(name.indexOf(searchValue) + searchValue.length) }}
        </span>
        <span v-else>{{ name }}</span>
      </template>
    </a-tree>
  </div>
</template>

<script>
import tree from "@/config/api/tree";
import {mapGetters} from "vuex";

export default {
  name: "MenuTree",
  data() {
    return {
      searchValue: '',
      treeData: [],
      treeStyle: {
        overflow: 'auto',
        maxHeight: `${document.body.clientHeight - 38 - 68}px`,
        maxWidth: '300px',
      }
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
    this.getTreeData()
  },
  methods: {
    getTreeData() {
      tree.getTreeData().then(res => {
        this.treeData = Object.values(res.data.data)
        this.treeData.forEach(item => {
          item.scopedSlots = {
            title: 'name',
            key: "id",
          }
        })
      }).catch(err => {
        console.log(err);
      })
    },

    /**
     * dragend 触发时调用
     * @param event
     * @param node
     */
    dragend({event, node}) {
      let input = [], output = [], parameters = []
      node.dataRef.parameters.forEach(item => {
        if (item.category === "input") {
          input.push(item)
        } else if (item.category === "output") {
          output.push(item)
        } else if (item.category === "parameter") {
          parameters.push(item)
          if (item.type === "bool") {
            item.value = item.value === "True"
          }
        }
      })
      const data = {
        id: `node${Date.parse(new Date())}`,
        x: this.graph.getPointByClient(event.x, event.y).x,
        y: this.graph.getPointByClient(event.x, event.y).y,
        size: [270, 50],
        shape: "modelRectNode",
        type: "node",
        fontSize: 14,
        label: node.dataRef.name,
        inputs: input,
        outputs: output,
        parameters: parameters,
      }

      this.graph.add("node", data)
    },

    /**
     * dragenter 触发时调用
     * @param event
     * @param node
     * @param expandedKeys
     */
    // eslint-disable-next-line no-unused-vars
    dragenter({event, node, expandedKeys}) {
      // console.log("dragenter", event, node, expandedKeys);
    },

    /**
     * dragleave 触发时调用
     * @param event
     * @param node
     */
    // eslint-disable-next-line no-unused-vars
    dragleave({event, node}) {
      // console.log("dragleave", event, node);
    },

    /**
     * dragover 触发时调用
     * @param event
     * @param node
     */
    // eslint-disable-next-line no-unused-vars
    dragover({event, node}) {
      // console.log("dragover", event, node);
    },

    /**
     * 开始拖拽时调用
     * @param event
     * @param node
     */
    // eslint-disable-next-line no-unused-vars
    dragstart({event, node}) {
      // console.log("dragstart", event, node);
    },

    onExpand(expandedKeys) {
      this.expandedKeys = expandedKeys;
      this.autoExpandParent = true;
    },

    onChange(e) {
      const getParentKey = (key, tree) => {
        let parentKey;
        for (let i = 0; i < tree.length; i++) {
          const node = tree[i];
          if (node.children) {
            if (node.children.some(item => item.key === key)) {
              parentKey = node.key;
            } else if (getParentKey(key, node.children)) {
              parentKey = getParentKey(key, node.children);
            }
          }
        }
        return parentKey;
      };

      const value = e.target.value;
      const expandedKeys = this.treeData.map(item => {
        if (item.name.indexOf(value) > -1) {
          return getParentKey(item.id, this.treeData);
        }
        return null;
      })
        .filter((item, i, self) => item && self.indexOf(item) === i);
      Object.assign(this, {
        expandedKeys,
        searchValue: value,
        autoExpandParent: true,
      });
    },
  }
}
</script>

<style lang="scss" scoped>
.ant-tree {
  overflow: auto;
  max-height: 800px;
}
</style>