import Map from '../components/Common/Map';
import './General.css';
import { Box } from '@mui/material';
import { useState } from 'react';
import Modal from '@mui/material/Modal';
import Button from '@mui/material/Button';

const styleModal = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 600,
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
  borderRadius: 2,
};

function CreateEvent() {
  const [position, setPosition] = useState();

  console.log(position);

  const [openMapModal, setOpenMapModal] = useState(false);
  const handleOpenMapModal = () => {
    setOpenMapModal(true);
  };
  const handleCloseMapModal = () => {
    setOpenMapModal(false);
  };

  function onSubmitClick(e) {
    // var splitLocation = (document.getElementById("LongitudeLatitude").value).split(",");
    var imageURL = "";

    var data = {
      "@context": "https://www.w3.org/ns/activitystreams",
      "summary": "creating an event post",
      "type": "Create",
      "actor": {
        "type": "Person",
        "name": "Umut",
        "surname": "Gün",
        "username": "umutgun17",
        "Id": 1
      },
      "object": {
        "type": "Event_Post",
        "owner_id": 1,
        "post_name": document.getElementById("eventTitle").value,
        "sport_category": document.getElementById("sportCategory").value,
        // "longtitude": parseFloat(splitLocation[0]),
        // "latitude": parseFloat(splitLocation[1]),
        "longtitude": position.lng,
        "latitude": position.lat,
        "description": document.getElementById("eventDescription").value,
        "pathToEventImage": "aaaaaa",
        "date_time": document.getElementById("eventDate").value,
        "participant_limit": parseInt(document.getElementById("participationLimit").value),
        "spectator_limit": parseInt(document.getElementById("spectatorLimit").value),
        "rule": document.getElementById("generalRules").value,
        "equipment_requirement": document.getElementById("equipmentRequirements").value,
        "location_requirement": document.getElementById("locationRequirements").value,
        "contact_info": document.getElementById("contactInfo").value,
        "skill_requirement": document.getElementById("skillRequirement").value,
        "repeating_frequency": parseInt(document.getElementById("repeatingFrequency").value),
        "badges": [
          { "id": 1 },
          { "id": 2 }
        ]
      }
    }

    console.log(data);


    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
      .forEach(function (form) {

        if (!form.checkValidity()) {

          console.log("required inputs");

          alert('You should enter necessary inputs.');

          e.preventDefault()
          e.stopPropagation()
        } else {

          console.log("submited");
          alert('The post published successfully. You will redirect to the detail page of the post.');
          window.location.href = '/eventDetail/5';

          e.preventDefault();
          e.stopPropagation();
        }

        form.classList.add('was-validated')

      })
  };

  function sporCategoryChange() {
    var sporCategory = document.getElementById("sportCategory").value;
    if (sporCategory == 'Other') {
      var element = document.getElementById('spor-category-other');
      element.classList.add('d-block');
    } else {
      var element = document.getElementById('spor-category-other');
      element.classList.remove('d-block');
    }
  };



  return (

    <div className="card create-new-event-container general-container">
      <div className="container"></div>
      <h4 className="card-header">Create New Event</h4>
      <div className="card-body">
        <form className="needs-validation" noValidate>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="eventTitle">Event Title</label>
            <input type="text" className="form-control" id="eventTitle" name="eventTitle" placeholder="Enter event title" required />
            <div className="invalid-feedback">
              Please enter title.
            </div>
          </div>

          <div className="col-md-8 row">
            <div className="col-md-8 form-group has-validation">
              <label htmlFor="sportCategory">Sport Category</label>
              <select className="form-control" id="sportCategory" name="sportCategory" onChange={sporCategoryChange} required>
                <option value="">Choose</option>
                <option value="Handball">Handball</option>
                <option value="Football">Football</option>
                <option value="Basketball">Basketball</option>
                <option value="Other">Other</option>
              </select>
              <div className="invalid-feedback">
                Please select sport category.
              </div>
            </div>

            <div className="col-md-4 form-group has-validation" id="spor-category-other">
              <label htmlFor="sporCategoryOther">Spor Category (Other)</label>
              <input type="text" className="form-control" id="sporCategoryOther" name="sporCategoryOther" placeholder="Enter spor category" />
            </div>

          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="eventTitle">Event Description</label>
            <textarea className="form-control" id="eventDescription" name="eventDescription" placeholder="Enter event description" required></textarea>
            <div className="invalid-feedback">
              Please enter description.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="eventDate">Event Date and Time</label>
            <input type="datetime-local" className="form-control" id="eventDate" name="eventDate" placeholder="Enter event date and time" required />
            <div className="invalid-feedback">
              Please enter event date and time.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="eventImage" className="form-label">Event Image</label>
            <input className="form-control" type="file" id="eventImage" name="eventImage" required />
            <div className="invalid-feedback">
              Please choose event image.
            </div>
          </div>

          <div className="col-md-8 row">
            <div className="col-md-6 form-group has-validation">
              <label htmlFor="LongitudeLatitude">Longitude, Latitude</label>
              <div className="invalid-feedback">
                Please enter longitude and latitude.
              </div>
              <Button onClick={handleOpenMapModal} variant="outlined">Choose from the map</Button>
            </div>
          </div>

          <div className="col-md-8 row">
            <div className="col-md-4 form-group has-validation">
              <label htmlFor="participationLimit">Participation Limit</label>
              <input type="number" className="form-control" id="participationLimit" name="participationLimit" placeholder="Enter participation limit" required />
              <div className="invalid-feedback">
                Please enter participation limit.
              </div>
            </div>
            <div className="col-md-4 form-group has-validation">
              <label htmlFor="spectatorLimit">Spectator Limit</label>
              <input type="number" className="form-control" id="spectatorLimit" name="spectatorLimit" placeholder="Enter spectator limit" required />
              <div className="invalid-feedback">
                Please enter spectator limit.
              </div>
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="generalRule">General Rules</label>
            <textarea className="form-control" id="generalRules" name="generalRules" placeholder="Enter general rules"></textarea>
            <div className="invalid-feedback">
              Please enter general rules.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="equipmentRequirement">Equipment Requirement</label>
            <textarea className="form-control" id="equipmentRequirements" name="equipmentRequirements" placeholder="Enter equipment requirements"></textarea>
            <div className="invalid-feedback">
              Please enter equipment requirements.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="eventTitle">Location Requirements</label>
            <textarea className="form-control" id="locationRequirements" name="locationRequirements" placeholder="Enter location requirements"></textarea>
            <div className="invalid-feedback">
              Please enter location requirements.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="contactInfo">Contact Information</label>
            <input type="text" className="form-control" id="contactInfo" name="contactInfo" placeholder="Enter contact information" required />
            <div className="invalid-feedback">
              Please enter contact information.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="skillRequirement">Skill Requirement</label>
            <select className="form-control" id="skillRequirement" name="skillRequirement" required>
              <option value="">Choose</option>
              <option value="beginner">beginner</option>
              <option value="medium">medium</option>
              <option value="expert">expert</option>
            </select>
            <div className="invalid-feedback">
              Please select skill requirement.
            </div>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="repeatingFrequency">Repeating Frequency (If you want to repeat your event)</label>
            <select className="form-control" id="repeatingFrequency" name="repeatingFrequency" >
              <option value="0">0</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </div>

          <div className="col-md-8 form-group has-validation">
            <label htmlFor="badges">Badges</label>
            <div>
              <div className="form-check form-check-inline">
                <input className="form-check-input" type="checkbox" id="bades" value="friendly" />
                <label className="form-check-label" htmlFor="inlineCheckbox1">friendly</label>
              </div>
              <div className="form-check form-check-inline">
                <input className="form-check-input" type="checkbox" id="bades" value="polite" />
                <label className="form-check-label" htmlFor="inlineCheckbox1">polite</label>
              </div>
            </div>
          </div>
          <button onClick={onSubmitClick.bind(this)} className="btn btn-primary">Submit</button>
        </form>
      </div>

      <Modal
        open={openMapModal}
        onClose={handleCloseMapModal}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={styleModal}>
          <Map height="500px" position={position} setPosition={setPosition} />
          <div className="row justify-content-between mt-3">
            <div className="col-12 d-flex justify-content-center">
              <Button onClick={handleCloseMapModal} variant="contained">
                Choose Location
              </Button>
            </div>
          </div>
        </Box>
      </Modal>
    </div>
  );
}

export default CreateEvent;
