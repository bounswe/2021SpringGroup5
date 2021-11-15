import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { CardActionArea } from '@mui/material';
import { useState, forwardRef } from "react";
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';

function CustomCard({ data }) {
    return (
        <Card sx={{ maxWidth: 345 }} className="text-start">
            <CardActionArea>
                <CardMedia
                    component="img"
                    height="140"
                    image={data.src}
                />
                <CardContent>
                    <div className='row mb-2'>
                        <div className='col-8 fw-bold fs-6'>
                            {data.title}
                        </div>
                        <div style={{ fontSize: 14 }} className='col-4 text-end d-flex align-items-center justify-content-end text-muted'>
                            {data.type}
                        </div>
                    </div>
                    <div className='row'>
                        <div style={{ fontSize: 14 }} className='col-6 text-end d-flex align-items-center justify-content-start text-muted'>
                            {data.location}
                        </div>
                        <div style={{ fontSize: 12 }} className='col-6 text-end d-flex align-items-center justify-content-end text-muted'>
                            {data.date} / {data.time}
                        </div>
                    </div>
                </CardContent>
            </CardActionArea>
        </Card>
    );
}

const Alert = forwardRef(function Alert(props, ref) {
    return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

function SearchScreen(props) {
    const [query, setQuery] = useState("")
    const [show, setShow] = useState(false)


    const handleChange = (e) => {
        setQuery(e.target.value)
    }

    const handleRequest = () => {
        if (query === "basketball") {
            setShow(true)
        } else {
            setShow(false)
        }
    }

    const [openNotification, setOpenNotification] = useState(false)

    const handleOpenNotification = () => {
        setOpenNotification(true)
    }

    const handleCloseNotification = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpenNotification(false);
    };

    const sports = [
        {
            src: "https://cdnuploads.aa.com.tr/uploads/Contents/2021/08/20/thumbs_b_c_7d185fadd9e4918ce231278823901488.jpg?v=155228",
            title: "Basketball Game 1",
            type: "Basketball",
            location: "Uskudar",
            date: "17 Nov",
            time: "13:00"
        },
        {
            src: "https://iaftm.tmgrup.com.tr/251c2a/633/358/0/0/707/400?u=https://iftm.tmgrup.com.tr/2021/09/17/basketbol-super-liginde-2021-22-sezonu-heyecani-basliyor-1631887007257.jpeg",
            title: "Basketball Game 2",
            type: "Basketball",
            location: "Kadikoy",
            date: "18 Nov",
            time: "17:00"
        },
        {
            src: "https://www.istanbulsporenvanteri.com/uploads/resim/1050-1/wfbne3ck.c3d.png",
            title: "Basketball Game 3",
            type: "Basketball",
            location: "Besiktas",
            date: "19 Nov",
            time: "18:00"
        },
        {
            src: "https://trthaberstatic.cdn.wp.trt.com.tr/resimler/1500000/basketbol-thy-avrupa-ligi-1501700_2.jpg",
            title: "Basketball Game 4",
            type: "Basketball",
            location: "Hisarustu",
            date: "23 Nov",
            time: "18:30"
        }
    ]

    return (
        <div className="container">
            <div className="row justify-content-center align-items-center mt-5">
                <div className="col-9 col-md-6">
                    <Paper
                        sx={{ p: '2px 4px', display: 'flex', alignItems: 'center' }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            placeholder="Search"
                            inputProps={{ 'aria-label': 'search' }}
                            value={query}
                            onChange={handleChange}
                        />
                        <IconButton onClick={handleRequest} sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Paper>
                </div>
            </div>
            {show &&
                <div className="row justify-content-center align-items-center mt-5">
                    <div className="row col-9">
                        {sports.map((sport) =>
                            <div onClick={handleOpenNotification} className='col-12 col-md-6 col-lg-4 mb-4'>
                                <CustomCard data={sport} />
                            </div>
                        )}
                    </div>
                </div>
            }
            <Snackbar anchorOrigin={{ vertical: 'top', horizontal: 'center' }} open={openNotification} autoHideDuration={2000} onClose={handleCloseNotification}>
                <Alert onClose={handleCloseNotification} severity="success" sx={{ width: '100%' }}>
                    Successfully applied for the event!
                </Alert>
            </Snackbar>
        </div>

    );
}

export default SearchScreen;
