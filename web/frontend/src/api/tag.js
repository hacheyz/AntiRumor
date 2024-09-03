import request from '@/utils/request.js'

export const tagListService = (params)=>{
  return request.post('/tag/list', params)
}

export const tagListWithRelateNumService = (params)=>{
  return request.post('/tag/listWithRelateNum', params)
}