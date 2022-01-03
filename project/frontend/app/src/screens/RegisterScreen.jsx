import { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useMutation, useQuery } from 'react-query';
import { Alert, Button, Checkbox, FormControlLabel, MenuItem, TextField } from '@mui/material';
import './LandingPage.css';
import { register } from '../services/AuthService';
import { getSports } from '../services/SportsService';
import { toTitleCase, validateEmail, validatePassword, validateUsername } from '../helpers/functions';

function RegisterScreen() {
  const [alert, setAlert] = useState(null);
  const [formStep, setFormStep] = useState(0);
  const { handleSubmit, control, getValues } = useForm();
  const [checked, setChecked] = useState(false);

  const { data: sports_and_levels } = useQuery('sports_and_levels', getSports);

  const mutation = useMutation('register', registerData => register(registerData), {
    onSuccess: () => {
      setAlert({ type: 'success', message: 'Please check your email' });
    },
    onError: () => {
      setAlert({ type: 'error', message: 'Some error occurred' });
    },
    onMutate: () => {
      setAlert(null);
    },
  });

  const onRegister = registerData => {
    if (getValues().username === undefined) {
      setAlert({ type: 'error', message: 'Username required' });
    } else if (!validateUsername(getValues().username)) {
      setAlert({
        type: 'error',
        message: 'The username shall be at least 4 characters long and containing only alphanumeric characters.',
      });
    } else if (getValues().email === undefined) {
      setAlert({ type: 'error', message: 'Email required' });
    } else if (!validateEmail(getValues().email)) {
      setAlert({ type: 'error', message: 'Please enter a valid email' });
    } else if (getValues().name === undefined || getValues().surname === undefined) {
      setAlert({ type: 'error', message: 'Name and surname are required' });
    } else if (getValues().password === undefined || getValues().password_confirm === undefined) {
      setAlert({ type: 'error', message: 'Please enter the password twice' });
    } else if (getValues().password !== getValues().password_confirm) {
      setAlert({ type: 'error', message: 'Passwords do not match' });
    } else if (!validatePassword(getValues().password)) {
      setAlert({
        type: 'error',
        message:
          'Password shall be at least 6 characters long, containing at least one number and one letter and containing only alphanumeric characters.',
      });
    } else {
      mutation.mutate(registerData);
    }
  };

  const handleChange = event => {
    setChecked(event.target.checked);
  };

  return (
    <div className="landing-page-wrapper">
      <div className="landing-page-content">
        <form onSubmit={handleSubmit(onRegister)} className="landing-page-form">
          <p>Register</p>
          {formStep === 0 ? (
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
                name="email"
                control={control}
                render={({ field }) => (
                  <TextField
                    autoComplete="off"
                    type="email"
                    color="success"
                    variant="standard"
                    label="Email"
                    data-testId="email"
                    required={true}
                    {...field}
                  />
                )}
              />
              <div className="landing-page-form-inputs-row">
                <Controller
                  name="name"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Name"
                      data-testId="name"
                      required={true}
                      {...field}
                    />
                  )}
                />
                <Controller
                  name="surname"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Surname"
                      data-testId="surname"
                      required={true}
                      {...field}
                    />
                  )}
                />
              </div>

              <div className="landing-page-form-inputs-row">
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
                <Controller
                  name="password_confirm"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      type="password"
                      label="Password Confirm"
                      data-testId="password confirm"
                      required={true}
                      {...field}
                    />
                  )}
                />
              </div>
            </div>
          ) : (
            <div className="landing-page-form-inputs">
              <div className="landing-page-form-inputs-row">
                <Controller
                  name="sport_1"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      sx={{ width: '50%' }}
                      select={true}
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Sport"
                      data-testId="sport 1"
                      required={true}
                      {...field}
                    >
                      {sports_and_levels &&
                        sports_and_levels.sports.map(sport => (
                          <MenuItem key={sport.id} value={sport.sport_name}>
                            {toTitleCase(sport.sport_name)}
                          </MenuItem>
                        ))}
                    </TextField>
                  )}
                />
                <Controller
                  name="level_1"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      sx={{ width: '50%' }}
                      select={true}
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Level"
                      data-testId="level 1"
                      required={true}
                      {...field}
                    >
                      {sports_and_levels &&
                        sports_and_levels.skill_levels.map(skillLevel => (
                          <MenuItem key={skillLevel.id} value={skillLevel.level_name}>
                            {toTitleCase(skillLevel.level_name)}
                          </MenuItem>
                        ))}
                    </TextField>
                  )}
                />
              </div>
              <div className="landing-page-form-inputs-row">
                <Controller
                  name="sport_2"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      sx={{ width: '50%' }}
                      select={true}
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Sport"
                      data-testId="sport 2"
                      required={true}
                      {...field}
                    >
                      {sports_and_levels &&
                        sports_and_levels.sports.map(sport => (
                          <MenuItem key={sport.id} value={sport.sport_name}>
                            {toTitleCase(sport.sport_name)}
                          </MenuItem>
                        ))}
                    </TextField>
                  )}
                />
                <Controller
                  name="level_2"
                  control={control}
                  render={({ field }) => (
                    <TextField
                      sx={{ width: '50%' }}
                      select={true}
                      autoComplete="off"
                      color="success"
                      variant="standard"
                      label="Level"
                      data-testId="level 2"
                      required={true}
                      {...field}
                    >
                      {sports_and_levels &&
                        sports_and_levels.skill_levels.map(skillLevel => (
                          <MenuItem key={skillLevel.id} value={skillLevel.level_name}>
                            {toTitleCase(skillLevel.level_name)}
                          </MenuItem>
                        ))}
                    </TextField>
                  )}
                />
              </div>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={checked}
                    onChange={handleChange}
                    inputProps={{ 'aria-label': 'controlled' }}
                    color="success"
                  />
                }
                label={
                  <div>
                    <span>I have read and agree to the </span>
                    <a href={'#'}>terms and conditions</a>
                  </div>
                }
              />
            </div>
          )}

          <div className="landing-page-form-submit">
            {formStep === 0 ? (
              <Button
                color="success"
                variant="outlined"
                onClick={e => {
                  e.preventDefault();
                  setFormStep(1);
                }}
              >
                Next
              </Button>
            ) : (
              <>
                <Button color="success" type="submit" variant="contained">
                  Register
                </Button>
                <Button color="success" variant="outlined" onClick={() => setFormStep(0)}>
                  Previous Step
                </Button>
                {alert && <Alert severity={alert.type}>{alert.message}</Alert>}
              </>
            )}
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

export default RegisterScreen;
