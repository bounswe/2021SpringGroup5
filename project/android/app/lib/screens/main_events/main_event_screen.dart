import 'package:flutter/material.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/popup_event_details/popup_event_details.dart';

class MainEventScreen extends StatefulWidget {
  const MainEventScreen({Key? key}) : super(key: key);

  @override
  _MainEventScreenState createState() => _MainEventScreenState();
}

class _MainEventScreenState extends State<MainEventScreen> {
  final List<Map<String, dynamic>> _eventList = [
    {
      "id": 1,
      "name": "1v1 Voleybol Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 2,
      "name": "1v1 Frizbi Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 3,
      "name": "1v1 Basketbol Maçı",
      "description":
          'Rekabetli Olkmdfksmd skmfsdkmfskdmfskd mfks dmfsk dmfks dmfks mfdk acak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 4,
      "name": "1v1 Kriket Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 5,
      "name": "1v1 Futbol Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 6,
      "name": "1v1 Boks Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 7,
      "name": "1v1 Bisiklet Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 8,
      "name": "1v1 Aikido Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 9,
      "name": "1v1 Yoga Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
    {
      "id": 10,
      "name": "1v1 Yüzme Maçı",
      "description": 'Rekabetli Olacak',
      "image": "assets/images/basketball_event.png",
      "location": "etiler merkez",
      "datetime": "12.10 - 16:00"
    },
  ];

  List<Map<String, dynamic>> _afterSearchActionEvents = [];

  @override
  initState() {
    _afterSearchActionEvents = _eventList;
    super.initState();
  }

  void _searchAction(String userInputText) {
    List<Map<String, dynamic>> results = [];
    if (userInputText.isEmpty) {
      //girdi olmazsa tüm eventler gözükecek
      results = _eventList;
    } else {
      results = _eventList
          .where((event) =>
              event["name"].toLowerCase().contains(userInputText.toLowerCase()))
          .toList();
    }
    setState(() {
      //girdiden sonra sonuçları yansıtma
      _afterSearchActionEvents = results;
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
                    onPressed: () {},
                    icon: Icon(
                      Icons.filter_list,
                      color: Colors.green,
                    )),
              ],
            ),
            Expanded(
              child: _afterSearchActionEvents.isNotEmpty
                  ? ListView.builder(
                      itemCount: _afterSearchActionEvents.length,
                      itemBuilder: (context, index) => Card(
                        elevation: 5,
                        key: ValueKey(_afterSearchActionEvents[index]["id"]),
                        color: Colors.white,
                        margin: const EdgeInsets.symmetric(vertical: 9),
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
                                _afterSearchActionEvents[index]['image']),
                          ),
                          title: Text(_afterSearchActionEvents[index]['name']),
                          subtitle: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                  '${_afterSearchActionEvents[index]["location"]}'),
                              Text(
                                  '${_afterSearchActionEvents[index]["datetime"].toString()}'),
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
                                SizedBox(
                                  height: 5,
                                  width: 5,
                                ),
                                FloatingActionButton(
                                  onPressed: () {},
                                  child: Text('JOIN'),
                                ),
                              ]),
                        ),
                      ),
                    )
                  : const Text(
                      'Event is not found!',
                      style: TextStyle(fontSize: 20),
                    ),
            ),
          ],
        ),
      ),
    );
  }
}
