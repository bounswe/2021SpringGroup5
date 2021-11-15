import { Alert, Button, MenuItem, TextField } from '@mui/material';
import './LandingPage.css';
import { register } from '../services/AuthService';
import { useForm, Controller } from 'react-hook-form';
import { useMutation, useQuery } from 'react-query';
import { useState } from 'react';
import { getSports } from '../services/SportsService';
import { toTitleCase } from '../helpers/functions';

function RegisterScreen() {
  const [alert, setAlert] = useState(null);
  const [formStep, setFormStep] = useState(0);
  const { handleSubmit, control } = useForm();

  const { data: sports_and_levels } = useQuery('sports_and_levels', getSports);

  const mutation = useMutation('register', registerData => register(registerData), {
    onSuccess: () => {
      setAlert({ type: 'success', message: 'Please check your email' });
    },
    onError: () => {
      setAlert(null);
    },
    onMutate: () => {
      setAlert(null);
    },
  });

  const onRegister = registerData => {
    mutation.mutate(registerData);
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
            </div>
          )}

          <div className="landing-page-form-submit">
            {formStep === 1 ? (
              <>
                <Button color="success" type="submit" variant="contained">
                  Register
                </Button>
                {alert && <Alert severity="success">{alert.message}</Alert>}
              </>
            ) : (
              <Button color="success" variant="contained" onClick={() => setFormStep(1)}>
                Next
              </Button>
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
