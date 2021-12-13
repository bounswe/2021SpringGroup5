import { Alert, Button, TextField } from '@mui/material';
import './LandingPage.css';
import { login } from '../services/AuthService';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from 'react-query';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';

function LoginScreen() {
  const history = useHistory();

  const [alert, setAlert] = useState(null);
  const { handleSubmit, control } = useForm();

  const mutation = useMutation('login', loginData => login(loginData), {
    onSuccess: () => {
      history.push('/');
    },
    onError: error => {
      setAlert({ type: 'error', message: 'Wrong username or password' });
    },
    onMutate: () => {
      setAlert(null);
    },
  });

  const onLogin = loginData => {
    mutation.mutate(loginData);
  };

  return (
    <div className="landing-page-wrapper">
      <div className="landing-page-content">
        <form onSubmit={handleSubmit(onLogin)} className="landing-page-form">
          <p>Login</p>
          <div className="landing-page-form-inputs">
            <Controller
              name="username"
              control={control}
              render={({ field }) => (
                <TextField
                  autoComplete="off"
                  color="success"
                  variant="standard"
                  label="Username"
                  data-testId="username"
                  required={true}
                  {...field}
                />
              )}
            />
            <Controller
              name="password"
              control={control}
              render={({ field }) => (
                <TextField
                  autoComplete="off"
                  color="success"
                  variant="standard"
                  type="password"
                  label="Password"
                  data-testId="password"
                  required={true}
                  {...field}
                />
              )}
            />
          </div>

          <div className="landing-page-form-submit">
            <div className="landing-page-form-submit-row">
              <Button
                color="success"
                variant="text"
                size="small"
                onClick={() => {
                  history.push('/register');
                }}
              >
                Register
              </Button>

              <Button
                color="success"
                variant="text"
                size="small"
                onClick={() => {
                  history.push('/forgot-password');
                }}
              >
                Forgot Password
              </Button>
            </div>
            <Button color="success" type="submit" variant="contained">
              Login
            </Button>
            {alert && <Alert severity="error">{alert.message}</Alert>}
          </div>
        </form>
        <div className="landing-page-logo">
          <span>L</span>
          <span>U</span>
          <span>D</span>
          <span>O</span>
        </div>
      </div>
    </div>
  );
}

export default LoginScreen;
