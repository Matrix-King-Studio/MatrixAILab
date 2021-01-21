import service from "@/request";

export default {
    login(id) {
        return service({
            url: `/admin/login/`,
            method: "post",
        })
    }
}