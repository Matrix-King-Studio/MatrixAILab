import service from "@/request";

export default {
    getDataSet(id) {
        return service({
            url: `/project/${id}/dataSet/`,
            method: "get",
        })
    },
    getFile(filePath) {
        return service({
            url: filePath,
            method: "get",
        })
    },
    readFile(fileId) {
        return service({
            url: `/file/${fileId}/readFile`,
            method: "get",
        })
    }
}