import request from '@/utils/request'

export const rumorPageListService = (params)=>{
  return request.post('/rumor/pagelist', params)
}