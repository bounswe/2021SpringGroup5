import CommentSection from '../components/Common/CommentSection';
import { useQuery } from 'react-query';
import { useParams } from 'react-router-dom';
import { getEvent } from '../services/EventService';
import { useAuth } from '../auth/Auth';

function EventDetailScreen() {
  const { me } = useAuth();
  const { id: event_id } = useParams(); 
  const { data: event, isLoading } = useQuery(`eventDetail/${event_id}`, () => getEvent(me, event_id));

  if (!isLoading && !event) {
    return <div> Event not found. </div>;
  }
 
  return (
    <div className="event-detail gray-bg general-container">
      <div className="container">
        <div className="row align-items-start">
          <div className="col-lg-12 m-15px-tb">
            <article className="event">
              <div className="event-img">
                <img src={event && event.object.pathToEventImage} title="" alt="" />
              </div>
              <div className="event-title">
                <h6>
                  Category: <a href="#">{event && event.object.sport_category}</a>
                </h6>
                <h2>{event && event.object.post_name}</h2>
                <div className="media">
                  <div className="media-body">
                    <label>
                      Creator: {event && event.object.owner.name} {event && event.object.owner.surname}
                    </label>
                    <span></span>
                    <label>Event Time: {event && event.object.date_time}</label>
                    <span></span>
                    <label>Contact Information: {event && event.object.contact_info}</label>
                    <span></span>
                    <label>Skill Requirement: {event && event.object.skill_requirement}</label>
                    <p></p>
                    <label>Participation Limit: {event && event.object.participant_limit}</label> -{' '}
                    <label>Spectator Limit: {event && event.object.spectator_limit}</label>
                  </div>
                </div>
              </div>
              <div className="event-content">
                <h4>Event Description</h4>
                <p>{event && event.object.description}</p>

                <h4>General Rules</h4>
                <p>{event && event.object.rule}</p>

                <h4>Equipment Requirements</h4>
                <p>{event && event.object.equipment_requirement}</p>

                <h4>Location Requirements</h4>
                <p>{event && event.object.location_requirement}</p>
              </div>
              <a href={'/eventParticipants/' + (event && event.object.id)}>Event Participations</a> - 
              <a href={'/eventApply/' + (event && event.object.id)}> Apply Event</a>

            </article>
            {event && <CommentSection comments={event.object.comments} event_id={event.object.id} />}
          </div>
        </div>
      </div>


    </div>
  );
}

export default EventDetailScreen;
