import { Alert, Button, TextField } from '@mui/material';
import './LandingPage.css';
import { login } from '../services/AuthService';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from 'react-query';
import { useState } from 'react';
import { useHistory } from 'react-router-dom';

function LoginScreen(props) {
    const setUser = props.setUser;

    const history = useHistory();

    const [alert, setAlert] = useState(null);
    const { handleSubmit, control } = useForm();

    const mutation = useMutation('login', loginData => login(loginData), {
        onSuccess: data => {
            setUser(data);
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
        <div className='landing-page-wrapper'>
            <div className='landing-page-content'>
                <form onSubmit={handleSubmit(onLogin)} className='landing-page-form'>
                    <p>Login</p>
                    <div className='landing-page-form-inputs'>
                        <Controller
                            name='username'
                            control={control}
                            render={({ field }) => (
                                <TextField
                                    autoComplete='off'
                                    color='success'
                                    variant='standard'
                                    label='Username'
                                    required={true}
                                    {...field}
                                />
                            )}
                        />
                        <Controller
                            name='password'
                            control={control}
                            render={({ field }) => (
                                <TextField
                                    autoComplete='off'
                                    color='success'
                                    variant='standard'
                                    type='password'
                                    label='Password'
                                    required={true}
                                    {...field}
                                />
                            )}
                        />
                    </div>
                    <Button color='success' variant='text' size='small'>
                        Forgot Password
                    </Button>
                    <div className="landing-page-form-submit">
                        <Button color='success' type='submit' variant='contained'>
                            Login
                        </Button>
                        {alert && <Alert severity='error'>{alert.message}</Alert>}
                    </div>
                </form>
                <div className='landing-page-logo'>
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