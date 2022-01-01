import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class GoogleMapsNoRadiusScreen extends StatefulWidget {

  final ValueChanged<List<double>> parentAction;
  const GoogleMapsNoRadiusScreen({Key? key, required this.parentAction}) : super(key: key);

  @override
  _GoogleMapsNoRadiusScreenState createState() => _GoogleMapsNoRadiusScreenState();
}

class _GoogleMapsNoRadiusScreenState extends State<GoogleMapsNoRadiusScreen> {
  List<Marker> collectionMarkers = [];
  List<double> mapCallback = [0.0, 0.0];

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
            markers: Set.from(collectionMarkers),
            onTap: handleTap,
          ),
        ),
      ),
      //Text(collectionMarkers[0].position),
      //Text(collectionCircles[0].radius),
    ]);
  }


  handleTap(LatLng tappedPoint) {
    print(tappedPoint); // the lat / long values of tapped point.
    setState(() {
      collectionMarkers = [];
      collectionMarkers.add(Marker(
        markerId: MarkerId(tappedPoint.toString()),
        position: tappedPoint,
      ));
      mapCallback[0] = (collectionMarkers[0].position.latitude);
      mapCallback[1] = (collectionMarkers[0].position.longitude);
      widget.parentAction(mapCallback);
    });
  }
}
