import 'dart:math';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class GoogleMapsScreen extends StatefulWidget {
  const GoogleMapsScreen({Key? key}) : super(key: key);

  @override
  _GoogleMapsScreenState createState() => _GoogleMapsScreenState();
}

class _GoogleMapsScreenState extends State<GoogleMapsScreen> {
  double _value = 5;
  List<Marker> collectionMarkers = [];
  List<Circle> collectionCircles = [];

  @override
  Widget build(BuildContext context) {
    return Stack(children: [
      Container(
        child: Align(
          alignment: Alignment.center,
          child: GoogleMap(
            initialCameraPosition: CameraPosition(
              target: LatLng(41.083556, 29.050598),
              zoom: 14.9,
            ),
            circles: Set.from(collectionCircles),
            markers: Set.from(collectionMarkers),
            onTap: handleTap,
            onLongPress: changeRadius,
          ),
        ),
      ),
    ]);
  }

  handleTap(LatLng tappedPoint) {
    print(tappedPoint); // the lat / long values of tapped point.
    setState(() {
      collectionCircles.clear();
      collectionMarkers = [];
      collectionMarkers.add(Marker(
        markerId: MarkerId(tappedPoint.toString()),
        position: tappedPoint,
      ));
    });
  }

  changeRadius(LatLng pressedPoint) {
// the lat / long values of tapped point.
    setState(() {
      collectionCircles = [];
      collectionCircles.add(Circle(
        strokeWidth: 10,
        strokeColor: Colors.black,
        fillColor: Colors.blue.withOpacity(0.3),
        circleId: CircleId(pressedPoint.toString()),
        center: LatLng(collectionMarkers[0].position.latitude,
            collectionMarkers[0].position.longitude),
        radius: 98760 * //actually this would be 110574 as 1 degree is 110574 km
            sqrt((((pressedPoint.longitude -
                            collectionMarkers[0].position.longitude) *
                        (pressedPoint.longitude -
                            collectionMarkers[0].position.longitude)) +
                    ((pressedPoint.latitude -
                            collectionMarkers[0].position.latitude) *
                        (pressedPoint.latitude -
                            collectionMarkers[0].position.latitude)))
                .abs()),
      ));
    });
  }
}
