import service from "@/request";

export default {
    saveGraph(graphId, graphData) {
        return service({
            url: `/graph/${graphId}/data/`,
            method: "POST",
            data: graphData
        })
    },
    runGraph(graphId) {
        return service({
            url: `/graph/${graphId}/run/`,
            method: "GET",
        })
    },
    getRunGraphNodeResult(graphId, nodeId) {
        return service({
            url: `/graph/${graphId}/node/`,
            method: "GET",
            params: {nodeId: nodeId},
        })
    }
}