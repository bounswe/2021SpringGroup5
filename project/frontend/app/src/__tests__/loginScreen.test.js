import LoginScreen from '../screens/LoginScreen';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('login screen input', async () => {
  render(<LoginScreen />);
  expect(screen.getByTestId('username')).toBeInTheDocument();
  const username = screen.getByTestId('username');
  expect(screen.getByTestId('password')).toBeInTheDocument();
  const password = screen.getByTestId('password');

  expect(screen.getByRole('button', { name: /login/i })).toBeInTheDocument();
  const login_button = screen.getByRole('button', { name: /login/i });

  userEvent.type(username, 'username');
  userEvent.type(password, 'password');

  userEvent.click(login_button);
  await waitFor(() => {});
});
