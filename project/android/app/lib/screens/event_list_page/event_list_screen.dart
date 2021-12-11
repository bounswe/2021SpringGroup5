import 'package:flutter/material.dart';
import 'package:ludo_app/components/event.dart';
import 'package:ludo_app/screens/event_list_page/event_item.dart';

//in this page the events will be displayed from top to bottom, if tap on a event card it will open the
// event card details page

class EventListScreen extends StatelessWidget {
  final eventList = Event.generateEvent();

  @override
  Widget build(BuildContext context) {
    return Container(
        decoration:
            BoxDecoration(color: Colors.lightGreenAccent.withOpacity(0.6)),
        child: ListView.separated(
            padding: EdgeInsets.symmetric(horizontal: 15),
            scrollDirection: Axis.vertical,
            itemBuilder: (context, index) => EventItem(eventList[index]),
            separatorBuilder: (_, index) => SizedBox(
                  height: 20,
                ),
            itemCount: eventList.length));
  }
}
