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

function CreateEquipment() {
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

    //var splitLocation = (document.getElementById("LongitudeLatitude").value).split(",");

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
         "post_name": document.getElementById("postName").value,
         "sport_category": document.getElementById("sportCategory").value,
         "description": document.getElementById("postDescription").value,
         "link": document.getElementById("equipmentLink").value     
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
          alert('The post published successfully. You will redirect to the equipment page.');
          window.location.href = '/equipmentDetail/1';

          e.preventDefault();
          e.stopPropagation();
        }

        form.classList.add('was-validated')

      })
  };

  function sporCategoryChange() {
    var sporCategory = document.getElementById("sportCategory").value;
    if(sporCategory == 'Other') {
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
        <h4 className="card-header">Create New Equipment Post</h4>
        <div className="card-body">
          <form className="needs-validation" noValidate>

            <div className="col-md-8 form-group has-validation">
              <label htmlFor="eventTitle">Post Name</label>
              <input type="text" className="form-control" id="postName" name="postName" placeholder="Enter post name" required />
              <div className="invalid-feedback">
                Please enter name.
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
              <label htmlFor="postTitle">Post Description</label>
              <textarea className="form-control" id="postDescription" name="postDescription" placeholder="Enter post description" required></textarea>
              <div className="invalid-feedback">
                Please enter description.
              </div>
            </div>

            <div className="col-md-8 row">
              <div className="col-md-4 form-group has-validation">
                <label htmlFor="equipmentLink">Equipment Link</label>
                <input type="text" className="form-control" id="equipmentLink" name="equipmentLink" placeholder="Enter link" required />
                <div className="invalid-feedback">
                  Please enter link.
                </div>
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

export default CreateEquipment;
