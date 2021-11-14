import { httpClient } from '../httpClient';

export function login(loginForm) {
  return httpClient.post('/login', {
    actor: {
      type: 'Person',
      ...loginForm,
    },
  });
}

export function forgotPassword(forgotPasswordForm) {
  return httpClient.post('/forgot-password', {
    ...forgotPasswordForm,
  });
}
