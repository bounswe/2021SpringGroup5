import { QueryClient, QueryClientProvider } from 'react-query';
import { configure, render as rtlRender, screen } from '@testing-library/react';
import { ParticipantListingRow } from '../screens/ParticipantsScreen';

const user_1 = {
  user_id: 1,
  user_name: 'ali',
  user_surname: 'ozturk',
  user_username: 'ali123',
  image_url: '',
};

const user_2 = {
  user_id: 2,
  user_name: 'henry',
  user_surname: 'cavill',
  user_username: 'superman',
  image_url:
    'https://m.media-amazon.com/images/M/MV5BODI0MTYzNTIxNl5BMl5BanBnXkFtZTcwNjg2Nzc0NA@@._V1_UY1200_CR190,0,630,1200_AL_.jpg',
};
const event_details_mock = {
  object: {
    post_name: 'Mock Post',
    participant_limit: 7,
    spectator_limit: 30,
    owner: {
      id: 1,
      name: 'Sally',
      surname: 'Sparrow',
      username: 'crazy_girl',
    },
    spectators: [user_1, user_2, user_1, user_2, user_1, user_2, user_1],
    waiting_players: [user_1],
    accepted_players: [user_1, user_2, user_1, user_2, user_1, user_2, user_1],
    rejected_players: [user_1, user_2, user_1, user_2, user_1, user_2, user_1],
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
    is_event_creator: true,
  },
};

function render(children) {
  const queryClient = new QueryClient();
  return rtlRender(<QueryClientProvider client={queryClient}>{children}</QueryClientProvider>);
}

test('should prevent accept when participants are full', async () => {
  configure({ defaultHidden: true });

  render(
    <ParticipantListingRow
      participants={event_details_mock.object.waiting_players}
      title="Waiting"
      actionable={true}
      event={event_details_mock}
    />
  );

  expect(screen.getByTestId('accept_button_0')).toBeInTheDocument();
  const button = screen.getByTestId('accept_button_0');
  expect(button).toBeDisabled();
});
