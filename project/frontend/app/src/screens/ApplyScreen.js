import { useQuery } from 'react-query';
import { useParams } from 'react-router-dom';
import { applyEvent } from '../services/EventService';
import { useAuth } from '../auth/Auth';

function ApplyScreen() {
  const { me } = useAuth();
  const { id: event_id } = useParams(); 
  const { data: event, isLoading } = useQuery(`eventApply/${event_id}`, () => applyEvent(me, event_id));

  if (!isLoading && !event) {
    return <div> Event not found. </div>;
  }
 
return (
    <span>You succesfully applied!</span>
);
}

export default ApplyScreen;
