import 'package:flutter/material.dart';
import 'package:ludo_app/components/event.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/popup_event_details/popup_event_details.dart';

class EventItem extends StatelessWidget {
  final Event event;

  EventItem(this.event);

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
        child: Container(
          height: 208,
          padding: EdgeInsets.all(15),
          decoration: BoxDecoration(
            image: DecorationImage(
                image: AssetImage('assets/images/basketball_event.png'),
                fit: BoxFit.cover),
            borderRadius: BorderRadius.circular(20),
            color: Colors.white,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Row(
                //mainAxisAlignment: MainAxisAlignment.spaceBetween,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      Container(
                        padding: EdgeInsets.all(3),
                        child: Text(
                          '3v3 Tek Pota Basket Maçı',
                          style: TextStyle(
                              fontSize: 17,
                              color: Colors.black,
                              decoration: TextDecoration.none),
                        ),
                        width: MediaQuery.of(context).size.width * 0.63,
                        height: MediaQuery.of(context).size.width * 0.070,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(10),
                          color: Colors.grey.withOpacity(0.5),
                        ),
                      ),
                      SizedBox(
                        width: MediaQuery.of(context).size.width * 0.08,
                      ),
                      FloatingActionButton(
                        onPressed: () {},
                        child: Text('JOIN'),
                      ),
                    ],
                  ),
                ],
              ),
              Row(
                children: [
                  Container(
                    padding: EdgeInsets.all(1),
                    child: Text(
                      'Basketball (event.type)',
                      style: TextStyle(
                          fontSize: 14,
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
                      'Ucaksavar (event.location)',
                      style: TextStyle(
                          fontSize: 14,
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
                      '17 May-09:00 (event.datetime)',
                      style: TextStyle(
                          fontSize: 14,
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
                height: MediaQuery.of(context).size.width * 0.02,
              ),
              Container(
                  decoration: BoxDecoration(
                      color: Colors.blue,
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: Colors.black)),
                  child: TextButton(
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
                      child: Text(
                        'MAP VIEW',
                        style: TextStyle(color: Colors.white),
                      ))),
            ],
          ),
        ),
        onTap: () {
          Navigator.of(context).push(PopupCardEffect(builder: (context) {
            return PopupEventDetails();
          }));
        });
  }
}
