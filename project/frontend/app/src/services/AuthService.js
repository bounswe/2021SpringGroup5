import { httpClient } from '../httpClient';

export let accessToken, refreshToken;

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
      accessToken = res.data.access;
      refreshToken = res.data.refresh;
      console.log(accessToken);
      console.log(refreshToken);
      httpClient.defaults.headers['Authorization'] = `Bearer ${accessToken}`;
    });
}

export function me() {
  return new Promise(resolve => resolve({ username: 'didemaytac', name: 'Didem', surname: 'Aytac', user_id: 1 }));
  // return httpClient.get('/me', { withCredentials: true }).then(res => res.data);
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
