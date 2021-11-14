import { httpClient } from '../httpClient';

export function login(loginForm) {
    return httpClient.post('/login', {
        actor: {
            type: 'Person',
            ...loginForm
        },
    });
}