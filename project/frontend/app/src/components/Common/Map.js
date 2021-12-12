import { useEffect } from 'react'
import { MapContainer, TileLayer, Marker, Circle, useMapEvents } from 'react-leaflet'


const defaultPosition = [41.0860262, 29.0468946]

function CustomMarker(props) {
    const map = useMapEvents({
        click(e) {
            // const x = e.latlng
            // console.log(Math.sqrt(((x.lat - z.lat) ** 2 + (x.lng - z.lng) ** 2)))
            // z = e.latlng
            props.setPosition(e.latlng)
        },
        locationfound(e) {
            map.setView(e.latlng, map.getZoom())
        },
    })
    useEffect(() => {
        map.locate()
    }, [map])

    return (
        <>
            {props.position && <Marker position={props.position} />}
            {props.position && parseFloat(props.radiusKm) && <Circle center={props.position} pathOptions={{ color: 'red' }} radius={parseFloat(props.radiusKm) * 930} />}
        </>
    )
}

function Map(props) {
    return (
        <div>
            <MapContainer style={{ height: props.height }} center={defaultPosition} zoom={13} scrollWheelZoom={false}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <CustomMarker {...props} />

            </MapContainer>
        </div>
    )
}


export default Map

