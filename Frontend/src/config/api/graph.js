import service from "@/request";

export default {
    saveGraph(graphId, graphData) {
        return service({
            url: `/graph/${graphId}/data/`,
            method: "POST",
            data: graphData
        })
    }
}