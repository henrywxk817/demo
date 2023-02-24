import axios, {AxiosInstance, AxiosError, AxiosResponse, AxiosRequestConfig} from 'axios';

// const baseURL = 'http://localhost:7401/api/v1'
const baseURL = 'https://api.openai.com/v1'
const openai_api_key = import.meta.env['VITE_OPENAI_API_KEY']


const service:AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 1500000
});

service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        config.headers.Authorization = 'Bearer ' + openai_api_key
        config.headers['content-type'] = 'application/json'
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
