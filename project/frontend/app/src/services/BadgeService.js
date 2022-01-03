import { httpClient } from '../httpClient';

export function getAllBadgesRequest(data) {
    return httpClient.get('/post/get_all_badges/');
}


export function sendBadgeRequest(data) {
    console.log(data);
    return httpClient.post('/post/send_badge/', {
        to_user: {
            Id: data.userId
        },
        badge: {
            name: data.badgeName
        }
    });
}
