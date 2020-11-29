import service from "@/request";

export default {
    getTreeData() {
        return service({
            url: "/tree",
            method: "get",
        })
    }
}