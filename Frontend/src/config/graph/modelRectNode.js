import G6 from "@antv/g6"

const modelRectNode = {
    init() {
        G6.registerNode('modelRectNode', {
            /**
             * 绘制节点/边，包含文本
             * @param  {Object} cfg 节点的配置项
             * @param  {G.Group} group 节点的容器
             * @return {G.Shape} 绘制的图形，通过node.get('keyShape') 可以获取到
             */
            draw(cfg, group) {
                const width = cfg.size[0]
                const height = cfg.size[1]

                // 此处必须有偏移 不然drag-node错位
                const offsetX = -width / 2
                const offsetY = -height / 2
                const label = cfg.label
                const id = `node${Date.parse(new Date())}`

                const shape = group.addShape("rect", {
                    attrs: {
                        id: id,
                        x: offsetX,
                        y: offsetY,
                        width: width,
                        height: height,
                        stroke: "#99CCFF",
                        fill: "#FFFFFF",
                        radius: 4,
                    },
                })
                group.addShape("rect", {
                    attrs: {
                        x: offsetX,
                        y: offsetY,
                        width: 4,
                        height: height,
                        fill: "#66CCFF",
                        parent: id,
                        radius: [4, 0, 0, 4]
                    },
                })
                group.addShape('text', {
                    attrs: {
                        id: `label${Date.parse(new Date())}`,
                        x: offsetX + width / 2,
                        y: offsetY + height / 2,
                        textAlign: 'center',
                        textBaseline: 'middle',
                        text: label,
                        parent: id,
                        fill: "#000000",
                        fontSize: cfg.fontSize
                    }
                })

                // 绘制输入点
                if (cfg.inputs) {
                    let inputsLength = cfg.inputs.length
                    for (let i = 0; i < inputsLength; i++) {
                        let point = cfg.inputs[i]
                        let x = width * ((i + 1) / (inputsLength + 1)), y = 0
                        group.addShape('circle', {
                            attrs: {
                                id: `circle-${point.name}-InPointOut-${Date.parse(new Date())}`,
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY,
                                r: 10,
                                isInPointOut: true,
                                fill: '#1890ff',
                                opacity: 0
                            }
                        })
                        group.addShape('text', {
                            attrs: {
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY - 18,
                                isInPointText: true,
                                textAlign: 'center',
                                textBaseline: 'top',
                                text: point.name,
                                fill: '#1890ff',
                                opacity: 0,
                            }
                        })
                        group.addShape('circle', {
                            attrs: {
                                id: `circle-${point.name}-InPoint-${Date.parse(new Date())}`,
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY,
                                r: 6,
                                isInPoint: true,
                                fill: '#fff',
                                stroke: '#1890ff',
                                opacity: 0
                            }
                        })
                        point.id = id
                    }
                }

                // 绘制输出点
                if (cfg.outputs) {
                    let outputsLength = cfg.outputs.length
                    for (let i = 0; i < outputsLength; i++) {
                        let point = cfg.outputs[i]
                        let x = width * ((i + 1) / (outputsLength + 1)), y = height
                        group.addShape('circle', {
                            attrs: {
                                id: `circle-${point.name}-OutPointOut-${Date.parse(new Date())}`,
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY,
                                r: 10,
                                isOutPointOut: true,
                                fill: '#1890ff',
                                opacity: 0
                            }
                        })
                        group.addShape('text', {
                            attrs: {
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY + 21,
                                isOutPointText: true,
                                textAlign: 'center',
                                textBaseline: 'bottom',
                                text: point.name,
                                fill: '#1890ff',
                                opacity: 0
                            }
                        })
                        group.addShape('circle', {
                            attrs: {
                                id: `circle-${point.name}-OutPoint-${Date.parse(new Date())}`,
                                parent: id,
                                x: x + offsetX,
                                y: y + offsetY,
                                r: 6,
                                isOutPoint: true,
                                fill: '#fff',
                                stroke: '#1890ff',
                                opacity: 0
                            }
                        })
                        point.id = id
                    }
                }
                return shape
            },

            /**
             * 绘制后的附加操作，默认没有任何操作
             * @param  {Object} cfg 节点的配置项
             * @param  {G.Group} group 节点的容器
             */
            // eslint-disable-next-line no-unused-vars
            afterDraw(cfg, group) {
            },

            /**
             * 更新节点，包含文本
             * @override
             * @param  {Object} cfg 节点的配置项
             * @param  {Node} node 节点
             */
            // eslint-disable-next-line no-unused-vars
            update(cfg, node) {
            },

            /**
             * 更新节点后的操作，一般同 afterDraw 配合使用
             * @override
             * @param  {Object} cfg 节点的配置项
             * @param  {Node} node 节点
             */
            // eslint-disable-next-line no-unused-vars
            afterUpdate(cfg, node) {
            },

            /**
             * 设置节点的状态，主要是交互状态，业务状态请在 draw 方法中实现
             * 单图形的节点仅考虑 selected、active 状态，有其他状态需求的用户自己复写这个方法
             * @param  {String} name 状态名称
             * @param  {Object} value 状态值
             * @param  {Node} node 节点
             */
            // eslint-disable-next-line no-unused-vars
            setState(name, value, node) {
                const group = node.getContainer();
                const shape = group.get("children")[0];

                const childes = group.findAll(child => {
                    return child.attrs.parent === shape.attrs.id
                });
                const circles = group.findAll(circle => {
                    return circle.attrs.isInPoint || circle.attrs.isOutPoint;
                });
                const texts = group.findAll(text => {
                    return text.attrs.isInPointText || text.attrs.isOutPointText;
                });

                const selectStyles = () => {
                    shape.attr("fill", "#f3f9ff");
                    shape.attr("stroke", "#6ab7ff");
                    shape.attr("cursor", "move");
                    childes.forEach(child => {
                        child.attr("cursor", "move");
                    });
                    circles.forEach(circle => {
                        circle.attr('opacity', 1)
                    })
                    texts.forEach(text => {
                        text.attr('opacity', 1)
                    })
                };
                const unSelectStyles = () => {
                    shape.attr("fill", "#fff");
                    shape.attr("stroke", "#ced4d9");
                    circles.forEach(circle => {
                        circle.attr('opacity', 0)
                    })
                    texts.forEach(text => {
                        text.attr('opacity', 0)
                    })
                };
                switch (name) {
                    case "selected":
                        if (value) {
                            selectStyles()
                        } else {
                            unSelectStyles()
                        }
                        break
                    case "hover":
                        if (value) {
                            selectStyles()
                        } else {
                            unSelectStyles()
                        }
                        break
                }
            },

            /**
             * 获取控制点
             * @param  {Object} cfg 节点、边的配置项
             * @return {Array|null} 控制点的数组,如果为 null，则没有控制点
             */
            // eslint-disable-next-line no-unused-vars
            getAnchorPoints(cfg) {}
        }, "modelRect");
    }
}

export default modelRectNode