import 'package:flutter/material.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/create_event/create_event_screen.dart';
import 'package:ludo_app/screens/filter_popup/filter_popup_screen.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/popup_event_details/popup_event_details.dart';
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
  /*
  final List<Map<String, dynamic>> eventList = [
    {
      "id": 1,
      "name": "Tek Pota Basket Maçı",
      "description": 'Güzel bir maç olması dileğiyle!',
      "image": "assets/images/basketball-sport.jpg",
      "location": "Uçaksavar Stadyumu",
      "datetime": "2021-12-19 20:00"
    },
    {
      "id": 2,
      "name": "Cumartesi Frizbi'si",
      "description": 'Çimlerde frizbi fırlatacak arkadaşlar buraya!',
      "image": "assets/images/frisbee-sport.jpg",
      "location": "Boğaziçi Güney Çimler",
      "datetime": "2021-12-17 15:00"
    },
    {
      "id": 3,
      "name": " Tek Kale Futbol Maçı",
      "description": 'Genç yeetenekleri bekliyorum!',
      "image": "assets/images/football-sport.jpg",
      "location": "Etiler Naturel Park",
      "datetime": "2021-12-25 23:30"
    },
    {
      "id": 4,
      "name": "Boğaz'a Karşı Yüzelim",
      "description": 'Haydi, bu sıcak günün tadını çıkaralım!',
      "image": "assets/images/swimming-sport.jpg",
      "location": "Bebek Havuzu",
      "datetime": "2021-12-19 12:00"
    },
    {
      "id": 5,
      "name": "Namaste!",
      "description": 'Bugünki Meditasyonunu yaptın mı?',
      "image": "assets/images/yoga-sport.jpg",
      "location": "Etiler Sanatçılar Parkı",
      "datetime": "2021-12-20 14:35"
    },
    {
      "id": 6,
      "name": "Squash Oynayacak Sporcuları Arıyorum",
      "description": 'Rekabetli bir oyun olsun!',
      "image": "assets/images/squash-sport.jpg",
      "location": "HillSide Spor Kompleksi",
      "datetime": "2021-12-17 09:30"
    },
    {
      "id": 7,
      "name": "Sahilde Bisiklet Etkinliği",
      "description": 'Boğaza karşı bisiklet sürelim!',
      "image": "assets/images/bicycle-sport.jpg",
      "location": "Bebek İskele",
      "datetime": "2021-12-16 09:30"
    },
    {
      "id": 8,
      "name": "Doğa Yürüyüşüne Var Mısın?",
      "description": 'Atatürk Arberatumunda Eşşiz Bir Rotada!',
      "image": "assets/images/walking-sport.jpg",
      "location": "Atatürk Arberatumunu",
      "datetime": "2021-12-25 15:00"
    },
  ];
   */

  List<Map<String, dynamic>> afterSearchActionEvents = [];

  @override
  initState() {
    if(widget.willFetchAllEvents){
      fetchEvents();
    }
    afterSearchActionEvents = eventList;
    super.initState();
  }

  void sortByDate() {
    eventList.sort((a, b) => a['datetime'].compareTo(b['datetime']));
    setState(() {
      //girdiden sonra sonuçları yansıtma ve search olmuşsa yine de searched eventleri sortluyor.
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void sortByName() {
    eventList.sort((a, b) => a['name'].compareTo(b['name']));
    setState(() {
      //girdiden sonra sonuçları yansıtma ve search olmuşsa yine de searched eventleri sortluyor.
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void searchAction(String userInputText) {
    List<Map<String, dynamic>> results = [];
    if (userInputText.isEmpty) {
      //girdi olmazsa tüm eventler gözükecek
      results = eventList;
    } else {
      results = eventList
          .where((event) =>
              event["name"].toLowerCase().contains(userInputText.toLowerCase()))
          .toList();
    }
    setState(() {
      //girdiden sonra sonuçları yansıtma
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
                              Navigator.of(context)
                                  .push(PopupCardEffect(builder: (context) {
                                return PopupEventDetails();
                              }));
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
