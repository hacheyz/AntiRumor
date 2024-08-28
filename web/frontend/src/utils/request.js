//定制请求的实例

//导入axios  npm install axios
import axios from 'axios';

//定义一个变量,记录公共的前缀  ,  baseURL
const baseURL = 'http://localhost:8080/';
const instance = axios.create({baseURL})

import {useTokenStore} from '@/stores/token.js'
//添加请求拦截器
instance.interceptors.request.use(
  (config) => {
    //请求前的回调
    //添加token
    const tokenStore = useTokenStore();
    //判断有没有token
    if (tokenStore.token) {
      config.headers.Authorization = tokenStore.token
    }
    return config;
  },
  (err) => {
    //请求错误的回调
    Promise.reject(err)
  }
)

export default instance;