import CommentSection from '../components/Common/CommentSection';
import { useQuery } from 'react-query';
import { useParams } from 'react-router-dom';
import { getEvent } from '../services/EventService';

function EventDetailScreen() {
  const { id: event_id } = useParams();
  const { data: event, isLoading } = useQuery(`events/${event_id}`, () => getEvent(event_id));

  if (!isLoading && !event) {
    return <div> Event not found. </div>;
  }
  const state = {
    image: '',
    json: {
      '@context': 'https://www.w3.org/ns/activitystreams',
      summary: 'reading an event post deatil',
      type: 'Create',
      actor: {
        type: 'Person',
        name: 'Umut',
        surname: 'Gün',
        username: 'umutgun17',
        Id: 1,
      },
      object: {
        type: 'Event_Post',
        owner_id: 1,
        post_name: 'Professional Tennis Match',
        sport_category: 'Tennis',
        longitude: 41.06314391161562,
        latitude: 28.913763761603146,
        description: 'I want a partner to play with me tennis as a professional.',
        pathToEventImage:
          'https://media.istockphoto.com/photos/tennis-players-playing-a-match-on-the-court-picture-id817164728',
        date_time: '21.12.2021 13:00',
        participant_limit: 2,
        spectator_limit: 10,
        rule: 'The general rules are the same with general tennis match.',
        equipment_requirement: 'Tennis racket and minimum 3 tennis balls',
        location_requirement: 'Tennis shoes is requirement to enter the court.',
        contact_info: '+90 543 528 56 00',
        skill_requirement: 'expert',
        repeating_frequency: 0,
        badges: [
          { id: 1, name: 'friendly' },
          { id: 2, name: 'polite' },
        ],
      },
    },
  };
  return (
    <div className="event-detail gray-bg general-container">
      <div className="container">
        <div className="row align-items-start">
          <div className="col-lg-12 m-15px-tb">
            <article className="event">
              <div className="event-img">
                <img src={state.json.object.pathToEventImage} title="" alt="" />
              </div>
              <div className="event-title">
                <h6>
                  Category: <a href="#">{state.json.object.sport_category}</a>
                </h6>
                <h2>{state.json.object.post_name}</h2>
                <div className="media">
                  <div className="media-body">
                    <label>
                      Creator: {state.json.actor.name} {state.json.actor.surname}
                    </label>
                    <span></span>
                    <label>Event Time: {state.json.object.date_time}</label>
                    <span></span>
                    <label>Contact Information: {state.json.object.contact_info}</label>
                    <span></span>
                    <label>Skill Requirement: {state.json.object.skill_requirement}</label>
                    <p></p>
                    <label>Participation Limit: {state.json.object.participant_limit}</label> -{' '}
                    <label>Spectator Limit: {state.json.object.spectator_limit}</label>
                  </div>
                </div>
              </div>
              <div className="event-content">
                <h4>Event Description</h4>
                <p>{state.json.object.description}</p>

                <h4>General Rules</h4>
                <p>{state.json.object.rule}</p>

                <h4>Equipment Requirements</h4>
                <p>{state.json.object.equipment_requirement}</p>

                <h4>Location Requirements</h4>
                <p>{state.json.object.location_requirement}</p>
              </div>
            </article>
            {event && <CommentSection comments={event.object.comments} event_id={event_id} />}
          </div>
        </div>
      </div>
    </div>
  );
}

export default EventDetailScreen;
