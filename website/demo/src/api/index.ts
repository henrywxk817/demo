import request from '../utils/request';


// export const correction = (
//   content: string
// ) =>{
//   return request({
//     url:'/chatGPT/correction',
//     method: 'post',
//     data: {
//       content
//     }
//   })
// }

export const correction = (
  content: string
) =>{
  return request({
    url:'/edits',
    method: 'post',
    data: {
      "model": "text-davinci-edit-001",
      "input": content,
      "instruction": "修改错别字和词语",
    }
  })
}
