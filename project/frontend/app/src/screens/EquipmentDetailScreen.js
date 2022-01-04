
import { useQuery } from 'react-query';
import { useParams } from 'react-router-dom';
import { getEquipment } from '../services/EventService';
import { useAuth } from '../auth/Auth';

function EquipmentDetailScreen() {
  const { me } = useAuth();
  const { id: eq_id } = useParams(); 
  const { data: eq, isLoading } = useQuery(`equipmentDetail/${eq_id}`, () => getEquipment(me, eq_id));

  if (!isLoading && !eq) {
    return <div> Equipment post not found. </div>;
  }
 
  return (
    <div className="event-detail gray-bg general-container">
      <div className="container">
        <div className="row align-items-start">
          <div className="col-lg-12 m-15px-tb">
            <article className="event">
            <div className="event-img">
                <img src={eq && eq.object.pathToEquipmentPostImage} title="" alt="" />
              </div>
              <div className="event-title">
                <h6>
                  Category: <a href="#">{eq && eq.object.sport_category}</a>
                </h6>
                <h2>{eq && eq.object.post_name}</h2>
                <div className="media">
                  <div className="media-body">
                    <label>
                      Creator: {eq && eq.object.owner.name} {eq && eq.object.owner.surname}
                    </label>
                  </div>
                </div>
              </div>
              <div className="event-content">
                <h4>Post Description</h4>
                <p>{eq && eq.object.description}</p>

                <h4>Equipment Link</h4>
                <p>{eq && eq.object.link}</p>
              </div>

            </article>
           
          </div>
        </div>
      </div>


    </div>
  );
}

export default EquipmentDetailScreen;
