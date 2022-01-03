import 'package:flutter/material.dart';
import 'package:ludo_app/components/change_password.dart';
import 'package:ludo_app/components/check_registered_account.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/components/rounded_password_field.dart';
import 'package:ludo_app/screens/change_password/change_password_screen.dart';
import 'package:ludo_app/screens/login/components/background.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';
import 'package:ludo_app/screens/signup/signup_screen.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:ludo_app/globals.dart' as globals;

class Body extends StatelessWidget {
  final String? message;

  Body({Key? key, this.message}) : super(key: key);

  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    if(message != null) Future.delayed(Duration.zero, () => showMailDialog(context, message??''));
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              "LOGIN",
              style: TextStyle(fontWeight: FontWeight.normal, fontSize: 15.5),
            ),
            SizedBox(height: size.height * 0.02),
            Image.asset(
              "assets/images/ludo_logo.png",
              height: size.height * 0.35,
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(
              hintText: "Username",
              onChanged: (value) {},
              controller: usernameController,
            ),
            RoundedPasswordField(
              onChanged: (value) {},
              controller: passwordController,
            ),
            RoundedButton(
              text: "LOGIN",
              press: () {
                showAlertDialog(context, usernameController.text, passwordController.text);
              },
            ),
            SizedBox(height: size.height * 0.02),
            ChangePassword(
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return ChangePasswordScreen();
                    },
                  ),
                );
              },
            ),
            SizedBox(height: size.height * 0.015),
            CheckRegisteredAccount(
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
            ),
          ],
        ),
      ),
    );
  }
}

showMailDialog(BuildContext context, String message) {
  if (message == "") {
    return;
  }
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        content: Text(message),
      );
    },
  );
}

showAlertDialog(BuildContext context, String username, String password) async {
  Future<String>? _futureResponse;
  FutureBuilder<String> buildFutureBuilder() {
    return FutureBuilder<String>(
      future: _futureResponse,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text(snapshot.data!);
        } else if (snapshot.hasError) {
          return Text('${snapshot.error}');
        }

        return const CircularProgressIndicator();
      },
    );
  }

  _futureResponse = login(context, username, password);
  // late var futureRegister = fetchRegister();
  // print(futureRegister);
  // set up the AlertDialog
  AlertDialog alert = AlertDialog(
    content: buildFutureBuilder(),
  );

  // show the dialog
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return alert;
    },
  );

}

Future<String> login(BuildContext context, String username, String password) async {
  final response = await http.post(
    Uri.parse('http://3.122.41.188:8000/login'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode({
      "actor":
      {
        "type": "Person",
        "username": username,
        "password": password
      }
    }),
  );

  Map bodyMap = json.decode(response.body);
  print(bodyMap);

  if (bodyMap.containsKey("token")) {

    //RegExp exp = RegExp(r'csrftoken=(\w+);');
    //String csrf = exp.firstMatch(response.headers['set-cookie']!)!.group(1)!;
    RegExp exp = RegExp(r'sessionid=(\w+);');
    String sessionid = exp.firstMatch(response.headers['set-cookie']!)!.group(1)!;
    globals.csrftoken = bodyMap['csrf'];
    globals.refresh = bodyMap['token']['refresh'];
    globals.access = bodyMap['token']['access'];
    globals.sessionid = sessionid;

    final response2 = await http.get(
      Uri.parse('http://3.122.41.188:8000/me'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': globals.access,
        //'Cookie': 'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}'
      },
    );

    Map userInfo = json.decode(response2.body);
    print(userInfo);

    if(userInfo.containsKey('name')) {
      globals.isLoggedIn = true;
      globals.name = userInfo['name'];
      globals.surname = userInfo['surname'];
      globals.username = userInfo['username'];
      globals.userid = userInfo['Id'];
      globals.email = userInfo['mail'];
    } else {
      throw Exception(response2.body);
    }

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) {
          return MainEventScreen(willFetchAllEvents: true);
        },
      ),
    );

    //return response.body;
    return "";
  } else {
    throw Exception(bodyMap['errormessage']);
  }
}
