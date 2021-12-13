import axios from 'axios';

const API_URL = 'http://3.127.142.97:8000';

export const httpClient = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});
