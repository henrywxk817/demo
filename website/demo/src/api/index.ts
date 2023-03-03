import request from '../utils/request';


export const correction = (
  content: string
) =>{
  return request({
    url:'/chatGPT/correction',
    method: 'post',
    data: {
      content: "修改错别字：" + content
    }
  })
}

// export const correction = (
//   content: string
// ) =>{
//   return request({
//     url:'/edits',
//     method: 'post',
//     data: {
//       "model": "text-davinci-edit-001",
//       "input": content,
//       "instruction": "修改错别字和词语",
//     }
//   })
// }

// export const correction = (
//   content: string
// ) =>{
//   return request({
//     url:'/completions',
//     method: 'post',
//     data: {
//       "model": "text-davinci-003",
//       "prompt": "检查下列文本的错别字并且修正：\n[文本]:" + content + "\n[修正后的文本]:",
//       "temperature": 0,
//       "max_tokens":1000,
//       "top_p":0.8,
//       "frequency_penalty":0.0,
//       "presence_penalty":0.0
//     }
//   })
// }