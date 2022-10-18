/**axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
 import axios from 'axios';
 
 const service = axios.create({
    //  baseURL: "http://10.136.211.125:8080", // 服务地址
     baseURL: "http://localhost:8080/", // 本地
     timeout: 60000, //设置请求超时时间
     withCredentials: false, //设置跨域是否允许携带凭证(开发环境需要配置，因为要使用跨域；生产环境可能需要将其注释掉！)
     headers: {
        "Content-Type": "application/json;charset=utf-8",
         'Cache-Control': 'no-cache'  //解决缓存问题
     }
 })
 // 设置post请求头
 // service.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'; // 默认值
 service.defaults.headers.post['Content-Type'] = 'application/json;charse=UTF-8'; // 自定义
 
 //设置请求拦截器（在项目中客户端向服务器发送请求之前会进行token校验，token存储在vuex或localstorage中）
 service.interceptors.request.use(
     config => {
         // NProgress.start()
         // 每次发送请求之前判断是否存在token，如果存在，则统一在http请求的header都加上token，
         // 不用每次请求都手动添加了。即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断
         if (localStorage.getItem('Authorization')) {
             config.headers.Authorization = localStorage.getItem('Authorization');
         }
         return config;
     },
     error => {
         return Promise.reject(error);
     })
 
 export default service
 