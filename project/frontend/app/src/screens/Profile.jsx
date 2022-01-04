import React, { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from 'react-query';
import { useHistory, useLocation } from 'react-router-dom';
import { Avatar, Button, Card, CardContent, Typography } from '@mui/material';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import './Profile.css';
import { useAuth } from '../auth/Auth';
import { toTitleCase, trimDescription } from '../helpers/functions';
import { followUser, getUserInfo, unfollowUser } from '../services/UserService';
import CardMedia from '@mui/material/CardMedia';
import CardActionArea from '@mui/material/CardActionArea';

function CustomEventCard({ data }) {
  const history = useHistory();
  return (
    <Card sx={{ width: 300 }} className="text-start">
      <CardActionArea>
        <CardMedia
          sx={{
            objectFit: 'cover',
          }}
          component="img"
          height="140px"
          image={
            data.pathToEventImage ||
            'https://cdn.discordapp.com/attachments/825091092374356030/907634507308490772/1.png'
          }
        />
        <CardContent
          onClick={() => {
            history.push(`/eventDetail/${data.pk}`);
          }}
        >
          <div className="row mb-2">
            <div className="col-8 fw-bold fs-6">{data.post_name}</div>
            <div
              style={{ fontSize: 14 }}
              className="col-4 text-end d-flex align-items-center justify-content-end text-muted"
            >
              {data.type}
            </div>
          </div>
          <div className="row">
            <div style={{ fontSize: 12 }}>
              {new Date(data.date_time).toLocaleTimeString()}
              <br />
              {new Date(data.date_time).toDateString()}
            </div>
          </div>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}

function CustomEquipmentCard({ data }) {
  const history = useHistory();
  return (
    <Card sx={{ width: 300 }} className="text-start">
      <CardActionArea>
        <CardMedia
          sx={{
            objectFit: 'cover',
          }}
          component="img"
          height="140px"
          image={
            data.pathToEquipmentPostImage ||
            'https://cdn.discordapp.com/attachments/825091092374356030/907634507308490772/1.png'
          }
        />
        <CardContent
          onClick={() => {
            history.push(`/equipmentDetail/${data.id}`);
          }}
        >
          <div className="row mb-2">
            <div className="col-8 fw-bold fs-6">{data.post_name}</div>
            <div
              style={{ fontSize: 14 }}
              className="col-4 text-end d-flex align-items-center justify-content-end text-muted"
            >
              {data.type}
            </div>
          </div>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
const Profile = () => {
  const { me } = useAuth();

  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);

  const user_id = searchParams.get('user_id') || (me && me.Id);
  const is_me = !searchParams.get('user_id') || searchParams.get('user_id') === (me && me.Id.toString());
  const { data: user } = useQuery(`users/${user_id}`, () => getUserInfo(user_id));

  return (
    <div className="profile-wrapper">
      {user && (
        <React.Fragment>
          <ProfileInformation user={user.user} is_me={is_me} user_id={user_id} following={user.following} />
          <div>
            <ProfileEvents events={user.events} title="Previously Created Event Posts" />
            <ProfileEvents events={user.equipments} title="Previously Created Equipment Posts" />
          </div>

          <div className="profile-sports-and-badges">
            <ProfileSports sports={user.sports} />
            <ProfileBadges badges={user.badges} />
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

  const displayedItems = sports.length > 2 ? sports.slice(startIndex, startIndex + 2) : sports;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(sports.length > 2 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 2 === sports.length) {
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
              <Typography component="div">{toTitleCase(sport.sport_name__sport_name)}</Typography>
              <Typography color="text.secondary">Skill Level</Typography>
              <Typography component="div">{toTitleCase(sport.skill_level__level_name)}</Typography>
            </CardContent>
          </Card>
        ))}
        {displayedItems.length === 0 && (
          <Card className="profile-sport-card">
            <CardContent>
              <Typography color="text.secondary">No Posts Yet</Typography>
            </CardContent>
          </Card>
        )}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

const ProfileBadges = props => {
  const { badges } = props;

  const [startIndex, setStartIndex] = useState(0);

  const displayedItems = badges.length > 3 ? badges.slice(startIndex, startIndex + 3) : badges;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(badges.length > 3 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 3 === badges.length) {
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
          <Card className="profile-sport-card">
            <CardContent>
              <Typography color="text.secondary">{toTitleCase(badge.badge__name)}</Typography>
              <Typography component="div">{trimDescription(badge.badge__description)}</Typography>
            </CardContent>
          </Card>
        ))}
        {displayedItems.length === 0 && (
          <Card className="profile-sport-card">
            <CardContent>
              <Typography color="text.secondary">No Posts Yet</Typography>
            </CardContent>
          </Card>
        )}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

const ProfileEvents = props => {
  const { events, title } = props;

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
      <div className="profile-slider-header">{title} </div>
      <div className="profile-horizontal-slider">
        <div className="profile-horizontal-arrow-icon">
          {hasPreviousItems && <ArrowBackIosIcon onClick={onPrevious} />}
        </div>
        {title === 'Previously Created Event Posts' &&
          displayedItems.map(event => (
            <div className="profile-event-card">
              <CustomEventCard data={event} />
            </div>
          ))}
        {title === 'Previously Created Equipment Posts' &&
          displayedItems.map(event => (
            <div className="profile-event-card">
              <CustomEquipmentCard data={event} />
            </div>
          ))}
        {displayedItems.length === 0 && (
          <Card className="profile-event-card">
            <CardContent>
              <Typography color="text.secondary">No Posts Yet</Typography>
            </CardContent>
          </Card>
        )}
        <div className="profile-horizontal-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

export const ProfileInformation = props => {
  const { user, is_me, user_id, following } = props;

  const queryClient = useQueryClient();

  const followMutation = useMutation('follow', user_id => followUser(user_id), {
    enabled: !!user_id,
    onSuccess: async () => {
      await queryClient.invalidateQueries(`users/${user_id}`);
    },
  });

  const unfollowMutation = useMutation('unfollow', user_id => unfollowUser(user_id), {
    enabled: !!user_id,
    onSuccess: async () => {
      await queryClient.invalidateQueries(`users/${user_id}`);
    },
  });

  const onFollow = user_id => {
    followMutation.mutate(user_id);
  };

  const onUnfollow = user_id => {
    unfollowMutation.mutate(user_id);
  };

  return (
    <div className="profile-information">
      <Avatar alt={user.username} src={user.image_url} />
      <div>
        <p>Name: {user.name}</p>
        <p>Surname: {user.surname}</p>
        <p>Username: {user.username}</p>
      </div>
      {!is_me && !following && (
        <Button variant="contained" color="success" type="submit" onClick={() => onFollow(user_id)}>
          Follow
        </Button>
      )}
      {!is_me && following && (
        <Button variant="contained" color="success" type="submit" onClick={() => onUnfollow(user_id)}>
          Unfollow
        </Button>
      )}
    </div>
  );
};
