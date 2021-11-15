import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/constants.dart';
import 'package:ludo_app/screens/login/login_screen.dart';
import 'package:ludo_app/screens/signup/signup_screen.dart';
import 'package:ludo_app/screens/welcome/components/background.dart';

class Body extends StatelessWidget {
  const Body({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery
        .of(context)
        .size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            DecoratedBox(
              decoration: BoxDecoration(
                border:Border.all(color:kPrimaryColor, width: 25),
                color: kPrimaryColor,
              ),
              child: Text(
                "  LUDO,  SOCIAL SPORT APP  ",
                style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                    fontStyle: FontStyle.italic,
                    color: Colors.white),
              ),
            ),
            SizedBox(height: size.height * 0.03),
            Image.asset(
              "assets/images/ludo_logo.png",
              height: size.height * 0.3,
            ),
            SizedBox(height: size.height * 0.05),
            RoundedButton(
              text: "LOGIN",

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
            ),
            RoundedButton(
              text: "SIGN UP",
              color: kPrimaryLightColor,
              textColor: Colors.black,
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return SignUpScreen();
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
