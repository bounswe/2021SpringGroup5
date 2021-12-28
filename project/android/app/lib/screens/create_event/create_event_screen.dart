import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';

class CreateEventScreen extends StatefulWidget {
  const CreateEventScreen({Key? key}) : super(key: key);

  @override
  _CreateEventScreenState createState() => _CreateEventScreenState();
}

class _CreateEventScreenState extends State<CreateEventScreen> {
  bool _beginnerFlag = true;
  bool _averageFlag = true;
  bool _skilledFlag = true;
  bool _expertFlag = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Create Your Event"),
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(5.0),
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Type Your Event Name",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                decoration: InputDecoration(
                  hintText: ('Type here...'),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(20.0),
                    borderSide: BorderSide(),
                  ),
                ),
                keyboardType: TextInputType.text,
              )),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Type Your Event Description",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),

              Container(
                  child: TextFormField(
                decoration: InputDecoration(
                  hintText: ('Type here...'),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(20.0),
                    borderSide: BorderSide(),
                  ),
                ),
                keyboardType: TextInputType.text,
              )),
              Padding(
                padding: const EdgeInsets.only(
                    left: 8.0, right: 8.0, top: 6.0, bottom: 8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Select the Skill Level Requirement",
                            style: TextStyle(fontSize: 16))),
                    //type
                  ],
                ),
              ),
              const SizedBox(height: 1, width: 10),

              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(20)),
                child: Padding(
                  padding: const EdgeInsets.only(
                      left: 8.0, right: 8.0, top: 3.0, bottom: 3.0),
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _beginnerFlag = !_beginnerFlag),
                          child: Text(_beginnerFlag ? 'BEGINNER' : 'BEGINNER'),
                          style: ElevatedButton.styleFrom(
                            primary: _beginnerFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _averageFlag = !_averageFlag),
                          child: Text(_averageFlag ? 'AVERAGE' : 'AVERAGE'),
                          style: ElevatedButton.styleFrom(
                            primary: _averageFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _skilledFlag = !_skilledFlag),
                          child: Text(_skilledFlag ? 'SKILLED' : 'SKILLED'),
                          style: ElevatedButton.styleFrom(
                            primary: _skilledFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _expertFlag = !_expertFlag),
                          child: Text(_expertFlag ? 'EXPERT' : 'EXPERT'),
                          style: ElevatedButton.styleFrom(
                            primary: _expertFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                      ]),
                ),
              ),
              const SizedBox(height: 1, width: 10),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(children: [
                  Container(
                      decoration:
                          BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                      child: const Text("Mark Exact Location of Event",
                          style: TextStyle(fontSize: 16)))
                ]),
              ),
              const SizedBox(height: 1, width: 10),
              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(20)),
                child: Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        SizedBox(
                          child: const GoogleMapsScreen(),
                          height: MediaQuery.of(context).size.height * 0.59,
                          width: MediaQuery.of(context).size.width * 0.93,
                        ),
                      ]),
                ),
              ),
              const SizedBox(height: 1, width: 10),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Select the Date and Time of Event",
                            style: TextStyle(fontSize: 16))),
                    //type
                  ],
                ),
              ),

              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(20)),
                height: 200,
                child: CupertinoDatePicker(
                  mode: CupertinoDatePickerMode.dateAndTime,
                  initialDateTime: DateTime(2021, 12, 1, 12, 00),
                  onDateTimeChanged: (DateTime newDateTime) {
                    //Do Some thing
                  },
                  use24hFormat: false,
                  minuteInterval: 1,
                ),
              ),

              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return const MainEventScreen();
                      },
                    ),
                  );
                },
                child: const Text(
                  "CREATE",
                  style: TextStyle(fontSize: 16),
                ),
              ), //map
            ],
          ),
        ));
  }
}
