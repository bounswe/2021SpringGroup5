import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';

class FilterScreen extends StatefulWidget {
  const FilterScreen({Key? key}) : super(key: key);

  @override
  _FilterScreenState createState() => _FilterScreenState();
}

class _FilterScreenState extends State<FilterScreen> {
  bool _todayflag = true;
  bool _thisweekflag = true;
  bool _thismonthflag = true;
  bool _alltimeflag = true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Filter Events"),
        ),
        body: Padding(
          padding: const EdgeInsets.all(5.0),
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.only(
                    left: 8.0, right: 8.0, top: 3.0, bottom: 8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Event Date",
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
                              setState(() => _todayflag = !_todayflag),
                          child: Text(_todayflag ? 'TODAY' : 'TODAY'),
                          style: ElevatedButton.styleFrom(
                            primary: _todayflag
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
                              setState(() => _thisweekflag = !_thisweekflag),
                          child:
                              Text(_thisweekflag ? 'THIS WEEK' : 'THIS WEEK'),
                          style: ElevatedButton.styleFrom(
                            primary: _thisweekflag
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
                              setState(() => _thismonthflag = !_thismonthflag),
                          child: Text(
                              _thismonthflag ? 'THIS MONTH' : 'THIS MONTH'),
                          style: ElevatedButton.styleFrom(
                            primary: _thismonthflag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 5,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _alltimeflag = !_alltimeflag),
                          child: Text(_alltimeflag ? 'ALL' : 'ALL'),
                          style: ElevatedButton.styleFrom(
                            primary: _alltimeflag
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
                      child: const Text("Location",
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
                    "FILTER",
                    style: TextStyle(fontSize: 16),
                  )) //map
            ],
          ),
        ));
  }
}
