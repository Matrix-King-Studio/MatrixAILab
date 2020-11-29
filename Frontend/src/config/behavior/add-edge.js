import G6 from "@antv/g6"

let startPoint = null
let startPointId = null
let startItem = null
let endPoint = {}
let activeItem = null
let curInPoint = null

const addEdge = {
    init() {
        G6.registerBehavior("add-edge", {
            hasTran: false,
            getEvents() {
                return {
                    mousemove: "onMousemove",
                    mouseup: "onMouseup",
                    mousedown: "onMouseDown",
                    "node:mouseover": "onMouseover",
                    "node:mouseleave": "onMouseleave"
                }
            },
            onMouseup(event) {
                const item = event.item
                if (item && item.getType() === "node") {
                    const group = item.getContainer()
                    if (event.target.attrs.isInPoint) {
                        const children = group.cfg.children
                        children.map(child => {
                            if (child.attrs.isInPointOut && child.attrs.parent === event.target.attrs.parent) {
                                activeItem = child
                            }
                        })
                        curInPoint = event.target
                    } else if (event.target.attrs.isInPointOut) {
                        activeItem = event.target
                        const children = group.cfg.children
                        children.map(child => {
                            if (child.attrs.isInPoint && child.attrs.parent === event.target.attrs.parent) {
                                curInPoint = child
                            }
                        })
                    }
                    if (curInPoint) {
                        // 判断该入点是否已经被连接
                        let checkLinkedEdges = this.graph.findAll("edge", edge => {
                            return edge.getModel().endPointId === curInPoint.attrs.id
                        })
                        // 判断该入edge.getModel点是否是该node的入点
                        let isInPointInStartNode = curInPoint.cfg.parent.get("item") === startItem

                        if (!checkLinkedEdges.length && activeItem && !isInPointInStartNode) {
                            const endX = parseInt(curInPoint.attrs.x)
                            const endY = parseInt(curInPoint.attrs.y)
                            endPoint = { x: endX, y: endY }
                            if (this.edge) {
                                this.graph.removeItem(this.edge)
                                let data = {
                                    id: `edge${Date.parse(new Date())}`,
                                    source: startItem,
                                    target: item,
                                    start: startPoint,
                                    end: endPoint,
                                    startPointId: startPointId,
                                    endPointId: curInPoint.attrs.id,
                                    shape: "customEdge",
                                    type: "edge"
                                }
                                this.graph.add("edge", data)
                                console.log(this.graph.save());
                            }
                        } else if (this.edge) {
                            this.graph.removeItem(this.edge)
                        }
                    } else if (this.edge) {
                        this.graph.removeItem(this.edge)
                    }
                } else if (this.edge) {
                    this.graph.removeItem(this.edge)
                }

                this.graph.paint()
                startPoint = null
                startPointId = null
                startItem = null
                endPoint = {}
                activeItem = null
                curInPoint = null
                this.graph.setMode("default")
            },
            onMousemove(event) {
                const item = event.item
                if (!startPoint && event.target.attrs.isOutPoint) {
                    const startX = parseInt(event.target.attrs.x)
                    const startY = parseInt(event.target.attrs.y)
                    startPoint = { x: startX, y: startY }
                    startPointId = event.target.attrs.parent ? event.target.attrs.parent : event.target.attrs.id
                    startItem = item

                    this.edge = this.graph.add("edge", {
                        source: { x: event.x, y: event.y },
                        target: item,
                        start: startPoint,
                        end: startPoint,
                        type: "link-edge"
                    })
                } else {
                    const point = { x: event.x, y: event.y }
                    if (this.edge) {
                        // 增加边的过程中，移动时边跟着移动
                        this.graph.updateItem(this.edge, {
                            //  start: startPoint,
                            target: point
                        })
                    }
                }
            },
            onMouseover(event) {
                const item = event.item
                if (item && item.getType() === "node") {
                    if (event.target.attrs.isInPointOut && !this.hasTran) {
                        event.target.transform([
                            ["t", 0, 3],
                            ["s", 1.2, 1.2],
                        ])
                        this.hasTran = true
                    }
                    this.graph.paint()
                }
            },
            onMouseleave() {
                this.graph.find("node", node => {
                    const group = node.get("group")
                    const children = group.cfg.children
                    children.map(child => {
                        if (child.attrs.isInPointOut) {
                            child.resetMatrix()
                        }
                    })
                })
                this.hasTran = false
                this.graph.paint()
            }
        });
    }
}

export default addEdge