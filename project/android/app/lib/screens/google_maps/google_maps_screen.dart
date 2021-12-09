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
    return Stack(children: <Widget>[
      Align(
        alignment: Alignment.center,
        child: GoogleMap(
          initialCameraPosition: CameraPosition(
            target: LatLng(100, -100),
            zoom: 15.0,
          ),
          circles: Set.from(collectionCircles),
          markers: Set.from(collectionMarkers),
          onTap: _handleTap,
        ),
      ),
      Padding(
        padding: const EdgeInsets.only(left: 80.0,right: 8.0,top: 8.0,bottom: 8.0),
        child: Align(
          alignment: Alignment.bottomLeft,

          child: FloatingActionButton(
            backgroundColor: Colors.orangeAccent,
            onPressed: () {},
            child: Icon(Icons.arrow_left),
          ),
        ),
      ),
      Padding(
        padding: const EdgeInsets.only(left: 8.0,right: 80.0,top: 8.0,bottom: 8.0),
        child: Align(
          alignment: Alignment.bottomRight,
          child: FloatingActionButton(
            backgroundColor: Colors.orangeAccent,
            onPressed: () {},
            child: Icon(Icons.arrow_right),
          ),
        ),
      ),
      Padding(
        padding: const EdgeInsets.all(8.0),
        child: Align(
          alignment: Alignment.bottomCenter,
          child: FloatingActionButton(
            backgroundColor: Colors.orangeAccent,
            onPressed: () {},
            child: Icon(Icons.arrow_upward),
          ),
        ),
      ),
    ]);
  }

  _handleTap(LatLng tappedPoint) {
    print(tappedPoint); // the lat / long values of tapped point.
    setState(() {
      collectionCircles = [];
      collectionCircles.add(Circle(
          strokeWidth: 3,
          fillColor: Colors.lightBlueAccent.withOpacity(0.2),
          circleId: CircleId(tappedPoint.toString()),
          radius: 500,
          center: LatLng(tappedPoint.latitude, tappedPoint.longitude)));
      collectionMarkers = [];
      collectionMarkers.add(Marker(
        markerId: MarkerId(tappedPoint.toString()),
        position: tappedPoint,
      ));
    });
  }
}
