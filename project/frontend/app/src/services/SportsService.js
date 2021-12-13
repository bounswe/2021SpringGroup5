import { httpClient } from '../httpClient';

export function getSports() {
  return httpClient.get('/register').then(res => res.data);
}
