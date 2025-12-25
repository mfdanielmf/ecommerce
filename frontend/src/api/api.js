import axios from 'axios'

export default (url = 'http://localhost:8080') => {
  return axios.create({
    baseURL: url,
  })
}
