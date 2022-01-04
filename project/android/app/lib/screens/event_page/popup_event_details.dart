import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:ludo_app/globals.dart' as globals;

class EventDetailsScreen extends StatefulWidget {
  int? eventId; // event id cannot be null

  EventDetailsScreen({Key? key, required this.eventId}) : super(key: key);

  @override
  State<EventDetailsScreen> createState() => _EventDetailsScreenState();
}

class _EventDetailsScreenState extends State<EventDetailsScreen> {
  Map eventDetails = {};

  Future fetchEventDetails() async {
    // Return all events
    var params = {
      "@context": "https://www.w3.org/ns/activitystreams",
      "summary": "${globals.name} read an event post",
      "type": "View",
      "actor": {
        "type": "Person",
        "name": globals.name,
        "surname": globals.surname,
        "username": globals.username,
        "Id": globals.userid,
      },
      "object": {
        "type": "EventPost",
        "post_id": widget.eventId,
      }
    };

    final response = await http.post(
      Uri.parse('http://3.122.41.188:8000/post/get_event_post_details/'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': globals.access,
        'Cookie':
            'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}',
      },
      body: jsonEncode(params),
    );
    if (response.statusCode == 201) {
      WidgetsBinding.instance!.addPostFrameCallback((_) {
        setState(() {
          eventDetails = jsonDecode(response.body)['object'];
          print(jsonDecode(response.body)['object']);
        });
      });
    } else {
      throw Exception(response.body);
    }
  }

  String capFirstLetter(String word) {
    return word[0].toUpperCase() + word.substring(1);
  }

  @override
  void initState() {
    fetchEventDetails();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Event Details"),
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
                    children: [
                      Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Expanded(
                          child: Text(
                            eventDetails.isEmpty
                                ? ""
                                : eventDetails['post_name'],
                            style: const TextStyle(
                              fontSize: 24,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Container(
                    child: eventDetails.isEmpty
                        ? Text("")
                        : eventDetails['pathToEventImage'] == ""
                            ? Image.asset(
                                'assets/images/default_event_image.png')
                            : Image.network(eventDetails['pathToEventImage']),
                  ),
                  /*
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
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Event Participants:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['accepted_players'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Owner of event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['owner']['name'] +
                                  ' ' +
                                  eventDetails['owner']['surname'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Sport name:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : capFirstLetter(eventDetails['sport_category']),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Created Date:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['created_date'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Description:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['description'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Lat-Long:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['latitude'].toString() +
                                  ', ' +
                                  eventDetails['longitude'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Event Date:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty ? "" : eventDetails['date_time'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Participation Limit:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['participant_limit'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Spectator Limit:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['spectator_limit'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Event Rules:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty ? "" : eventDetails['rule'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Equipment Requirements:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['equipment_requirement'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Status of Event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty ? "" : eventDetails['status'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Capacity of Event:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty ? "" : eventDetails['capacity'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Location Requirement:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['location_requirement'] == ""
                                  ? "None"
                                  : eventDetails['location_requirement'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Contact Information:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['contact_info'] == ""
                                  ? "None"
                                  : eventDetails['contact_info'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Skill Requirement:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['skill_requirement'],
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Number of Accepted Players:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['current_player'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Number of Accepted Spectators:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['current_spectator'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(
                    children: [
                      const Padding(
                        padding: EdgeInsets.only(right: 20),
                        child: Text(
                          "Comments:",
                          style: TextStyle(
                              backgroundColor: Colors.lightGreenAccent,
                              fontSize: 16),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          eventDetails.isEmpty
                              ? ""
                              : eventDetails['comments'].toString(),
                          style: TextStyle(fontSize: 16),
                        ),
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
                            return Scaffold(
                              appBar: AppBar(title: const Text('Congrats!')),
                              body: const Padding(
                                padding: EdgeInsets.all(20.0),
                                child: Text(
                                  "You've succesfully applied to an event. "
                                  "Now, you can check the event in your profil page",
                                  style: TextStyle(fontSize: 16),
                                ),
                              ),
                            );
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
