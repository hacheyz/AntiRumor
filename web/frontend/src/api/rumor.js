import request from '@/utils/request.js'

export const rumorPageListService = (params)=>{
  return request.post('/rumor/pagelist', params)
}