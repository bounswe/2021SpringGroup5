import { QueryClient, QueryClientProvider } from 'react-query';
import { configure, render as rtlRender, screen } from '@testing-library/react';
import CommentSection from '../components/Common/CommentSection';

const event_mock = {
  event_id: 1,
  comments: [
    {
      content: 'This is the first comment',
      created_date: '29/12/2021 12.20',
      image_url: '',
      username: 'didemaytac',
    },
    {
      content: 'This is the second comment',
      created_date: '28/12/2021 10.30',
      image_url: 'https://www.cumhuriyet.com.tr/Archive/2019/3/4/1276859_resource/Captain-Tsubasa-2018.jpg',
      username: 'tsubasa',
    },
  ],
};

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('comment_section', async () => {
  configure({ defaultHidden: true });

  render(<CommentSection comments={event_mock.comments} event_id={event_mock.event_id} />);

  expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  expect(screen.getByTestId('comment_0')).toBeInTheDocument();
  expect(screen.getByTestId('comment_1')).toBeInTheDocument();
  expect(screen.getByTestId('comment-area')).toBeInTheDocument();
});
