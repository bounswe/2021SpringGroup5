import { httpClient } from '../httpClient';

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
    waiting_players: [user_1, user_2, user_1, user_2, user_1, user_2, user_1],
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
    is_event_creator: false,
  },
};
export function getEvent(event_id) {
  return new Promise(resolve => resolve(event_details_mock));
  /*return httpClient
    .post(`/post/get_event_post_details`, {
      '@context': 'https://www.w3.org/ns/activitystreams',
      summary: '',
      type: 'View',
      actor: {
        type: 'Person',
        name: '',
        surname: '',
        username: '',
        id: 1,
      },
      object: {
        type: 'EventPost',
        post_id: event_id,
      },
    })
    .then(res => res.data);*/
}

export function postComment(post_id, text) {
  return httpClient.post(`post/create_event_comment`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: '',
    type: 'Create',
    object: {
      type: 'Comment',
      content: text,
      post_id: post_id,
    },
  });
}

export function acceptUser(event_id, user_id) {
  return httpClient.post(`/post/accept_application`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: 'Salih accepted an application',
    type: 'Accept',
    applicant: {
      id: user_id,
    },
    object: {
      type: 'EventPost',
      id: event_id,
    },
  });
}

export function rejectUser(event_id, user_id) {
  return httpClient.post(`/post/reject_application/`, {
    '@context': 'https://www.w3.org/ns/activitystreams',
    summary: 'Salih accepted an application',
    type: 'Reject',
    applicant: {
      id: user_id,
    },
    object: {
      type: 'EventPost',
      id: event_id,
    },
  });
}
