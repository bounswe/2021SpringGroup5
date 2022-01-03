import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/components/rounded_password_field.dart';
import 'package:ludo_app/screens/user_create/components/background.dart';
import 'package:ludo_app/screens/fav_sports/fav_sports_screen.dart';

class Body extends StatelessWidget {
  final String name;
  final String surname;
  final String email;

  final usernameController = TextEditingController();
  final pw1Controller = TextEditingController();
  final pw2Controller = TextEditingController();

  Body(
      {Key? key,
      required this.name,
      required this.surname,
      required this.email})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              "Set your username and password",
              style: const TextStyle(
                  fontWeight: FontWeight.normal, fontSize: 15.5),
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(
              hintText: "Username",
              onChanged: (value) {},
              controller: usernameController,
            ),
            RoundedPasswordField(
              onChanged: (value) {},
              controller: pw1Controller,
            ),
            RoundedPasswordField(
              hintText: "Repeat password",
              onChanged: (value) {},
              controller: pw2Controller,
            ),
            //RoundedPasswordField(onChanged: (value) {}),
            RoundedButton(
                text: "NEXT",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return FavSportsScreen(
                            name: name,
                            surname: surname,
                            email: email,
                            username: usernameController.text,
                            pw1: pw1Controller.text,
                            pw2: pw2Controller.text);
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
