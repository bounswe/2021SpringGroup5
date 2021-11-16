import { Alert, Button, TextField } from '@mui/material';
import './LandingPage.css';
import { forgotPassword } from '../services/AuthService';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from 'react-query';
import { useState } from 'react';

function ForgotPasswordScreen() {
  const [alert, setAlert] = useState(null);
  const { handleSubmit, control } = useForm();

  const mutation = useMutation('forgotPassword', forgotPasswordData => forgotPassword(forgotPasswordData), {
    onSuccess: () => {
      setAlert({ type: 'info', message: 'Please check your e-mail' });
    },
    onError: () => {
      setAlert(null);
    },
    onMutate: () => {
      setAlert(null);
    },
  });

  const onForgotPassword = forgotPasswordData => {
    mutation.mutate(forgotPasswordData);
  };

  return (
    <div className="landing-page-wrapper">
      <div className="landing-page-content">
        <form onSubmit={handleSubmit(onForgotPassword)} className="landing-page-form">
          <p>Forgot Password</p>
          <div className="landing-page-form-inputs">
            <Controller
              name="email"
              control={control}
              render={({ field }) => (
                <TextField
                  autoComplete="off"
                  type="email"
                  color="success"
                  variant="standard"
                  label="Email"
                  required={true}
                  {...field}
                />
              )}
            />
          </div>
          <div className="landing-page-form-submit">
            <Button color="success" type="submit" variant="contained">
              Reset Password
            </Button>
            {alert && <Alert severity="info">{alert.message}</Alert>}
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

export default ForgotPasswordScreen;
