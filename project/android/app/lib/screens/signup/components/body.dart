import 'package:flutter/material.dart';
import 'package:ludo_app/components/check_registered_account.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/screens/login/login_screen.dart';
import 'package:ludo_app/screens/signup/components/background.dart';
import 'package:ludo_app/screens/user_create/user_create_screen.dart';

class Body extends StatelessWidget {

  final nameController = TextEditingController();
  final surnameController = TextEditingController();
  final emailController = TextEditingController();

  Body({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              "SIGN UP",
              style: TextStyle(fontWeight: FontWeight.normal, fontSize: 15.5),
            ),
            SizedBox(height: size.height * 0.02),
            Image.asset(
              "assets/images/ludo_logo.png",
              height: size.height * 0.30,
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(
              hintText: "Name",
              onChanged: (value) {},
              controller: nameController,
            ),
            RoundedInputField(
              hintText: "Surname",
              onChanged: (value) {},
              controller: surnameController,
            ),
            RoundedInputField(
              hintText: "Your Email",
              icon: Icons.alternate_email,
              onChanged: (value) {},
              controller: emailController,
            ),
            RoundedButton(
                text: "SIGN UP",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return UserCreateScreen(
                            name: nameController.text,
                            surname: surnameController.text,
                            email: emailController.text);
                      },
                    ),
                  );
                }),
            SizedBox(height: size.height * 0.02),
            CheckRegisteredAccount(
              login: false,
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return const LoginScreen();
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
