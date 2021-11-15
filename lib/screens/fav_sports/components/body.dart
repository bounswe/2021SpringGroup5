import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/constants.dart';
import 'package:ludo_app/screens/fav_sports/components/background.dart';
import 'package:ludo_app/screens/fav_sports/fav_sports_screen.dart';
import 'package:ludo_app/screens/main_page/main_screen.dart';

class Body extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              "Please enter your favourite\nsport and skill level below",
              textAlign: TextAlign.center,
              style: TextStyle(fontWeight: FontWeight.normal, fontSize: 15.5),
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(
              hintText: "Favourite sport",
              icon: Icons.directions_walk,
              onChanged: (value) {},
            ),
            RoundedInputField(
              hintText: "Skill level",
              icon: Icons.double_arrow,
              onChanged: (value) {},
            ),
            RoundedButton(
                text: "ADD MORE INTEREST",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return FavSportsScreen();
                      },
                    ),
                  );
                }),
            RoundedButton(
                text: "COMPLETE SIGN UP",
                textColor: Colors.black,
                color: kPrimaryLightColor,
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return MainScreen();
                      },
                    ),
                  );
                }),
            SizedBox(height: size.height * 0.03),
          ],
        ),
      ),
    );
  }
}
