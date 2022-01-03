import { httpClient } from '../httpClient';

export function followedUsersEventsRequest(data) {
    return httpClient.get('/home/');
}
