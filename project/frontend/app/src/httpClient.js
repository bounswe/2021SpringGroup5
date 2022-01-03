import axios from 'axios';
import Cookies from 'universal-cookie';

const API_URL = 'http://3.122.41.188:8000';

const cookies = new Cookies();

export const httpClient = axios.create({
  baseURL: API_URL,
  withCredentials: true,
});
