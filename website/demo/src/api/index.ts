import request from '../utils/request';


export const correction = (
  content: string
) =>{
  return request({
    url:'/chatGPT/correction',
    method: 'post',
    data: {
      content
    }
  })
}
