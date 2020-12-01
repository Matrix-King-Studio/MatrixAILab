import G6 from "@antv/g6"
import store from "@/store";

export default {
    init() {
        G6.registerBehavior("select-node", {
            getDefaultCfg() {
                return {
                    multiple: true,
                    keyCode: 17
                }
            },
            getEvents() {
                return {
                    'node:click': 'onClick',
                    'node:contextmenu': 'onRightClick',
                }
            },
            onClick(event) {
                store.commit('graph/SetSelectNode', event.item)
            },
            onRightClick(event) {
                store.commit('graph/SetSelectNode', event.item)
            },
        })
    }
}