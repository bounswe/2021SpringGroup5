import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

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
  bool _opentoapplicationflag = true;
  bool _fullflag = true;
  bool _cancelledflag = true;
  List<double> mapCallback = [];

  final sportTypeController = TextEditingController();

  _updateLocation(List<double> maps){
    setState(() {
      mapCallback = maps;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Filter Events"),
        ),
        body: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(5.0),
            child: Column(
              children: [
                Padding(
                  padding: const EdgeInsets.only(
                      left: 8.0, right: 8.0, top: 3.0, bottom: 8.0),
                  child: Row(
                    children: [
                      Container(
                          decoration: BoxDecoration(
                              color: Colors.blue.withOpacity(0.4)),
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
                      borderRadius: BorderRadius.circular(10)),
                  child: Padding(
                    padding: const EdgeInsets.only(
                        left: 4.0, right: 4.0, top: 3.0, bottom: 3.0),
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
                            onPressed: () => setState(
                                () => _thismonthflag = !_thismonthflag),
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
                        child: const Text("Sport Type",
                            style: TextStyle(fontSize: 16)))
                  ]),
                ),
                Container(
                    child: TextFormField(
                      decoration: InputDecoration(
                        hintText: ('Type here...'),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(10.0),
                          borderSide: BorderSide(),
                        ),
                      ),
                      keyboardType: TextInputType.text,
                      controller: sportTypeController,
                    )),
                const SizedBox(height: 1, width: 10),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Row(children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Capacity",
                            style: TextStyle(fontSize: 16)))
                  ]),
                ),
                Container(
                  decoration: BoxDecoration(
                      border: Border.all(),
                      borderRadius: BorderRadius.circular(10)),
                  child: Padding(
                    padding: const EdgeInsets.only(
                        left: 8.0, right: 8.0, top: 3.0, bottom: 3.0),
                    child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          ElevatedButton(
                            onPressed: () => setState(() =>
                                _opentoapplicationflag =
                                    !_opentoapplicationflag),
                            child: Text(_opentoapplicationflag
                                ? 'OPEN TO APPLY'
                                : 'OPEN TO APPLY'),
                            style: ElevatedButton.styleFrom(
                              primary: _opentoapplicationflag
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
                                setState(() => _fullflag = !_fullflag),
                            child: Text(_fullflag ? 'FULL' : 'FULL'),
                            style: ElevatedButton.styleFrom(
                              primary: _fullflag
                                  ? Colors.grey
                                  : Colors.lightBlue, // This is what you need!
                            ),
                          ),
                          const SizedBox(
                            width: 1,
                            height: 1,
                          ),
                          ElevatedButton(
                            onPressed: () => setState(
                                () => _cancelledflag = !_cancelledflag),
                            child: Text(
                                _cancelledflag ? 'CANCELLED' : 'CANCELLED'),
                            style: ElevatedButton.styleFrom(
                              primary: _cancelledflag
                                  ? Colors.grey
                                  : Colors.lightBlue, // This is what you need!
                            ),
                          ),
                          const SizedBox(
                            width: 1,
                            height: 5,
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
                      borderRadius: BorderRadius.circular(10)),
                  child: Padding(
                    padding: const EdgeInsets.all(4.0),
                    child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          SizedBox(
                            child: GoogleMapsScreen(parentAction: _updateLocation),
                            height: MediaQuery.of(context).size.height * 0.59,
                            width: MediaQuery.of(context).size.width * 0.93,
                          ),
                        ]),
                  ),
                ),

                ElevatedButton(
                    onPressed: () {
                      showAlertDialog(
                        context, _todayflag, _thisweekflag, _thismonthflag, _alltimeflag,
                          _opentoapplicationflag, _fullflag, _cancelledflag, mapCallback,
                        sportType: sportTypeController.text);
                      },
                    child: const Text(
                      "FILTER",
                      style: TextStyle(fontSize: 16),
                    )), //map
                Text(mapCallback.toString()),
              ],
            ),
          ),
        ));
  }
}

showAlertDialog(BuildContext context, todayflag, thisweekflag, thismonthflag, alltimeflag,
    opentoapplicationflag, fullflag, cancelledflag, mapCallback,
    {sportType = ""}) async {


  Future<String>? _futureResponse;
  FutureBuilder<String> buildFutureBuilder() {
    return FutureBuilder<String>(
      future: _futureResponse,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text(snapshot.data!);
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }
  String capacity = "open to applications";
  //if (fullflag) capacity = "full";
  //else if (cancelledflag) capacity = "cancelled";

  var params = {
    "status": "upcoming",
    "search_query": "",
    "sort_func": {
      "isSortedByLocation": true
    },
    "filter_func": {
      "location": {
        "lat": mapCallback[0],
        "lng": mapCallback[1],
        "radius": mapCallback[2]
      },
      "sportType": sportType,
      "date": null,
      "capacity": capacity
    }
  };
  print(params);
  _futureResponse = filterEvents(params, context);
  // late var futureRegister = fetchRegister();
  // print(futureRegister);
  // set up the AlertDialog
  AlertDialog alert = AlertDialog(
    content: buildFutureBuilder(),
  );

  // show the dialog
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return alert;
    },
  );
}

Future<String> filterEvents(params, BuildContext context) async {
  final response = await http.post(
    Uri.parse('http://3.122.41.188:8000/search/search_event/'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(params),
  );

  if (response.statusCode == 200) {

    // TODO: RETURN TO MAIN WITH EVENTS

    return response.body;

  } else {
    // If the server did not return a 201 CREATED response,
    // then throw an exception.
    throw Exception(json.decode(response.body)['errormessage']);
  }
}