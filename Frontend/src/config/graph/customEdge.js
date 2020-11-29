import G6 from "@antv/g6"

const MIN_ARROW_SIZE = 3

const customEdge = {
    init() {
        const dashArray = [
            [0, 1],
            [0, 2],
            [1, 2],
            [0, 1, 1, 2],
            [0, 2, 1, 2],
            [1, 2, 1, 2],
            [2, 2, 1, 2],
            [3, 2, 1, 2],
            [4, 2, 1, 2]
        ]

        const lineDash = [4, 2, 1, 2]
        const interval = 9

        /**
         * 自定义的边 customEdge
         */
        G6.registerEdge('customEdge', {
            /**
             * 绘制边，包含文本
             * @param  {Object} cfg 边的配置项
             * @param  {G.Group} group 边的容器
             * @return {G.Shape} 绘制的图形，通过 node.get('keyShape') 可以获取到
             */
            draw(cfg, group) {
                if (cfg.sourceNode && cfg.targetNode && group.attrs) {
                    let sourceNode, targetNode, start, end
                    if (typeof (cfg.source) === 'string') {
                        cfg.source = cfg.sourceNode
                    }
                    if (!cfg.start) {
                        cfg.start = {
                            x: 0,
                            y: 17
                        }
                    }
                    if (!cfg.end) {
                        cfg.end = {
                            x: 0,
                            y: -17
                        }
                    }

                    if (!cfg.source.x) {
                        sourceNode = cfg.source.getModel()
                        // console.log(sourceNode)
                        start = { x: sourceNode.x + cfg.start.x, y: sourceNode.y + cfg.start.y }
                    } else {
                        start = cfg.source
                    }

                    if (typeof (cfg.target) === 'string') {
                        cfg.target = cfg.targetNode
                    }

                    if (!cfg.target.x) {
                        targetNode = cfg.target.getModel()
                        end = { x: targetNode.x + cfg.end.x, y: targetNode.y + cfg.end.y }
                    } else {
                        end = cfg.target
                    }

                    let hgap = Math.abs(end.x - start.x)
                    let path = [
                        ['M', start.x, start.y],
                        [
                            'C',
                            start.x,
                            start.y + hgap / (hgap / 50),
                            end.x,
                            end.y - hgap / (hgap / 50),
                            end.x,
                            end.y - 4
                        ],
                        [
                            'L',
                            end.x,
                            end.y
                        ]
                    ]
                    let lineWidth = 1
                    lineWidth = lineWidth > MIN_ARROW_SIZE ? lineWidth : MIN_ARROW_SIZE
                    const width = lineWidth * 10 / 3
                    const halfHeight = lineWidth * 4 / 3
                    const radius = lineWidth * 4
                    const endArrowPath = [
                        ['M', -width, halfHeight],
                        ['L', 0, 0],
                        ['L', -width, -halfHeight],
                        ['A', radius, radius, 0, 0, 1, -width, halfHeight],
                        ['Z']
                    ]

                    // 绘画label
                    // let sourcePoint
                    // for (let index in sourceNode.information.inputattibute) {
                    //     let pd = sourceNode.information.inputattibute[index]
                    //     if (pd.id === cfg.startPointId) {
                    //         sourcePoint = pd
                    //     }
                    // }
                    // for (let index in sourceNode.information.outputattibute) {
                    //     let pd = sourceNode.information.outputattibute[index]
                    //     if (pd.id === cfg.startPointId) {
                    //         sourcePoint = pd
                    //     }
                    // }
                    // group.addShape('text', {
                    //     attrs: {
                    //         text: sourcePoint.name,
                    //         fill: '#595959',
                    //         textAlign: 'start',
                    //         textBaseline: 'middle',
                    //         x: (start.x + end.x) / 2,
                    //         y: (start.y + end.y) / 2,
                    //     }
                    // })
                    return group.addShape('path', {
                        attrs: {
                            id: `edge${Date.parse(new Date())}`,
                            path: path,
                            stroke: '#b8c3ce',
                            lineAppendWidth: 10,
                            endArrow: {
                                path: endArrowPath,
                            }
                        }
                    })
                }
            },

            /**
             * 绘制后的附加操作，默认没有任何操作
             * @param  {Object} cfg 边的配置项
             * @param  {G.Group} group 边的容器
             */
            afterDraw(cfg, group) {
                if (cfg.sourceNode && cfg.targetNode && group.attrs) {
                    if (cfg.source.getModel().isDoingStart && cfg.target.getModel().isDoingEnd) {
                        const shape = group.get('children')[0]
                        const length = shape.getTotalLength()
                        let totalArray = []
                        for (let i = 0; i < length; i += interval) {
                            totalArray = totalArray.concat(lineDash)
                        }
                        let index = 0
                        shape.animate({
                            onFrame() {
                                const cfg = {
                                    lineDash: dashArray[index].concat(totalArray)
                                }
                                index = (index + 1) % interval
                                return cfg
                            },
                            repeat: true
                        }, 3000)
                    }
                }
            },

            /**
             * 设置边的状态，主要是交互状态，业务状态请在 draw 方法中实现
             * 单图形的边仅考虑 selected、active 状态，有其他状态需求的用户自己复写这个方法
             * @param  {String} name 状态名称
             * @param  {Object} value 状态值
             * @param  {Edge} edge 边
             */
            setState(name, value, edge) {
                const group = edge.getContainer()
                const shape = group.get('children')[0]
                const selectStyles = () => {
                    shape.attr('stroke', '#6ab7ff')
                }
                const unSelectStyles = () => {
                    shape.attr('stroke', '#b8c3ce')
                }
                switch (name) {
                    case 'selected':
                    case 'hover':
                        if (value) {
                            selectStyles()
                        } else {
                            unSelectStyles()
                        }
                        break
                }
            }
        })

        /**
         * 自定义的边 link-edge
         */
        G6.registerEdge('link-edge', {
            /**
             * 绘制边，包含文本
             * @param  {Object} cfg 边的配置项
             * @param  {G.Group} group 边的容器
             * @return {G.Shape} 绘制的图形，通过 node.get('keyShape') 可以获取到
             */
            draw(cfg, group) {
                let sourceNode, targetNode, start, end
                if (!cfg.source.x) {
                    sourceNode = cfg.source.getModel()
                    start = { x: sourceNode.x + cfg.start.x, y: sourceNode.y + cfg.start.y }
                } else {
                    start = cfg.source
                }
                if (!cfg.target.x) {
                    targetNode = cfg.target.getModel()
                    end = { x: targetNode.x + cfg.end.x, y: targetNode.y + cfg.end.y }
                } else {
                    end = cfg.target
                }

                let path = []
                path = [
                    ['M', start.x, start.y],
                    ['L', end.x, end.y]
                ]
                return group.addShape('path', {
                    attrs: {
                        id: `edge${Date.parse(new Date())}`,
                        path: path,
                        stroke: '#1890FF',
                        strokeOpacity: 0.9,
                        lineDash: [5, 5]
                    }
                })
            },
        })
    }
}

export default customEdge
