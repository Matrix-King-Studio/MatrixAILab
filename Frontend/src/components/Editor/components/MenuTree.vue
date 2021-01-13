<template>
  <div class="sider">
    <div class="left">
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
    <div class="resize"></div>
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
        //maxWidth: '300px',
      },
     
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
  mounted() {
    this.dragControllerDiv()
  },
  methods: {
    dragControllerDiv: function () {
    var resize = document.getElementsByClassName('resize');
    var left = document.getElementsByClassName('left');
    var box = document.getElementsByClassName('sider');
    for (let i = 0; i < resize.length; i++) {
        // 鼠标按下事件
        resize[i].onmousedown = function (e) {
            //颜色改变提醒
            resize[i].style.background = '#818181';
            var startX = e.clientX;
            resize[i].left = resize[i].offsetLeft;
            // 鼠标拖动事件
            document.onmousemove = function (e) {
                var endX = e.clientX;
                var moveLen = resize[i].left + (endX - startX); // （endx-startx）=移动的距离。resize[i].left+移动的距离=左边区域最后的宽度

                if (moveLen < 200) moveLen = 200; // 左边区域的最小宽度为32px
                if(moveLen > 400) moveLen = 400 ;
                resize[i].style.left = moveLen; // 设置左侧区域的宽度

                for (let j = 0; j < left.length; j++) {
                  left[j].style.width = moveLen + 'px'; 
                  
                }
            };

            // 鼠标松开事件
            document.onmouseup = function (evt) {
                //颜色恢复
                resize[i].style.background = '#d6d6d6';
                document.onmousemove = null;
                document.onmouseup = null;
                resize[i].releaseCapture && resize[i].releaseCapture(); //当你不在需要继续获得鼠标消息就要应该调用ReleaseCapture()释放掉
            };
            resize[i].setCapture && resize[i].setCapture(); //该函数在属于当前线程的指定窗口里设置鼠标捕获
            return false;
        };
      }
    },

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
.sider{
  margin-right: 10px;
  position: relative;
  height: 100%;
}
.left{
  width: calc(100% - 0px);  /*左侧初始化宽度*/   
  height: 100%;
  background: #FFFFFF;
}
.ant-tree {
  overflow: auto;
  max-height: 800px;
}
.resize{
  cursor: col-resize;
  position: absolute;
  top: 0;
  right: -10px;
  background-color: #d6d6d6;
  border-radius: 5px;
  width: 10px;
  height: 100%;
  background-size: cover;
  background-position: center;
  /*z-index: 99999;*/
  font-size: 32px;
  color: white;
}
</style>