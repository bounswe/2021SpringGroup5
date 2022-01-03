import HomeScreen from '../screens/HomeScreen.js';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
    const queryClient = new QueryClient();
    return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('check that if there is any post from followed users it is shown correctly or not', async () => {
    render(<HomeScreen />);
    expect(screen.getByTestId("followedPost")).toBeInTheDocument();
    expect(screen.getByTestId('button')).toBeInTheDocument();
    const event = screen.getByTestId('button');

    userEvent.click(event);
    await waitFor(() => { });
});
