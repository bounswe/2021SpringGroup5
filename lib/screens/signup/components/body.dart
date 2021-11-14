import 'package:flutter/material.dart';
import 'package:ludo_app/components/check_registered_account.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/screens/login/login_screen.dart';
import 'package:ludo_app/screens/signup/components/background.dart';
import 'package:ludo_app/screens/email_confirm/email_confirm_screen.dart';

class Body extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              "SIGN UP",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: size.height * 0.03),
            Image.asset(
              "assets/images/ludo_logo.png",
              height: size.height * 0.35,
            ),
            RoundedInputField(hintText: "Name", onChanged: (value) {}),
            RoundedInputField(hintText: "Surname", onChanged: (value) {}),
            RoundedInputField(hintText: "Your Email", icon: Icons.alternate_email, onChanged: (value) {}),
            //RoundedPasswordField(onChanged: (value) {}),
            RoundedButton(text: "SIGN UP", press: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return EmailConfirmScreen();
                  },
                ),
              );
            }),
            SizedBox(height: size.height * 0.03),
            CheckRegisteredAccount(
              login: false,
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return LoginScreen();
                    },
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
