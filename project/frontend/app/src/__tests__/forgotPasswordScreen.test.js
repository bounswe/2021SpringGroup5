import ForgotPasswordScreen from '../screens/ForgotPasswordScreen';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('forgot password screen input', async () => {
  render(<ForgotPasswordScreen />);
  expect(screen.getByTestId('email')).toBeInTheDocument();
  const email = screen.getByTestId('email');
  expect(screen.getByRole('button', { name: /reset password/i })).toBeInTheDocument();
  const reset_password_button = screen.getByRole('button', { name: /reset password/i });

  userEvent.type(email, 'test@test.com');
  userEvent.click(reset_password_button);
  await waitFor(() => {});
});
