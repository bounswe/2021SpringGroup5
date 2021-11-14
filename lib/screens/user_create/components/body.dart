import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/components/rounded_password_field.dart';
import 'package:ludo_app/screens/user_create/components/background.dart';
import 'package:ludo_app/screens/fav_sports/fav_sports_screen.dart';

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
              "Set your username and password",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: size.height * 0.03),
            RoundedInputField(
              hintText: "Username",
              onChanged: (value) {},
            ),
            RoundedPasswordField(
              onChanged: (value) {},
            ),
            RoundedPasswordField(
              hintText: "Repeat password",
              onChanged: (value) {},
            ),
            //RoundedPasswordField(onChanged: (value) {}),
            RoundedButton(text: "NEXT", press: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return FavSportsScreen();
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
