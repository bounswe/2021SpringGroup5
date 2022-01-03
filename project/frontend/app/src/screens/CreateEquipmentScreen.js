import './General.css';

function CreateEquipment() {

  function onSubmitClick(e) {

    var splitLocation = (document.getElementById("LongitudeLatitude").value).split(",");

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
         "longtitude": parseFloat(splitLocation[0]),
         "latitude": parseFloat(splitLocation[1]),
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
                <input type="text" className="form-control" id="LongitudeLatitude" name="LongitudeLatitude" placeholder="Enter longtitude and latitude" required />
                <div className="invalid-feedback">
                  Please enter longitude and latitude.
                </div>
              </div>

            </div>

            <button onClick={onSubmitClick.bind(this)} className="btn btn-primary">Submit</button>
          </form>
        </div>
    </div>
  );
}

export default CreateEquipment;
