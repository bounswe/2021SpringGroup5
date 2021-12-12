import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class GoogleMapsScreen extends StatefulWidget {
  const GoogleMapsScreen({Key? key}) : super(key: key);

  @override
  _GoogleMapsScreenState createState() => _GoogleMapsScreenState();
}

class _GoogleMapsScreenState extends State<GoogleMapsScreen> {
  List<Marker> collectionMarkers = [];
  List<Circle> collectionCircles = [];

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Align(
          alignment: Alignment.center,
          child: GoogleMap(
            initialCameraPosition: CameraPosition(
              target: LatLng(100, -100),
              zoom: 15.0,
            ),
            circles: Set.from(collectionCircles),
            markers: Set.from(collectionMarkers),
            onTap: handleTap,
            // onLongPress: changeRadius,
          ),
        ),
      ],
    );
  }

  handleTap(LatLng tappedPoint) {
    print(tappedPoint); // the lat / long values of tapped point.
    setState(() {
      collectionCircles = [];
      collectionMarkers = [];
      collectionMarkers.add(Marker(
        markerId: MarkerId(tappedPoint.toString()),
        position: tappedPoint,
      ));
      collectionCircles.add(Circle(
        circleId: CircleId(tappedPoint.toString()),
        center: LatLng(tappedPoint.latitude, tappedPoint.longitude),
        radius: 100,
      ));
    });
  }
}
