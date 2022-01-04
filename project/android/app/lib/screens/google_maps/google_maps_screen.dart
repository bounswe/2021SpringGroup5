import 'dart:math';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class GoogleMapsScreen extends StatefulWidget {

  final ValueChanged<List<double>> parentAction;
  const GoogleMapsScreen({Key? key, required this.parentAction}) : super(key: key);

  @override
  _GoogleMapsScreenState createState() => _GoogleMapsScreenState();
}

class _GoogleMapsScreenState extends State<GoogleMapsScreen> {
  List<Marker> collectionMarkers = [];
  List<Circle> collectionCircles = [];
  List<double> mapCallback = [0.0, 0.0, 0.0];

  @override
  Widget build(BuildContext context) {
    return Stack(children: [
      Container(
        child: Align(
          alignment: Alignment.center,
          child: GoogleMap(
            initialCameraPosition: const CameraPosition(
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
      //Text(collectionMarkers[0].position),
      //Text(collectionCircles[0].radius),
    ]);
  }


  handleTap(LatLng tappedPoint) {
    //print(tappedPoint); // the lat / long values of tapped point.
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
        radius: 97000 * //actually this would be 110574 as 1 degree is 110574 km
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

      mapCallback[0] = (collectionMarkers[0].position.latitude);
      mapCallback[1] = (collectionMarkers[0].position.longitude);
      mapCallback[2] = (collectionCircles[0].radius);
      widget.parentAction(mapCallback);
    });
  }
}
