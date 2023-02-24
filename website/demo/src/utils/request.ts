import axios, {AxiosInstance, AxiosError, AxiosResponse, AxiosRequestConfig} from 'axios';
// import process from 'process'

// const baseURL = 'http://localhost:7401/api/v1'
const baseURL = 'https://api.openai.com/v1'
const openai_api_key = import.meta.env['openai_api_key']


const service:AxiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 15000
});

service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        config.headers.Authorization = 'Bearer ' + openai_api_key
        config.headers['content-type'] = 'application/json'
        return config;
    },
    (error: AxiosError) => {
        console.log(error);
        return Promise.reject();
    }
);

service.interceptors.response.use(
    (response: AxiosResponse) => {
        if (response.status === 200) {
            return response;
        } else {
            Promise.reject();
        }
    },
    (error: AxiosError) => {
        console.log(error);
        return Promise.reject();
    }
);

export default service;
