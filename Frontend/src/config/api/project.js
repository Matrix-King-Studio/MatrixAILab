import service from "@/request";

export default {
    getProjectInfo(id) {
        return service({
            url: `/project/${id}`,
            method: "get",
        })
    },

    getProjectGraph(id) {
        return service({
            url: `/project/${id}/graph/`,
            method: "get",
        })
    }
}