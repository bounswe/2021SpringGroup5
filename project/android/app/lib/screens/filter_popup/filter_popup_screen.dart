import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';

class FilterScreen extends StatefulWidget {
  const FilterScreen({Key? key}) : super(key: key);

  @override
  _FilterScreenState createState() => _FilterScreenState();
}

class _FilterScreenState extends State<FilterScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Filter Events"),
        ),
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            children: [
              Row(
                children: [Text('Sport Type')],
              ), //type
              Row(children: [Text('Date and Time')]), //date
              Row(children: [
                Container(
                    decoration:
                        BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                    child: Text("Location", style: TextStyle(fontSize: 16)))
              ]),
              SizedBox(height: 8),
              Row(mainAxisAlignment: MainAxisAlignment.center, children: [
                SizedBox(
                  child: GoogleMapsScreen(),
                  height: MediaQuery.of(context).size.height * 0.4,
                  width: MediaQuery.of(context).size.width * 0.95,
                ),
              ]), //map
            ],
          ),
        ));
  }
}
