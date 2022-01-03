import 'package:flutter/material.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';

class EventDetailsScreen extends StatelessWidget {
  const EventDetailsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    const List<Map<String, dynamic>> participants = [
      {
        "name": "Rekabetli Oyuncu",
        "image": "assets/images/basketball-sport.jpg",
      },
      {
        "name": "Rekabetli Oyuncu",
        "image": "assets/images/basketball-sport.jpg",
      },
    ];
    return Scaffold(
      appBar: AppBar(
        title: Text("Event Details:"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Material(
          color: Colors.white.withOpacity(0.95),
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(15),
              child: Column(
                children: [
                  Row(
                    children: const [
                      Text(
                        // if event creator
                        "This Event's Participants:",
                        style: TextStyle(
                            backgroundColor: Colors.lightGreenAccent,
                            fontSize: 16),
                      ),
                    ],
                  ),
                  /*
                  Expanded(
                      child: ListView.builder(
                        itemCount: participants.length,
                        itemBuilder: (context, index) => Card(
                          elevation: 5,
                          key: ValueKey([index][0]),
                          color: Colors.white,
                          margin: const EdgeInsets.symmetric(vertical: 10),
                          child: Padding(
                            padding: const EdgeInsets.all(13.0),
                            child: ListTile(
                                onTap: () {}, // navigate to users profile
                                leading: Image(
                                  fit: BoxFit.cover,
                                  image:
                                      AssetImage(participants[index]['image']),
                                ),
                                title: participants[index]["name"]),
                          ),
                        ),
                      ),
                    ),
                  ),*/
                  SizedBox(
                    height: 15,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Event Name:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Owner of event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Sport name:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Date and Time of Post",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Description:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Lat-Long:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Date Time of Event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Participation Limit:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Spectator Limit:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Event Rules:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Equipment Requirements:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Status of Event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Capacity of Event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Location Requirement:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Contact Information:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Image url:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Skill Requirement:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Number of Accepted Players:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Badges:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Number of Accepted Spectators:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Comments:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Accepted USer Info:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Rejected User Info:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Accepted Spectator Info:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: const [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Waiting User Info:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Text(
                        "GGGG Game",
                        style: TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) {
                            return MainEventScreen();
                          },
                        ),
                      );
                    },
                    child: const Text(
                      'APPLY EVENT',
                      style: TextStyle(fontSize: 15),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
