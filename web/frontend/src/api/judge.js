import request from '@/utils/request.js'

export const questionPageListService = (params)=>{
  return request.post('/question/pagelist', params)
}

export const questionAddService = (params, query) => {
  return request.post('/question/add', params, {
    params: query, // 使用 params 选项传递查询参数
  });
};

export const questionAddAgreeService = (id)=>{
  return request.get('/question/addAgree?id='+id)
}

export const questionAddDisagreeService = (id)=>{
  return request.get('/question/addDisagree?id='+id)
}