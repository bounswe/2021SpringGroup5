import { httpClient } from '../httpClient';

export function getUserInfo(user_id) {
  return httpClient.get(`/profile/${user_id}`, { withCredentials: true }).then(res => res.data);
}

export function followUser(user_id) {
  return httpClient.post(`/follow/${user_id}`, { withCredentials: true }).then(res => res.data);
}

export function unfollowUser(user_id) {
  return httpClient.post(`/unfollow/${user_id}`, { withCredentials: true }).then(res => res.data);
}
