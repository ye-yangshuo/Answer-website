import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/',
  headers: {
    'Content-Type': 'application/json',
    'Content-Type' : 'multipart/form-data',

  },
  withCredentials: true,

});

axiosInstance.interceptors.request.use(
  function (config)
  {
    config.headers['Authorization'] = 'Bearer ' + sessionStorage.getItem('accessToken')
    return config;
  }
);

// 添加响应拦截器


export default axiosInstance;
