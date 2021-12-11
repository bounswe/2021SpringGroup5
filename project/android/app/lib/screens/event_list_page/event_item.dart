import 'package:flutter/material.dart';
import 'package:ludo_app/components/event.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';

class EventItem extends StatelessWidget {
  final Event event;

  EventItem(this.event);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 200,
      padding: EdgeInsets.all(15),
      decoration: BoxDecoration(
        image: DecorationImage(
            image: AssetImage('assets/images/basketball_event.png'),
            fit: BoxFit.cover),
        borderRadius: BorderRadius.circular(30),
        color: Colors.white,
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Row(
            //mainAxisAlignment: MainAxisAlignment.spaceBetween,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Container(
                    child: Text(
                      'Event.date',
                      style: TextStyle(
                          fontSize: 12,
                          color: Colors.black,
                          decoration: TextDecoration.none),
                    ),
                    width: MediaQuery.of(context).size.width * 0.13,
                    height: MediaQuery.of(context).size.width * 0.1,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Colors.grey.withOpacity(0.5),
                    ),
                  ),
                  SizedBox(
                    width: MediaQuery.of(context).size.width * 0.34,
                    height: MediaQuery.of(context).size.width * 0.1,
                  ),
                  Container(
                    child: Text(
                      'Event.isFullOrAvailable',
                      style: TextStyle(
                          fontSize: 12,
                          color: Colors.black,
                          decoration: TextDecoration.none),
                    ),
                    width: MediaQuery.of(context).size.width * 0.38,
                    height: MediaQuery.of(context).size.width * 0.1,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(10),
                      color: Colors.grey.withOpacity(0.5),
                    ),
                  ),
                ],
              ),
            ],
          ),
          SizedBox(
            height: MediaQuery.of(context).size.width * 0.145,
          ),
          Row(
            children: [
              Container(
                padding: EdgeInsets.all(1),
                child: Text(
                  '3v3 tek pota basketbol',
                  style: TextStyle(
                      fontSize: 15,
                      color: Colors.white,
                      decoration: TextDecoration.none),
                ),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(5),
                  color: Colors.black.withOpacity(0.5),
                ),
              ),
            ],
          ),
          SizedBox(
            height: MediaQuery.of(context).size.width * 0.01,
          ),
          Row(
            children: [
              Container(
                padding: EdgeInsets.all(1),
                child: Text(
                  'Ucaksavar stadı',
                  style: TextStyle(
                      fontSize: 15,
                      color: Colors.white,
                      decoration: TextDecoration.none),
                ),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(5),
                  color: Colors.black.withOpacity(0.5),
                ),
              ),
            ],
          ),
          SizedBox(
            height: MediaQuery.of(context).size.width * 0.01,
          ),
          Row(
            children: [
              Container(
                padding: EdgeInsets.all(1),
                child: Text(
                  '09:00',
                  style: TextStyle(
                      fontSize: 15,
                      color: Colors.white,
                      decoration: TextDecoration.none),
                ),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(5),
                  color: Colors.black.withOpacity(0.5),
                ),
              ),

            ],
          ),
        ],
      ),
    );
  }
}
