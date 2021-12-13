import RegisterScreen from '../screens/RegisterScreen';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

const validFormValues = {
  username: 'testusername',
  name: 'testname',
  surname: 'testsurname',
  email: 'test@email.com',
  password: 'password123',
  password_confirm: 'password123',
  sport_1: 'test_sport_1',
  level_1: 'test_level_1',
  sport_2: 'test_sport_2',
  level_2: 'test_level_2',
};

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('register screen inputs', async () => {
  render(<RegisterScreen />);
  expect(screen.getByTestId('username')).toBeInTheDocument();
  expect(screen.getByTestId('email')).toBeInTheDocument();
  expect(screen.getByTestId('name')).toBeInTheDocument();
  expect(screen.getByTestId('surname')).toBeInTheDocument();
  expect(screen.getByTestId('password')).toBeInTheDocument();
  expect(screen.getByTestId('password confirm')).toBeInTheDocument();

  expect(screen.getByRole('button', { name: /next/i })).toBeInTheDocument();
  const next_button = screen.getByRole('button', { name: /next/i });
  userEvent.click(next_button);
  await waitFor(() => {});

  expect(screen.getByTestId('sport 1')).toBeInTheDocument();
  expect(screen.getByTestId('level 1')).toBeInTheDocument();
  expect(screen.getByTestId('sport 2')).toBeInTheDocument();
  expect(screen.getByTestId('level 2')).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /register/i })).toBeInTheDocument();
});
