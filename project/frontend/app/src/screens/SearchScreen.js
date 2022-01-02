
import { useState } from 'react';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import ToggleButton from '@mui/material/ToggleButton';
import EquipmentSearch from '../components/SearchScreen/EquipmentSearch.js'
import EventSearch from '../components/SearchScreen/EventSearch.js'

function SearchScreen(props) {
    const [mode, setMode] = useState('events');

    return (
        <div className="container">
            <div className="row justify-content-center align-items-center mt-5">
                <div className="col-3">
                    <ToggleButtonGroup value={mode} onChange={(e, value) => setMode(value)} variant="outlined" exclusive>
                        <ToggleButton className="px-4" value="events">
                            Events
                        </ToggleButton>
                        <ToggleButton value="equipments">Equipments</ToggleButton>
                    </ToggleButtonGroup>
                </div>
            </div>

            {mode == "events" &&
                <EventSearch />
            }
            {mode == "equipments" &&
                <EquipmentSearch />
            }

        </div>
    );
}

export default SearchScreen;
