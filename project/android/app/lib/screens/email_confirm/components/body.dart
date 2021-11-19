import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/screens/email_confirm/components/background.dart';
import 'package:ludo_app/screens/user_create/user_create_screen.dart';

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
              "Please enter the verification code\nsent to your email address",
              style: TextStyle(fontWeight: FontWeight.normal,fontSize: 15.5),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(hintText: "Verification Code", icon: null, onChanged: (value) {}),
            //RoundedPasswordField(onChanged: (value) {}),
            RoundedButton(text: "NEXT", press: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return UserCreateScreen();
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
