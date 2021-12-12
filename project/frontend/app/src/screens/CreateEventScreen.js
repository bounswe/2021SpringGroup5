import './General.css';

function CreateEvent() {


  function onSubmitClick(e) {

    var splitLocation = (document.getElementById("LongitudeLatitude").value).split(",");
    var imageURL = "";

    var data = {
      "@context":"https://www.w3.org/ns/activitystreams",
      "summary":"creating an event post",
      "type":"Create",
      "actor":{
         "type":"Person",
         "name":"Umut",
         "surname":"Gün",
         "username":"umutgun17",
         "Id": 1
      },
      "object":{
         "type":"Event_Post",
         "owner_id": 1,
         "post_name": document.getElementById("eventTitle").value,
         "sport_category": document.getElementById("sportCategory").value,
         "longtitude": parseFloat(splitLocation[0]),
         "latitude": parseFloat(splitLocation[1]),
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
         "badges":[
          {"id":1},
          {"id":2}
        ]        
      }
   }

  console.log(data);


    var forms = document.querySelectorAll('.needs-validation')

    Array.prototype.slice.call(forms)
      .forEach(function (form) {

        if (!form.checkValidity()) {

          console.log("required inputs");

          e.preventDefault()
          e.stopPropagation()
        } else {

          console.log("submited");

          e.preventDefault()
          e.stopPropagation()
        }

        form.classList.add('was-validated')

      })
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

            <div className="col-md-8 form-group has-validation">
              <label htmlFor="sportCategory">Sport Category</label>
              <select className="form-control" id="sportCategory" name="sportCategory" required>
                <option value="">Choose</option>
                <option value="Handball">Handball</option>
                <option value="Football">Football</option>
                <option value="Basketball">Basketball</option>
              </select>
              <div className="invalid-feedback">
                Please select sport category.
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

            <div className="col-md-6 row">
              <div className="col-md-6 form-group has-validation">
                <label htmlFor="LongitudeLatitude">Longitude, Latitude</label>
                <input type="text" className="form-control" id="LongitudeLatitude" name="LongitudeLatitude" placeholder="Click the button" required />
                <div className="invalid-feedback">
                  Please enter longitude and latitude.
                </div>
              </div>
              <div className="col-md-6">
                <label className="col-md-12" htmlFor=""></label>
                <button className="btn">Click for the google map</button>
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
    </div>
  );
}

export default CreateEvent;
