import service from "@/request";

export default {
    login(id) {
        return service({
            url: `/user/login/`,
            method: "get",
        })
    }
}