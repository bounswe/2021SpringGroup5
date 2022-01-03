import IconButton from '@mui/material/IconButton';
import { Divider } from '@mui/material';
import MilitaryTechIcon from '@mui/icons-material/MilitaryTech';
import { useState, useEffect } from 'react';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import ButtonGroup from '@mui/material/ButtonGroup';
import { getAllBadgesRequest, sendBadgeRequest } from '../../services/BadgeService';


function Badge(props) {
    const [allBadges, setAllBadges] = useState([])

    const handleGetAllBadgesRequest = async () => {
        try {
            const response = await getAllBadgesRequest();
            setAllBadges(response.data);
        } catch (e) {
            console.log(e);
        }
    }

    const handleSendBadgeRequest = async (badge) => {
        try {
            const response = await sendBadgeRequest({
                userId: props.userId,
                badgeName: badge.name
            });
            console.log(response);
        } catch (e) {
            console.log(e);
        }
    }

    useEffect(() => {
        handleGetAllBadgesRequest()
    }, [])

    const [anchorEl, setAnchorEl] = useState(null);
    const openSortMenu = Boolean(anchorEl);
    const handleOpenSortMenu = event => {
        setAnchorEl(event.currentTarget);
    };
    const handleCloseSortMenu = () => {
        setAnchorEl(null);
    };

    return (
        <div>
            {(props.eventDate < new Date()) &&
                <div className="col-1 d-flex justify-content-end">
                    <ButtonGroup onClick={handleOpenSortMenu} variant="contained" aria-label="outlined button group">
                        <IconButton>
                            <MilitaryTechIcon />
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
                        <MenuItem style={{ paddingTop: 0, paddingBottom: 0 }} disabled>
                            <b>Choose a badge</b>
                        </MenuItem>
                        <Divider></Divider>
                        {allBadges.map(badge => (
                            <MenuItem onClick={() => handleSendBadgeRequest(badge)}>{badge.name}</MenuItem>
                        ))}
                    </Menu>
                </div>
            }
        </div>
    );
}

export default Badge;
