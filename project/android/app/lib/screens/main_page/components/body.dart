import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/constants.dart';
import 'package:ludo_app/screens/event_list_page/event_list_screen.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen.dart';
import 'package:ludo_app/screens/main_page/components/background.dart';
import 'package:ludo_app/screens/welcome/welcome_screen.dart';

class Body extends StatelessWidget {
  const Body({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: Column(
        children: <Widget>[
          SizedBox(
            height: 70,
          ),
          Container(
            alignment: Alignment.center,
            child: Text(
              "Events that matched with your interests.",
              style: TextStyle(fontSize: 15.5),
            ),
          ),
          SizedBox(
            height: 40,
          ),
          Column(
            children: [
              Image.asset(
                "assets/images/squash-sport.jpg",
                height: size.height * 0.3,
              ),
              SizedBox(
                height: 15,
              ),
              Text("1v1 Squash Game near Etiler."),
              RoundedButton(
                text: "MAP",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return GoogleMapsScreen();
                      },
                    ),
                  );
                },
              ),
              RoundedButton(
                text: "EVENTS",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return EventListScreen();
                      },
                    ),
                  );
                },
              ),
              SizedBox(
                height: MediaQuery.of(context).size.width * 0.02,
              ),
              RoundedButton(
                color: kPrimaryLightColor,
                textColor: Colors.black,
                text: "LOGOUT",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return WelcomeScreen();
                      },
                    ),
                  );
                },
              ),
            ],
          )
        ],
      ),
    );
  }
}
