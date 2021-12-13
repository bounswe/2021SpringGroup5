import React, { useState } from 'react';
import { useQuery } from 'react-query';
import { useHistory, useLocation } from 'react-router-dom';
import { Button, Card, CardContent, Typography } from '@mui/material';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import './Profile.css';
import { CustomCard } from './SearchScreen';
import { useAuth } from '../auth/Auth';
import { toTitleCase } from '../helpers/functions';
import { getUserInfo } from '../services/UserService';

const Profile = () => {
  const { me, logout, login, refresh, isAuthenticated, loading } = useAuth();

  const location = useLocation();
  const history = useHistory();
  const searchParams = new URLSearchParams(location.search);

  const username = searchParams.get('username') || (me && me.username);

  const { data: user } = useQuery(`users/${username}`, () => getUserInfo(username));
  return (
    <div className="profile-wrapper">
      {user && (
        <React.Fragment>
          <div className="profile-information">
            <img src={user.profile_image_url} alt="Image" />
            <div>
              <p>Name: {user.name}</p>
              <p>Surname: {user.surname}</p>
              <p>Username: {user.username}</p>
            </div>
            <Button variant="contained" color="success" type="submit">
              Follow
            </Button>
          </div>
          <div>
            <ProfileSports sports={user.sports} />
            <ProfileBadges badges={user.badges} />
          </div>
          <div>
            <ProfileEvents events={user.events} />
          </div>
        </React.Fragment>
      )}
    </div>
  );
};

export default Profile;

const ProfileSports = props => {
  const { sports } = props;

  const [startIndex, setStartIndex] = useState(0);

  const displayedItems = sports.length > 4 ? sports.slice(startIndex, startIndex + 4) : sports;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(sports.length > 4 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 4 === sports.length) {
      setHasNextItems(false);
    }
    setHasPreviousItems(true);
  };

  const onPrevious = () => {
    const prevStartIndex = startIndex - 1;
    setStartIndex(prevStartIndex);
    if (prevStartIndex === 0) {
      setHasPreviousItems(false);
    }
    setHasNextItems(true);
  };

  return (
    <div>
      <div className="profile-slider-header">Sports</div>
      <div className="profile-horizontal-slider">
        <div className="profile-horizontal-arrow-icon">
          {hasPreviousItems && <ArrowBackIosIcon onClick={onPrevious} />}
        </div>
        {displayedItems.map(sport => (
          <Card className="profile-sport-card">
            <CardContent>
              <Typography color="text.secondary">Sport</Typography>
              <Typography component="div">{toTitleCase(sport.sport_name)}</Typography>
              <Typography color="text.secondary">Skill Level</Typography>
              <Typography component="div">{toTitleCase(sport.level_name)}</Typography>
            </CardContent>
          </Card>
        ))}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

const ProfileBadges = props => {
  const { badges } = props;

  const [startIndex, setStartIndex] = useState(0);

  const displayedItems = badges.length > 6 ? badges.slice(startIndex, startIndex + 6) : badges;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(badges.length > 6 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 6 === badges.length) {
      setHasNextItems(false);
    }
    setHasPreviousItems(true);
  };

  const onPrevious = () => {
    const prevStartIndex = startIndex - 1;
    setStartIndex(prevStartIndex);
    if (prevStartIndex === 0) {
      setHasPreviousItems(false);
    }
    setHasNextItems(true);
  };

  return (
    <div>
      <div className="profile-slider-header">Badges</div>
      <div className="profile-horizontal-slider">
        <div className="profile-horizontal-arrow-icon">
          {hasPreviousItems && <ArrowBackIosIcon onClick={onPrevious} />}
        </div>
        {displayedItems.map(badge => (
          <Card className="profile-badge-card">
            <CardContent>
              <Typography component="div">{toTitleCase(badge)}</Typography>
            </CardContent>
          </Card>
        ))}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

const ProfileEvents = props => {
  const { events } = props;

  const [startIndex, setStartIndex] = useState(0);

  const displayedItems = events.length > 3 ? events.slice(startIndex, startIndex + 3) : events;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(events.length > 3 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 3 === events.length) {
      setHasNextItems(false);
    }
    setHasPreviousItems(true);
  };

  const onPrevious = () => {
    const prevStartIndex = startIndex - 1;
    setStartIndex(prevStartIndex);
    if (prevStartIndex === 0) {
      setHasPreviousItems(false);
    }
    setHasNextItems(true);
  };

  return (
    <div>
      <div className="profile-slider-header">Previously Joined Events </div>
      <div className="profile-horizontal-slider">
        <div className="profile-horizontal-arrow-icon">
          {hasPreviousItems && <ArrowBackIosIcon onClick={onPrevious} />}
        </div>
        {displayedItems.map(event => (
          <div className="profile-event-card">
            <CustomCard data={event} />
          </div>
        ))}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};
