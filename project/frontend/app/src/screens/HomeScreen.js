import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { CardActionArea } from '@mui/material';

import { followedUsersEventsRequest } from '../services/HomeService';
import { useHistory } from 'react-router-dom/cjs/react-router-dom.min';
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
            setSports(response.data.posts);
            console.log(response.data.posts);
        } catch (e) {
            console.log(e);
        }
    }

    console.log(sports);

    useEffect(() => {
        handleFollowedUsersEventsRequest()
    }, [])

    return (
        <div className="container_home" data-testid="followedPost">
            <img className="logo_home" src="https://cdn.discordapp.com/attachments/825091092374356030/907634507308490772/1.png" />
            <span className="text_home">This website is creating an amateur sports coordination platform. The main virtue of the platform is that it brings people that are interested same kind of sports together so that they can meet new people, socialize and engage in sports they like. In addition to that, people can create accounts for commercial purposes for example sport shop owners or sport field owners can create an account in the name of their business, create posts and participate in events like every other user can do.</span>
            <h3><b>Favourite Sport Categories</b></h3>
            <div className="banners row justify-content-center" style={{ marginLeft: 80 }}>
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
            <div data-testid="button" className='mt-5'>
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
            {!sports &&
                <p className="text-muted mb-5">There is not any event</p>
            }
        </div>
    );
}

export default HomeScreen;
