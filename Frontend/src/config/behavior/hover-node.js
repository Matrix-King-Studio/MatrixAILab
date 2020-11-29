import G6 from "@antv/g6";

export default {
    init() {
        G6.registerBehavior('hover-edge', {
            getEvents() {
                return {
                    'node:mouseover': 'onMouseover',
                    'node:mouseleave': 'onMouseleave',
                    'node:mousedown': 'onMousedown',
                    'node:mouseup': 'onMouseup',
                    'node:mousemove': 'onMouseMove'
                }
            },
            // eslint-disable-next-line no-unused-vars
            onMouseMove(event) {},
            onMouseover(event) {
                const self = this
                const item = event.item
                const graph = self.graph
                const group = item.getContainer()
                group.find(g => {
                    if (g.attrs.isOutPointText) {
                        g.attr('opacity', 0.5)
                    }
                })
                if (event.target.attrs.isOutPoint) {
                    group.find(g => {
                        if (g.attrs.isInPoint || g.attrs.isOutPoint) {
                            g.attr('fill', '#fff')
                        }
                        if (g.attrs.isOutPoint) {
                            if (g.attrs.id === event.target.attrs.parent) {
                                group.find(gr => {
                                    if (gr.attrs.id === g.attrs.id) {
                                        gr.attr('fill', '#1890ff')
                                        gr.attr('opacity', 1)
                                    }
                                })
                            }
                            if (g.attrs.id === event.target.attrs.id) {
                                g.attr('fill', '#1890ff')
                                g.attr('opacity', 1)
                            }
                        }
                    })
                    this.graph.paint()
                }
                if (item.hasState('selected')) {
                    // return
                } else {
                    if (self.shouldUpdate.call(self, event)) {
                        graph.setItemState(item, 'hover', true)
                    }
                }
                graph.paint()
            },
            onMouseleave(event) {
                const self = this
                const item = event.item
                const graph = self.graph
                const group = item.getContainer()
                group.find(g => {
                    if (g.attrs.isOutPointText) {
                        g.attr('opacity', 0)
                    }
                })
                group.find(g => {
                    if (g.attrs.isInPoint || g.attrs.isOutPoint) {
                        g.attr('fill', '#fff')
                    }
                })
                if (self.shouldUpdate.call(self, event)) {
                    if (!item.hasState('selected'))
                        graph.setItemState(item, 'hover', false)
                }
                graph.paint()
            },
            onMousedown(event) {
                if (event.target.attrs.isOutPoint) {
                    this.graph.setMode('addEdge')
                } else {
                    // this.graph.setMode('moveNode')
                }
            },
            // eslint-disable-next-line no-unused-vars
            onMouseup(event) {
                // console.log(event);
            }
        })
    }
}
