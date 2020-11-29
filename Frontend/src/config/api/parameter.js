import service from "@/request";

export default {
    saveParameter(id) {
        return service({
            url: `/project/${id}/dataSet/`,
            method: "get",
        })
    }
}