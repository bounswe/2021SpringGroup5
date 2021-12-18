import SearchScreen from '../screens/SearchScreen';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
    const queryClient = new QueryClient();
    return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('check for end date earlier than start date', async () => {
    render(<SearchScreen />);
    expect(screen.getByTestId('date')).toBeInTheDocument();
    const startDate = screen.getByTestId('startDate');
    const endDate = screen.getByTestId('endDate');
    expect(screen.getByRole('button', { name: /filter/i })).toBeInTheDocument();
    const filterButton = screen.getByRole('button', { name: /filter/i });

    userEvent.type(startDate, '21/03/2021');
    userEvent.type(endDate, '20/03/2021');
    userEvent.click(filterButton);

    expect(screen.getByTestId('errorMessageForDate')).toBeInTheDocument();
    await waitFor(() => { });
});

test('check for not double data type radius for the map', async () => {
    render(<SearchScreen />);
    expect(screen.getByTestId('map')).toBeInTheDocument();
    const radius = screen.getByTestId('radius');
    expect(screen.getByRole('button', { name: /applyMap/i })).toBeInTheDocument();
    const mapButton = screen.getByRole('button', { name: /applyMap/i });

    userEvent.type(radius, 'RandomThings......');
    userEvent.click(mapButton);

    expect(screen.getByTestId('errorMessageForMap')).toNotBeInTheDocument();
    await waitFor(() => { });
});
