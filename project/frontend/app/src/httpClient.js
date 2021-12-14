import axios from 'axios';

const API_URL = 'http://3.122.41.188:8000';

export const httpClient = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});
