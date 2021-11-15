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
    },
  });
}
