import CreateEventScreen from '../screens/CreateEventScreen.js';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
    const queryClient = new QueryClient();
    return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('check for there is a marker in the map after clicking', async () => {
    render(<CreateEventScreen />);
    expect(screen.getByTestId('map')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /applyMap/i })).toBeInTheDocument();
    const mapButton = screen.getByRole('button', { name: /applyMap/i });
    const map = screen.getByTestId('map');

    userEvent.click(map);
    userEvent.click(mapButton);

    expect(screen.getByTestId('marker')).toBeInTheDocument();
    await waitFor(() => { });
});
