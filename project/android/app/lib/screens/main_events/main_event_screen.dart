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
      "name": " Çift Kale Futbol Maçı",
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

  List<Map<String, dynamic>> afterSearchActionEvents = [];

  @override
  initState() {
    afterSearchActionEvents = eventList;
    super.initState();
  }

  void sortByDate() {
    eventList.sort((a, b) => a['datetime'].compareTo(b['datetime']));
    setState(() {
      //girdiden sonra sonuçları yansıtma
      afterSearchActionEvents = eventList;
    });
    print("$eventList");
  }

  void sortByName() {
    eventList.sort((a, b) => a['name'].compareTo(b['name']));
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
                    Navigator.of(context)
                        .push(PopupCardEffect(builder: (context) {
                      return FilterScreen();
                    }));
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
