import axios from 'axios';

const API_URL = ''; // todo add API_URL

export const httpClient = axios.create({
    baseURL: API_URL,
    withCredentials: true,
});