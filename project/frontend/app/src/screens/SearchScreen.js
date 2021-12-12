

import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import { Box, CardActionArea, Divider, SwipeableDrawer } from '@mui/material';
import { useState, forwardRef } from "react";
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import Modal from '@mui/material/Modal';
import Map from '../components/Common/Map';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import { ExpandLess, ExpandMore, FilterAlt, Sort } from '@mui/icons-material';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';


import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import ButtonGroup from '@mui/material/ButtonGroup';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import DateTimePicker from '@mui/lab/DateTimePicker';
import trLocale from 'date-fns/locale/tr';




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

const styleModal = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 600,
    bgcolor: 'background.paper',
    boxShadow: 24,
    p: 4,
    borderRadius: 2
};


function SearchScreen(props) {
    const [searchQuery, setSearchQuery] = useState("")
    const [position, setPosition] = useState()
    const [isSortedByLocation, setIsSortedByLocation] = useState(false)
    const [sportType, setSportType] = useState("")
    const [capacity, setCapacity] = useState("open_to_application")
    const [date, setDate] = useState("")
    const [radiusKm, setRadiusKm] = useState(2)
    const [startDate, setStartDate] = useState(new Date());
    const [endDate, setEndDate] = useState(new Date(new Date().getFullYear(), new Date().getMonth() + 1, new Date().getDate()));

    const handleFilter = () => {
        if (startDate === "Invalid Date" || endDate === "Invalid Date" || endDate < startDate)
            return handleOpenNotification()




        toggleFilterDrawer()
    }

    const [showPosts, setShowPosts] = useState(false)
    const handleSearch = () => {
        if (searchQuery === "basketball") {
            setShowPosts(true)
        } else {
            setShowPosts(false)
        }
    }

    const formatDate = (date) => {
        const temp = date.toLocaleString().split(',')
        return temp[0] + ":" + temp[1].split(':')[0].trim()
    }

    const formatRadius = radius => (radius / 90) // km to lat-lng


    const handleChange = (e) => {
        setSearchQuery(e.target.value)
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

    const [openMapModal, setOpenMapModal] = useState(false)
    const handleOpenMapModal = () => {
        setOpenMapModal(true)
    }
    const handleCloseMapModal = () => {
        setOpenMapModal(false)
    }

    const [anchorEl, setAnchorEl] = useState(null);
    const openSortMenu = Boolean(anchorEl);
    const handleOpenSortMenu = (event) => {
        setAnchorEl(event.currentTarget);
    };
    const handleCloseSortMenu = () => {
        setAnchorEl(null);
    };

    const [filterDrawer, setFilterDrawer] = useState(false)
    const toggleFilterDrawer = (status) => {
        setFilterDrawer(status)
    };

    const [openSportType, setOpenSportType] = useState(false)
    const [openCapacity, setOpenCapacity] = useState(false)
    const [openDate, setOpenDate] = useState(false)
    const [mode, setMode] = useState("events")



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
                <div className='col-3'>
                    <ToggleButtonGroup value={mode} onChange={(e, value) => setMode(value)} variant="outlined" exclusive >
                        <ToggleButton className="px-4" value="events">Events</ToggleButton>
                        <ToggleButton value="equipments">Equipments</ToggleButton>
                    </ToggleButtonGroup>
                </div>
            </div>
            <div className="row justify-content-center align-items-center mt-4">
                <div className="col-1 d-flex justify-content-end">
                    <ButtonGroup onClick={handleOpenSortMenu} variant="contained" aria-label="outlined button group">
                        <IconButton>
                            <Sort />
                        </IconButton>
                    </ButtonGroup>
                    <Menu
                        id="basic-menu"
                        anchorEl={anchorEl}
                        open={openSortMenu}
                        onClose={handleCloseSortMenu}
                        onClick={handleCloseSortMenu}
                        MenuListProps={{
                            'aria-labelledby': 'basic-button',
                        }}
                    >
                        <MenuItem style={{ paddingTop: 0, paddingBottom: 0 }} disabled><b>Sort by</b></MenuItem>
                        <Divider></Divider>
                        <MenuItem onClick={() => setIsSortedByLocation(false)} >Date</MenuItem>
                        <MenuItem onClick={() => setIsSortedByLocation(true)} >Location</MenuItem>
                    </Menu>
                </div>
                <div className="col-9 col-md-6">
                    <Paper
                        sx={{ p: '2px 4px', display: 'flex', alignItems: 'center' }}
                    >
                        <InputBase
                            sx={{ ml: 1, flex: 1 }}
                            placeholder="Search"
                            inputProps={{ 'aria-label': 'search' }}
                            value={searchQuery}
                            onChange={handleChange}
                        />
                        <IconButton onClick={handleSearch} sx={{ p: '10px' }} aria-label="search">
                            <SearchIcon />
                        </IconButton>
                    </Paper>
                </div>

                <div className="col-1 d-flex justify-content-start">
                    <ButtonGroup onClick={() => toggleFilterDrawer(true)} variant="contained" aria-label="outlined button group">
                        <IconButton>
                            <FilterAlt />
                        </IconButton>
                    </ButtonGroup>
                </div>
            </div>
            {
                showPosts &&
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
                <Alert onClose={handleCloseNotification} severity="error" sx={{ width: '100%' }}>
                    End date cannot be earlier than start date!
                </Alert>
            </Snackbar>
            <Modal
                open={openMapModal}
                onClose={handleCloseMapModal}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={styleModal}>
                    <Map height="500px" radiusKm={radiusKm} position={position} setPosition={setPosition} />
                    <div className="row justify-content-between mt-3">
                        <div className="col-5">
                            <TextField type="number" value={radiusKm} onChange={(e) => setRadiusKm(e.target.value)} id="outlined-basic" size="small" label="Radius (km)" variant="outlined" />
                        </div>
                        <div className="col-5 d-flex justify-content-end">
                            <Button onClick={handleCloseMapModal} variant="contained">Choose Location</Button>
                        </div>
                    </div>
                </Box>
            </Modal>
            <SwipeableDrawer
                anchor='right'
                open={filterDrawer}
                onClose={() => toggleFilterDrawer(false)}
                onOpen={() => toggleFilterDrawer(true)}
            >
                <Box
                    sx={{ width: 400, marginTop: "67px" }}
                    role="presentation"
                >
                    <List>
                        <ListItem button onClick={() => setOpenSportType((old) => !old)}>
                            <ListItemText primary={'Sport Type'} />
                            <ListItemIcon>
                                {openSportType ? <ExpandLess /> : <ExpandMore />}
                            </ListItemIcon>
                        </ListItem>
                        <Collapse in={openSportType} timeout="auto" unmountOnExit>
                            <List component="div" className="mt-2">
                                <TextField sx={{ ml: 4 }} value={sportType} onChange={(e) => setSportType(e.target.value)} id="outlined-basic" size="small" label="Sport Type" variant="outlined" />
                            </List>
                        </Collapse>

                        <ListItem button onClick={() => setOpenCapacity((old) => !old)}>
                            <ListItemText primary={'Capacity'} />
                            <ListItemIcon>
                                {openCapacity ? <ExpandLess /> : <ExpandMore />}
                            </ListItemIcon>
                        </ListItem>
                        <Collapse in={openCapacity} timeout="auto" unmountOnExit>
                            <List component="div" className="mt-2">
                                <RadioGroup sx={{ ml: 4 }} value={capacity} onChange={(e) => setCapacity(e.target.value)} name="row-radio-buttons-group">
                                    <FormControlLabel value="open_to_application" control={<Radio />} label="Open to application" />
                                    <FormControlLabel value="full" control={<Radio />} label="Full" />
                                    <FormControlLabel value="cancelled" control={<Radio />} label="Cancelled" />
                                </RadioGroup>
                            </List>
                        </Collapse>

                        <ListItem button onClick={() => setOpenDate((old) => !old)}>
                            <ListItemText primary={'Date'} />
                            <ListItemIcon>
                                {openDate ? <ExpandLess /> : <ExpandMore />}
                            </ListItemIcon>
                        </ListItem>
                        <Collapse in={openDate} timeout="auto" unmountOnExit>
                            <List component="div" className="row mt-2 px-4">
                                <div className='col-12 d-flex mb-3'>
                                    <LocalizationProvider dateAdapter={AdapterDateFns} locale={trLocale}>
                                        <DateTimePicker
                                            renderInput={(props) => <TextField {...props} />}
                                            label="Start Date"
                                            value={startDate}
                                            onChange={(newValue) => {
                                                setStartDate(newValue);
                                            }}
                                        />
                                    </LocalizationProvider>
                                </div>
                                <div className='col-12 d-flex'>
                                    <LocalizationProvider dateAdapter={AdapterDateFns} locale={trLocale}>
                                        <DateTimePicker
                                            renderInput={(props) => <TextField {...props} />}
                                            label="End Date"
                                            value={endDate}
                                            onChange={(newValue) => {
                                                setEndDate(newValue);
                                            }}
                                        />
                                    </LocalizationProvider>
                                </div>
                            </List>
                        </Collapse>

                        <ListItem button onClick={handleOpenMapModal}>
                            <ListItemText primary={'Location'} />
                        </ListItem>

                    </List>
                    <div className="justify-content-center d-flex mt-3">
                        <Button onClick={handleFilter} variant="contained">Filter</Button>
                    </div>
                </Box>
            </SwipeableDrawer>
        </div >

    );
}

export default SearchScreen;


