import axios, {AxiosInstance, AxiosError, AxiosResponse, AxiosRequestConfig} from 'axios';

// const baseURL = 'http://localhost:7401/api/v1'
const baseURL = 'https://www.henryapi.top/api/v1'


const service:AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 1500000
});

service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        return config;
    },
    (error: AxiosError) => {
        console.log(error);
        return Promise.reject("error");
    }
);

service.interceptors.response.use(
    (response: AxiosResponse) => {
        if (response.status === 200) {
            return response;
        } else {
            if (response.status === 429) {
                Promise.reject("请求太过频繁，请稍后重试");
            }
            else{
                Promise.reject("error");
            }
           
        }
    },
    (error: AxiosError) => {
        console.log(error);
        return Promise.reject("error");
    }
);

export default service;
