import SearchScreen from '../screens/SearchScreen.js';
import { render as rtlRender, screen, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from 'react-query';
import userEvent from '@testing-library/user-event';

function render(children) {
    const queryClient = new QueryClient();
    return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test("event date didn't pass and users are trying to send badges (in this case send badge button should not be seen)", async () => {
    render(<SearchScreen />);

    const eventDate = new Date("Thu Feb 10 2022 07:30:00 GMT+0300 (GMT+03:00)")

    if (eventDate < new Date()) {
        expect(screen.getByTestId('badge')).toBeInTheDocument();
    }

    await waitFor(() => { });
});
