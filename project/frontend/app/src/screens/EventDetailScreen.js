function EventDetailScreen() {

    const state = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary": "Sally is creating an event post",
        "type": "Create",
        "actor": {
            "type": "Person",
            "name": "Umut",
            "surname": "Gün",
            "username":"umutgun17",
            "Id":1
        },
        "object": {
            "type": "Event_Post",
            "owner_id": 1,
            "post_name": "Event Detail Title Will Be Here Here Here Here",
            "sport_category": "FOOTBALL",
            "longitude":12.345,
            "latitude":34.5678,
            "description": "Aenean eleifend ante maecenas pulvinar montes lorem et pede dis dolor pretium donec dictum. Vici consequat justo enim. Venenatis eget adipiscing luctus lorem. Adipiscing veni amet luctus enim sem libero tellus viverra venenatis aliquam. Commodo natoque quam pulvinar elit.",
            "pathToEventImage": "https://media.istockphoto.com/photos/foot-on-a-football-closeup-picture-id1175653469", 
            "date_time": "2021-02-10 10:30",
            "participant_limit": 14,
            "spectator_limit": 150,
            "rule": "Aenean eleifend ante maecenas pulvinar montes lorem et pede dis dolor pretium donec dictum. Vici consequat justo enim. Venenatis eget adipiscing luctus lorem. Adipiscing veni amet luctus enim sem libero tellus viverra venenatis aliquam. Commodo natoque quam pulvinar elit.",
            "equipment_requirement": "Aenean eleifend ante maecenas pulvinar montes lorem et pede dis dolor pretium donec dictum. Vici consequat justo enim. Venenatis eget adipiscing luctus lorem. Adipiscing veni amet luctus enim sem libero tellus viverra venenatis aliquam. Commodo natoque quam pulvinar elit.",           
            "location_requirement": "Aenean eleifend ante maecenas pulvinar montes lorem et pede dis dolor pretium donec dictum. Vici consequat justo enim. Venenatis eget adipiscing luctus lorem. Adipiscing veni amet luctus enim sem libero tellus viverra venenatis aliquam. Commodo natoque quam pulvinar elit.",
            "contact_info": "+90541 555 55 55",
            "skill_requirement": "beginner",
            "repeating_frequency": 1,
            "badges": [ {"id":1,"name":"friendly","description":"You are a friendly player","pathToBadgeImage":""}]
        }
    }
    return (
        <div className="event-detail gray-bg general-container">
        <div className="container">
            <div className="row align-items-start">
                <div className="col-lg-12 m-15px-tb">
                    <article className="event">
                        <div className="event-img">
                            <img src={state.object.pathToEventImage} title="" alt="" />
                        </div>
                        <div className="event-title">
                            <h6>Category: <a href="#">{state.object.sport_category}</a></h6>
                            <h2>{state.object.post_name}</h2>
                            <div className="media">
                                <div className="media-body">
                                    <label>Creator: {state.actor.name} {state.actor.surname}</label>
                                    <span></span>
                                    <label>Event Time: {state.object.date_time}</label>
                                    <span></span>
                                    <label>Contact Information: {state.object.contact_info}</label>
                                    <span></span>
                                    <label>Skill Requirement: {state.object.skill_requirement}</label>
                                    <p></p>
                                    <label>Participation Limit: {state.object.participant_limit}</label> - <label>Spectator Limit: {state.object.spectator_limit}</label>
                                </div>
                            </div>
                        </div>
                        <div className="event-content">
                            <h4>Event Description</h4>
                            <p>{state.object.description}</p>

                            <h4>General Rules</h4>
                            <p>{state.object.rule}</p>

                            <h4>Equipment Requirements</h4>
                            <p>{state.object.equipment_requirement}</p>

                            <h4>Location Requirements</h4>
                            <p>{state.object.location_requirement}</p>

                        </div>

                    </article>
                </div>

            </div>
        </div>
    </div>
    );
}

export default EventDetailScreen;
