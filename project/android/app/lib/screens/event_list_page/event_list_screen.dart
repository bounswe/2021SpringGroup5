import 'package:flutter/material.dart';
import 'package:ludo_app/components/event.dart';
import 'package:ludo_app/screens/event_list_page/event_item.dart';

//in this page the events will be displayed from top to bottom, if tap on a event card it will open the
// event card details page

class EventListScreen extends StatefulWidget {
  @override
  _EventListScreenState createState() => _EventListScreenState();
}

class _EventListScreenState extends State<EventListScreen> {
  final eventList = Event.generateEvent();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          backwardsCompatibility: true,
          title: Container(
            width: MediaQuery.of(context).size.width,
            height: MediaQuery.of(context).size.height * 0.050,
            color: Colors.white,
            child: Center(
              child: TextField(
                decoration: InputDecoration(
                  hintText: 'Search for an event',
                  prefixIcon: Icon(Icons.search),
                ),
              ),
            ),
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.only(top: 8),
          child: ListView.separated(
              padding: EdgeInsets.symmetric(horizontal: 15),
              scrollDirection: Axis.vertical,
              itemBuilder: (context, index) => EventItem(eventList[index]),
              separatorBuilder: (_, index) => SizedBox(
                    height: 20,
                  ),
              itemCount: eventList.length),
        ));
  }
}
