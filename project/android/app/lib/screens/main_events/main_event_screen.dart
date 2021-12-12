import 'package:flutter/material.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/filter_popup/filter_popup_screen.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/popup_event_details/popup_event_details.dart';

class MainEventScreen extends StatefulWidget {
  const MainEventScreen({Key? key}) : super(key: key);

  @override
  _MainEventScreenState createState() => _MainEventScreenState();
}

class _MainEventScreenState extends State<MainEventScreen> {
  var now_1d = DateTime.now().subtract(Duration(days: 1));
  var now_1w = DateTime.now().subtract(Duration(days: 7));
  var now_1m = DateTime(
      DateTime.now().year, DateTime.now().month - 1, DateTime.now().day);

  final List<Map<String, dynamic>> eventList = [
    {
      "id": 1,
      "name": "1v1 Voleybol Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 20:10"
    },
    {
      "id": 2,
      "name": "1v1 Frizbi Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/ludo_logo.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 15:20"
    },
    {
      "id": 3,
      "name": "1v1 Basketbol Maçı",
      "description":
          'Rekabetli Olkmdfksmd skmfsdkmfskdmfskd mfks dmfsk dmfks dmfks mfdk acak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-29 11:20"
    },
    {
      "id": 4,
      "name": "1v1 Kriket Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/squash-sport.jpg",
      "location": "etiler merkez",
      "datetime": "2021-11-24 11:11"
    },
    {
      "id": 5,
      "name": "1v1 Futbol Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 22:20"
    },
    {
      "id": 6,
      "name": "1v1 Boks Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 09:20"
    },
    {
      "id": 7,
      "name": "1v1 Bisiklet Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 06:40"
    },
    {
      "id": 8,
      "name": "1v1 Aikido Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 16:20"
    },
    {
      "id": 9,
      "name": "1v1 Yoga Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "2021-11-24 16:20"
    },
    {
      "id": 10,
      "name": "1v1 Yüzme Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/squash-sport.jpg",
      "location": "etiler merkez",
      "datetime": "2021-11-24 06:20"
    },
  ];

  List<Map<String, dynamic>> afterSearchActionEvents = [];

  @override
  initState() {
    afterSearchActionEvents = eventList;
    super.initState();
  }

  void sortByDate() {
    List<Map<String, dynamic>> results = [];
    eventList.sort((a, b) => a['datetime'].compareTo(b['datetime']));
    setState(() {
      //girdiden sonra sonuçları yansıtma
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void _searchAction(String userInputText) {
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
                    onChanged: (value) => _searchAction(value),
                    decoration: const InputDecoration(
                        labelText: 'Search For An Event',
                        prefixIcon: Icon(Icons.search)),
                  ),
                ),
                IconButton(
                    onPressed: () {
                      sortByDate();
                    },
                    icon: const Icon(Icons.sort_by_alpha, color: Colors.blue)),
                IconButton(
                  onPressed: () {
                    Navigator.of(context)
                        .push(PopupCardEffect(builder: (context) {
                      return FilterScreen();
                    }));
                  },
                  icon: const Icon(
                    Icons.filter_list,
                    color: Colors.blue,
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
                        child: ListTile(
                          onTap: () {
                            Navigator.of(context)
                                .push(PopupCardEffect(builder: (context) {
                              return PopupEventDetails();
                            }));
                          },
                          leading: Image(
                            fit: BoxFit.cover,
                            image: AssetImage(
                                afterSearchActionEvents[index]['image']),
                          ),
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
                                FloatingActionButton(
                                  backgroundColor: Colors.amber,
                                  onPressed: () {
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                        builder: (context) {
                                          return GoogleMapsScreen();
                                        },
                                      ),
                                    );
                                  },
                                  child: Text('MAP'),
                                ),
                                const SizedBox(
                                  height: 5,
                                  width: 5,
                                ),
                                FloatingActionButton(
                                  onPressed: () {
                                    Navigator.push(
                                      context,
                                      MaterialPageRoute(
                                        builder: (context) {
                                          return GoogleMapsScreen();
                                        },
                                      ),
                                    );
                                  },
                                  child: Text('JOIN'),
                                ),
                              ]),
                        ),
                      ),
                    )
                  : Padding(
                      padding: const EdgeInsets.only(top: 20),
                      child: const Text(
                        'Event is not found!',
                        style: TextStyle(fontSize: 20),
                      ),
                    ),
            ),
          ],
        ),
      ),
    );
  }
}
