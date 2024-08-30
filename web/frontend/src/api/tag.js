import request from '@/utils/request.js'

export const tagListService = (params)=>{
  return request.post('/tag/list', params)
}