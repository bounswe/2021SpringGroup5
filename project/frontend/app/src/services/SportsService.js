import { httpClient } from '../httpClient';

const sports_and_levels_mock = {
  sports: [
    { id: 1, sport_name: 'football' },
    { id: 2, sport_name: 'basketball' },
    { id: 3, sport_name: 'volleyball' },
    { id: 4, sport_name: 'cycling' },
  ],
  skill_levels: [
    { id: 1, level_name: 'beginner' },
    { id: 2, level_name: 'average' },
    { id: 3, level_name: 'skilled' },
    { id: 4, level_name: 'specialist' },
    { id: 5, level_name: 'expert' },
  ],
};

export function getSports() {
  // return new Promise(resolve => resolve(sports_and_levels_mock));
  return httpClient.get('/register').then(res => res.data);
}
