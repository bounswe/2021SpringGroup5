import React, { useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import { useMutation, useQuery, useQueryClient } from 'react-query';
import { Avatar, Card, CardContent, Typography } from '@mui/material';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import IconButton from '@mui/material/IconButton';
import { Check, Close } from '@mui/icons-material';
import './ParticipanstScreen.css';
import { acceptUser, getEvent, rejectUser } from '../services/EventService';
import { useAuth } from '../auth/Auth';
import Badge from '../components/Common/Badge';

export const ParticipantListingRow = props => {
  const { me } = useAuth();
  const history = useHistory();

  const { participants, title, actionable, event } = props;

  const [startIndex, setStartIndex] = useState(0);

  const displayedItems = participants.length > 4 ? participants.slice(startIndex, startIndex + 4) : participants;

  const [hasPreviousItems, setHasPreviousItems] = useState(false);
  const [hasNextItems, setHasNextItems] = useState(participants.length > 4 + startIndex);

  const onNext = () => {
    const newStartIndex = startIndex + 1;
    setStartIndex(newStartIndex);
    setHasPreviousItems(true);
    if (newStartIndex + 4 === participants.length) {
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

  const queryClient = useQueryClient();

  const acceptMutation = useMutation('accept', user_id => acceptUser(me, event.object.id, user_id), {
    enabled: !!me,
    onSuccess: () => {
      queryClient.invalidateQueries(`events/${event.object.id}`).then();
    },
  });

  const rejectMutation = useMutation('reject', user_id => rejectUser(me, event.object.id, user_id), {
    enabled: !!me,
    onSuccess: () => {
      queryClient.invalidateQueries(`events/${event.object.id}`).then();
    },
  });

  const onAccept = (user_id, e) => {
    e.stopPropagation();
    acceptMutation.mutate(user_id);
  };

  const onReject = (user_id, e) => {
    e.stopPropagation();
    rejectMutation.mutate(user_id);
  };

  return (
    <div>
      <div className="participant-listing-header">
        {title} ({participants.length})
      </div>
      <div className="participant-listing-slider">
        <div className="participant-listing-arrow-icon">
          {hasPreviousItems && <ArrowBackIosIcon onClick={onPrevious} />}
        </div>
        {displayedItems.map((participant, index) => (
          <Card key={index} className="user-card">
            <CardContent
              className="user-card-content"
              onClick={() => {
                history.push(`/profile?user_id=${participant.user__Id}`);
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <Avatar alt={participant.user__username} src={participant.image_url} />
                <div style={{ marginLeft: '10px' }}>
                  <Typography color="text.secondary">{participant.user__username}</Typography>
                  <Typography color="text.primary">
                    {participant.user__name} {participant.user__surname}
                  </Typography>
                </div>
              </div>
              {actionable && (
                <div className="action-buttons">
                  <IconButton
                    data-testid={'accept_button_'.concat(index)}
                    onClick={e => onAccept(participant.user__Id, e)}
                    size="small"
                    disabled={event.object.accepted_players.length >= event.object.participant_limit}
                  >
                    <Check fontSize="inherit" />
                  </IconButton>
                  <IconButton onClick={e => onReject(participant.user__Id, e)} size="small">
                    <Close fontSize="inherit" />
                  </IconButton>
                </div>
              )}
            </CardContent>
          </Card>
        ))}
        <div className="participant-listing-arrow-icon">{hasNextItems && <ArrowForwardIosIcon onClick={onNext} />}</div>
      </div>
    </div>
  );
};

const ParticipantListingPage = props => {
  const history = useHistory();
  const { participants } = props;

  return (
    <div>
      <div className="participant-listing-header">Participants</div>
      <div className="participant-listing-grid">
        {participants.map(participant => (
          <Card
            className="user-card"
            style={{ width: '100%' }}
          >
            <CardContent
              onClick={() => {
                history.push(`/profile?user_id=${participant.user__Id}`);
              }}
              className="user-card-content"
            >
              <div style={{ display: 'flex', alignItems: 'center' }}>
                <Avatar alt={participant.user__username} src={participant.image_url} />
                <div style={{ marginLeft: '10px' }}>
                  <Typography color="text.secondary">{participant.user__username}</Typography>
                  <Typography color="text.primary">
                    {participant.user__name} {participant.user__surname}
                  </Typography>
                </div>
              </div>
            </CardContent>
            <Badge eventDate={props.eventDate} userId={participant.user__Id} />
          </Card>
        ))}
      </div>
    </div>
  );
};

const ParticipantsScreen = () => {
  const { me } = useAuth();
  const { id: event_id } = useParams();
  const { data: event, isLoading } = useQuery(`events/${event_id}`, () => getEvent(me, event_id), { enabled: !!me });

  if (!isLoading && !event) {
    return <div> Event not found. </div>;
  }

  return (
    <div className="participants-wrapper">
      {event && (
        <div>
          <div className="event-information">
            <Typography color="text.primary">Participants for {event.object.post_name}</Typography>
            <Typography color="text.secondary">
              {event.object.accepted_players.length}/{event.object.participant_limit} Participants
            </Typography>
            <Typography color="text.secondary">
              {event.object.spectators.length}/{event.object.spectator_limit} Spectators
            </Typography>
          </div>

          {!event.object.is_event_creator && <ParticipantsLimited eventDate={new Date(event.object.date_time)} accepted_players={event.object.accepted_players} />}

          {event.object.is_event_creator && (
            <ParticipantsAdmin
              accepted_players={event.object.accepted_players}
              rejected_players={event.object.rejected_players}
              waiting_players={event.object.waiting_players}
              spectators={event.object.spectators}
              event={event}
            />
          )}
        </div>
      )}
    </div>
  );
};

export default ParticipantsScreen;

const ParticipantsLimited = props => {
  const { accepted_players } = props;

  return (
    <div>
      <ParticipantListingPage eventDate={props.eventDate} participants={accepted_players} />
    </div>
  );
};

const ParticipantsAdmin = props => {
  const { accepted_players, rejected_players, waiting_players, spectators, event } = props;

  return (
    <div>
      <ParticipantListingRow
        participants={waiting_players}
        title="Waiting Participants"
        actionable={true}
        event={event}
      />
      <ParticipantListingRow
        participants={accepted_players}
        title="Accepted Participants"
        actionable={false}
        event={event}
      />
      <ParticipantListingRow
        participants={rejected_players}
        title="Rejected Participants"
        actionable={false}
        event={event}
      />
      <ParticipantListingRow participants={spectators} title="Spectators" actionable={false} event={event} />
    </div>
  );
};
