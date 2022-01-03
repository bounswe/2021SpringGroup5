import 'package:flutter/material.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/create_event/create_event_screen.dart';
import 'package:ludo_app/screens/filter_popup/filter_popup_screen.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/event_page/popup_event_details.dart';
import 'package:ludo_app/screens/user_profile/components/body.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:ludo_app/globals.dart' as globals;

class MainEventScreen extends StatefulWidget {

  final bool willFetchAllEvents;
  const MainEventScreen({Key? key, this.willFetchAllEvents = false}) : super(key: key);


  @override
  _MainEventScreenState createState() => _MainEventScreenState();
}

class _MainEventScreenState extends State<MainEventScreen> {
  var now_1d = DateTime.now().subtract(const Duration(days: 1));
  var now_1w = DateTime.now().subtract(const Duration(days: 7));
  var now_1m = DateTime(
      DateTime.now().year, DateTime.now().month - 1, DateTime.now().day);

  final List<Map<String, dynamic>> eventList = [];

  List<Map<String, dynamic>> afterSearchActionEvents = [];

  @override
  initState() {
    if (widget.willFetchAllEvents) {
      fetchEvents();
    }
    afterSearchActionEvents = eventList;
    super.initState();
  }

  void sortByDate() {
    eventList.sort((a, b) => a['datetime'].compareTo(b['datetime']));
    setState(() {
      //list results after the input
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void sortByName() {
    eventList.sort((a, b) => a['name'].compareTo(b['name']));
    setState(() {
      ////list results after the input
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void searchAction(String userInputText) {
    List<Map<String, dynamic>> results = [];
    if (userInputText.isEmpty) {
      //if input = null, show all events
      results = eventList;
    } else {
      results = eventList
          .where((event) =>
          event["name"].toLowerCase().contains(userInputText.toLowerCase()))
          .toList();
    }
    setState(() {
      //list results after the input
      afterSearchActionEvents = results;
    });
  }

  Future fetchEvents() async {
    // Return all events
    var params = {
      "status": "upcoming",
      "search_query": "",
      "sort_func": {
        "isSortedByLocation": false
      },
      "filter_func": {
        "location": null,
        "sportType": "",
        "date": null,
        "capacity": "open to applications"
      }
    };
    final response = await http.post(
      Uri.parse('http://3.122.41.188:8000/search/search_event/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': globals.access,
        'Cookie': 'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}',
      },
      body: jsonEncode(params),
    );

    if (response.statusCode == 200) {
      WidgetsBinding.instance!.addPostFrameCallback((_){
        setState(() {
          eventList.clear();
          List events = jsonDecode(response.body);
          //print(events);
          for(var i = 0; i < events.length; i++){
            Map<String, dynamic> oneEvent = {
              "id": events[i]['pk'],
              "name": events[i]['post_name'],
              "description": events[i]['description'],
              "image": events[i]['pathToEventImage'],
              "location": "",
              "datetime": events[i]['created_date'],
            };
            eventList.add(oneEvent);
          }
          //print(eventList);
        });
      });
      return response.body;
    } else {
      Map responseBody = json.decode(response.body);
      if (responseBody.containsKey('errormessage')) {
        throw Exception(responseBody['errormessage']);
      } else if (responseBody.containsKey('message')){
        return response.body;
      }
    }
  }

  void _filterButtonNavigate(BuildContext context) async {
    // Navigator.push returns a Future that completes after calling
    // Navigator.pop on the Selection Screen.
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const FilterScreen()),
    );

    // After the Selection Screen returns a result, hide any previous snackbars
    // and show the new result.
    showAlertDialog(context, result[0], result[1], result[2], result[3],
        result[4], result[5], result[6], result[7], sportType: result[8]);
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
            List events = jsonDecode(snapshot.data!);
            WidgetsBinding.instance!.addPostFrameCallback((_){
              setState(() {
                eventList.clear();
                for(var i = 0; i < events.length; i++){
                  Map<String, dynamic> oneEvent = {
                    "id": events[i]['pk'],
                    "name": events[i]['post_name'],
                    "description": events[i]['description'],
                    "image": events[i]['pathToEventImage'],
                    "location": "",
                    "datetime": events[i]['created_date'],
                  };
                  eventList.add(oneEvent);
                }
              });
            });

            Navigator.pop(context);
            //return Text(snapshot.data!);
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
        'Authorization': globals.access,
        'Cookie': 'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}',
      },
      body: jsonEncode(params),
    );

    if (response.statusCode == 200) {

      //Navigator.pop(context, response.body);

      return response.body;

    } else {
      throw Exception(json.decode(response.body)['errormessage']);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            const SizedBox(
              height: 20,
            ),
            Row(
              children: [
                Flexible(
                  child: TextField(
                    onChanged: (value) => searchAction(value),
                    decoration: const InputDecoration(
                        labelText: 'Search For An Event',
                        prefixIcon: Icon(Icons.search)),
                  ),
                ),
                IconButton(
                    onPressed: () {
                      sortByName();
                    },
                    icon: const Icon(Icons.sort_by_alpha,
                        size: 25, color: Colors.blue)),
                IconButton(
                    onPressed: () {
                      sortByDate();
                    },
                    icon: const Icon(Icons.calendar_today,
                        size: 25, color: Colors.blue)),
                IconButton(
                  onPressed: () {
                    _filterButtonNavigate(context);
                  },
                  icon: const Icon(
                    Icons.filter_list,
                    color: Colors.blue,
                    size: 25,
                  ),
                ),
              ],
            ),
            Expanded(
              child: afterSearchActionEvents.isNotEmpty
                  ? ListView.builder(
                itemCount: afterSearchActionEvents.length,
                itemBuilder: (context, index) => Card(
                  elevation: 5,
                  key: ValueKey(afterSearchActionEvents[index]["id"]),
                  color: Colors.white,
                  margin: const EdgeInsets.symmetric(vertical: 10),
                  child: Padding(
                    padding: const EdgeInsets.all(13.0),
                    child: ListTile(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) {
                              return EventDetailsScreen();
                            },
                          ),
                        );
                      },
                      leading:
                      (afterSearchActionEvents[index]['image'] != '') ?
                      Image.network(afterSearchActionEvents[index]['image']) :
                      Image.asset('assets/images/default_event_image.png'),
                      title: Text(afterSearchActionEvents[index]['name']),
                      subtitle: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                              '${afterSearchActionEvents[index]["location"]}'),
                          Text(
                              '${afterSearchActionEvents[index]["datetime"].toString()}'),
                        ],
                      ),
                      trailing: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: <Widget>[
                            ElevatedButton(
                              onPressed: () {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) {
                                      return GoogleMapsScreen(
                                        parentAction: (List) => {},
                                      );
                                    },
                                  ),
                                );
                              },
                              child: Text('JOIN'),
                              style: ElevatedButton.styleFrom(
                                shape: CircleBorder(),
                                padding: EdgeInsets.all(20),
                              ),
                            ),
                          ]),
                    ),
                  ),
                ),
              )
                  : const Padding(
                padding: EdgeInsets.only(top: 20),
                child: Text(
                  'Event is not found!',
                  style: TextStyle(fontSize: 20),
                ),
              ),
            ),
          ],
        ),
      ),
      bottomSheet: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return ProfileScreen();
                    },
                  ),
                );
              },
              child: const Text(
                'PROFILE',
                style: TextStyle(fontSize: 15),
              )),
          ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return CreateEventScreen();
                    },
                  ),
                );
              },
              child: const Text(
                'CREATE EVENT',
                style: TextStyle(fontSize: 15),
              )),
        ],
      ),
    );
  }
}
