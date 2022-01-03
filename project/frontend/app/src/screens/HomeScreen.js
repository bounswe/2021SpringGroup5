import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { Box, CardActionArea, Divider, SwipeableDrawer } from '@mui/material';

import { followedUsersEventsRequest } from '../services/HomeService';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
import Badge from "../components/Common/Badge";
import { useState, useEffect } from 'react';
import './Home.css';


function CustomCard({ data }) {
    console.log(data);

    const history = useHistory()

    return (
        <Card onClick={() => history.push(`/eventDetail/${data.id}`)} sx={{ maxWidth: 345 }} className="text-start">
            <CardActionArea>
                <CardMedia component="img" height="140" image={data.pathToEventImage} />
                <CardContent>
                    <div className="row mb-2">
                        <div className="col-8 fw-bold fs-6">{data.post_name}</div>
                        <div style={{ fontSize: 14 }} className='col-4 text-end d-flex align-items-center justify-content-end text-muted'>
                            {data.sport_category}
                        </div>
                    </div>
                    <div className="row">
                        <div
                            style={{ fontSize: 14 }}
                            className="col-6 text-start d-flex align-items-center justify-content-start text-muted"
                        >
                            {/* {data.location} */}
                            {data.capacity}
                        </div>
                        <div
                            style={{ fontSize: 12 }}
                            className="col-6 text-end d-flex align-items-center justify-content-end text-muted"
                        >
                            {new Date(data.date_time).toLocaleTimeString()}<br></br>{new Date(data.date_time).toDateString()}
                        </div>
                    </div>
                </CardContent>
            </CardActionArea>
        </Card>
    );
}

function HomeScreen() {
    const [sports, setSports] = useState([])

    const handleFollowedUsersEventsRequest = async () => {
        try {
            const response = await followedUsersEventsRequest();
            setSports(response.data);
            console.log(response.data);
        } catch (e) {
            console.log(e);
        }
    }

    useEffect(() => {
        // handleFollowedUsersEventsRequest()

        setSports([
            {
                "id": 1,
                "post_name": "Haftaya Hali Saha",
                "owner": 3,
                "created_date": "2022-01-01 23:06:37",
                "description": "we need 5 player to hali saha",
                "longitude": 12.345,
                "latitude": 34.5678,
                "date_time": "2022-02-10 07:30:00",
                "participant_limit": 5,
                "spectator_limit": 0,
                "rule": "Be kind!",
                "equipment_requirement": "no equipment required",
                "status": "upcoming",
                "capacity": "open to applications",
                "location_requirement": "",
                "contact_info": "054155555",
                "pathToEventImage": "",
                "current_player": 0,
                "current_spectator": 0,
                "sport_name": "football",
                "skill_requirement": "beginner"
            },
            {
                "id": 2,
                "post_name": "Tennis buddy",
                "owner": 5,
                "created_date": "2022-01-01 23:10:09",
                "description": "benimle tennis oynayacak buddy aranıyor",
                "longitude": 12.345,
                "latitude": 34.5678,
                "date_time": "2022-02-10 07:30:00",
                "participant_limit": 1,
                "spectator_limit": 0,
                "rule": "Be kind!",
                "equipment_requirement": "tennis racket",
                "status": "upcoming",
                "capacity": "open to applications",
                "location_requirement": "",
                "contact_info": "054155555",
                "pathToEventImage": "https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file=EventPost_2.jpg",
                "current_player": 0,
                "current_spectator": 0,
                "sport_name": "tennis",
                "skill_requirement": "beginner"
            },
            {
                "id": 4,
                "post_name": "Tennis buddy",
                "owner": 5,
                "created_date": "2022-01-01 23:12:24",
                "description": "benimle tennis oynayacak buddy aranıyor",
                "longitude": 12.345,
                "latitude": 34.5678,
                "date_time": "2022-02-10 07:30:00",
                "participant_limit": 1,
                "spectator_limit": 0,
                "rule": "Be kind!",
                "equipment_requirement": "tennis racket",
                "status": "upcoming",
                "capacity": "open to applications",
                "location_requirement": "",
                "contact_info": "054155555",
                "pathToEventImage": "https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file=EventPost_4.jpg",
                "current_player": 0,
                "current_spectator": 0,
                "sport_name": "tennis",
                "skill_requirement": "beginner"
            },
            {
                "id": 3,
                "post_name": "Tennis buddy",
                "owner": 5,
                "created_date": "2022-01-01 23:10:09",
                "description": "benimle tennis oynayacak buddy aranıyor",
                "longitude": 12.345,
                "latitude": 34.5678,
                "date_time": "2022-02-17 07:30:00",
                "participant_limit": 1,
                "spectator_limit": 0,
                "rule": "Be kind!",
                "equipment_requirement": "tennis racket",
                "status": "upcoming",
                "capacity": "open to applications",
                "location_requirement": "",
                "contact_info": "054155555",
                "pathToEventImage": "https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file=EventPost_3.jpg",
                "current_player": 0,
                "current_spectator": 0,
                "sport_name": "tennis",
                "skill_requirement": "beginner"
            },
            {
                "id": 5,
                "post_name": "Tennis buddy",
                "owner": 5,
                "created_date": "2022-01-01 23:12:24",
                "description": "benimle tennis oynayacak buddy aranıyor",
                "longitude": 12.345,
                "latitude": 34.5678,
                "date_time": "2022-02-17 07:30:00",
                "participant_limit": 1,
                "spectator_limit": 0,
                "rule": "Be kind!",
                "equipment_requirement": "tennis racket",
                "status": "upcoming",
                "capacity": "open to applications",
                "location_requirement": "",
                "contact_info": "054155555",
                "pathToEventImage": "https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file=EventPost_5.jpg",
                "current_player": 0,
                "current_spectator": 0,
                "sport_name": "tennis",
                "skill_requirement": "beginner"
            }
        ])
    }, [])

    return (
        <div className="container_home">
            <img className="logo_home" src="https://cdn.discordapp.com/attachments/825091092374356030/907634507308490772/1.png" />
            <span className="text_home">Our project is creating an amateur sports coordination platform. The main virtue osf the platform i that it brings people that are interested same kind of sports together so that they can meet new people, socialize and engage in sports they like. In addition to that, people can create accounts for commercial purposes for example sport shop owners or sport field owners can create an account in the name of their business, create posts and participate events like every other user can do.</span>
            <h3><b>Favourite Sport Categories</b></h3>
            <div className="banners row justify-content-center">
                <div className='col-10'>
                    <a href="/search" className="banner">
                        <img src="https://www.recablog.com/wp-content/uploads/2021/01/soccer-780x470.jpg" />
                        <span>Soccer</span>
                    </a>
                    <a href="/search" className="banner">
                        <img src="https://sawahpress.com/en/wp-content/uploads/2021/11/thumbs_b_c_fec562758581b280dd2514fd42698034-780x470.jpg" />
                        <span>Basketball</span>
                    </a>
                    <a href="/search" className="banner">
                        <img src="https://gulfgoal.com/en/wp-content/uploads/2021/12/urn-newsml-dpa-com-20090101-211118-99-48608_large_4_3-780x470.jpg" />
                        <span>Tennis</span>
                    </a>
                </div>
            </div>
            <div className='mt-5'>
                <h3><b>Upcoming Events of Followed Users</b></h3>
            </div>
            {sports && (
                <div className="row justify-content-center align-items-center mt-5">
                    <div className="row col-9">
                        {sports.map(sport => (
                            <div className="col-12 col-md-6 col-lg-4 mb-4">
                                <CustomCard data={sport} />
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}

export default HomeScreen;
