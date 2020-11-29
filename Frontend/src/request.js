import axios from "axios"

const service = axios.create({
    baseURL: "http://localhost:8000/api/v1/",
    withCredentials: true,
    headers: {
        "Access-Control-Allow-Origin": '*',
    }
})

export default service