import axios from "axios"

const service = axios.create({
    baseURL: "http://39.96.87.195:8000/api/v1/",
    withCredentials: true,
    headers: {
        "Access-Control-Allow-Origin": '*',
    }
})

export default service