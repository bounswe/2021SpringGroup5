import { httpClient } from '../httpClient';
import Cookies from 'universal-cookie';

export let accessToken, csrfToken;

export function login(loginForm) {
  return httpClient
    .post(
      '/login',
      {
        actor: {
          type: 'Person',
          ...loginForm,
        },
      },
      { headers: { 'Content-Type': 'multipart/form-data' } }
    )
    .then(res => {
      accessToken = res.data.token.access;
      window.localStorage.setItem("token", res.data.token.access);
      httpClient.defaults.headers['Authorization'] = accessToken;
      httpClient.defaults.headers['Content-Type'] = 'application/json; charset=UTF-8';
      const cookies = new Cookies();
      cookies.set('accessToken', accessToken, { path: '/' });
    });
}

export function me() {
  if (window.localStorage.getItem("token")) {
    httpClient.defaults.headers['Authorization'] = window.localStorage.getItem("token");
    return httpClient.get('/me/', { withCredentials: true }).then(res => res.data);
  }
}

export function forgotPassword(forgotPasswordForm) {
  return httpClient.post('/forgot-password', {
    ...forgotPasswordForm,
  });
}

export function register(registerForm) {
  return httpClient.post('/register', {
    actor: {
      type: 'Person',
      username: registerForm.username,
      email: registerForm.email,
      name: registerForm.name,
      surname: registerForm.surname,
      password1: registerForm.password,
      password2: registerForm.password_confirm,
    },
    items: [
      {
        name: registerForm.sport_1,
        level: registerForm.level_1,
      },
      {
        name: registerForm.sport_2,
        level: registerForm.level_2,
      },
    ],
  });
}

export function refresh() {
  return new Promise(resolve => resolve());
  // return httpClient.get('/refresh').then(res => {
  //   accessToken = res.data.refresh;
  //   httpClient.defaults.headers['Authorization'] = `Bearer ${accessToken}`;
  // });
}

export function logout() {
  return httpClient.delete('/logout').then(() => {
    accessToken = undefined;
    httpClient.defaults.headers['Authorization'] = undefined;
  });
}
