import { QueryClient, QueryClientProvider } from 'react-query';
import { configure, render as rtlRender, screen } from '@testing-library/react';
import ApplyScreen from '../screens/ApplyScreen';

const apply_mock = {
    type: "Application",
    object: {
        type: "EventPost",
        Id: 1
    }
};

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('apply', async () => {
  configure({ defaultHidden: true });

  render(<ApplyScreen data={apply_mock.object} event_id={apply_mock.object.Id} />);

});
