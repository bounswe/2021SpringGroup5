const user_sports_mock = [
  { sport_name: 'basketball', level_name: 'beginner' },
  { sport_name: 'football', level_name: 'beginner' },
  { sport_name: 'volleyball', level_name: 'skilled' },
  { sport_name: 'hockey', level_name: 'skilled' },
  { sport_name: 'snooker', level_name: 'expert' },
  { sport_name: 'diving', level_name: 'average' },
  { sport_name: 'bicycle', level_name: 'beginner' },
];

const user_badges_mock = [
  {
    badge_name: 'enthusiastic',
    badge_description: 'the trait of being overly enthusiastic',
  },
  {
    badge_name: 'friendly',
    badge_description: 'relationship between people who have mutual affection for each other',
  },
  {
    badge_name: 'leader',
    badge_description:
      'someone with the authority to affect the conduct of others; who have the responsibility of leading',
  },
  {
    badge_name: 'gifted',
    badge_description: 'intellectual ability significantly higher than average',
  },
  {
    badge_name: 'loser',
    badge_description: 'one who loses',
  },
  {
    badge_name: 'competitive',
    badge_description: 'trait of being competitive',
  },
];

const user_events_mock = [
  {
    src: 'https://cdnuploads.aa.com.tr/uploads/Contents/2021/08/20/thumbs_b_c_7d185fadd9e4918ce231278823901488.jpg?v=155228',
    title: 'Basketball Game 1',
    type: 'Basketball',
    location: 'Uskudar',
    date: '17 Nov',
    time: '13:00',
  },
  {
    src: 'https://iaftm.tmgrup.com.tr/251c2a/633/358/0/0/707/400?u=https://iftm.tmgrup.com.tr/2021/09/17/basketbol-super-liginde-2021-22-sezonu-heyecani-basliyor-1631887007257.jpeg',
    title: 'Basketball Game 2',
    type: 'Basketball',
    location: 'Kadikoy',
    date: '18 Nov',
    time: '17:00',
  },
  {
    src: 'https://www.istanbulsporenvanteri.com/uploads/resim/1050-1/wfbne3ck.c3d.png',
    title: 'Basketball Game 3',
    type: 'Basketball',
    location: 'Besiktas',
    date: '19 Nov',
    time: '18:00',
  },
  {
    src: 'https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1500000/basketbol-thy-avrupa-ligi-1501700_2.jpg',
    title: 'Basketball Game 4',
    type: 'Basketball',
    location: 'Hisarustu',
    date: '23 Nov',
    time: '18:30',
  },
];

const user_info_mock = {
  name: 'Mr.',
  surname: 'Peanutbutter',
  username: 'peanutz',
  mail: 'peanutbutter@pblivin.com',
  profile_image_url: 'https://pbs.twimg.com/profile_images/600483555416920065/cDUoY9Ar_400x400.jpg',
  events: user_events_mock,
  equipments: user_events_mock,
  sports: user_sports_mock,
  badges: user_badges_mock,
  is_followed: true,
};

export function getUserInfo() {
  return new Promise(resolve => resolve(user_info_mock));
}

export function followUser() {
  return new Promise(resolve => resolve(user_info_mock));
}

export function unfollowUser() {
  return new Promise(resolve => resolve(user_info_mock));
}
