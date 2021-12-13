import 'package:flutter/material.dart';
import 'package:ludo_app/components/rounded_button.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/screens/fav_sports/components/background.dart';
import 'package:ludo_app/screens/login/login_screen.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class Body extends StatefulWidget {
  final String name;
  final String surname;
  final String email;
  final String username;
  final String pw1;
  final String pw2;

  Body({
    Key? key,
    required this.name,
    required this.surname,
    required this.email,
    required this.username,
    required this.pw1,
    required this.pw2,
  }) : super(key: key);

  @override
  State<Body> createState() => _BodyState();
}

class _BodyState extends State<Body> {

  final favSportController1 = TextEditingController();
  final levelController1 = TextEditingController();
  final favSportController2 = TextEditingController();
  final levelController2 = TextEditingController();

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
            const Text(
              "Please enter your favourite\nsport and skill level below\n",
              //json.encode(widget.favSports),
              textAlign: TextAlign.center,
              style: TextStyle(fontWeight: FontWeight.normal, fontSize: 15.5),
            ),
            SizedBox(height: size.height * 0.02),
            RoundedInputField(
              hintText: "1. Favourite sport",
              icon: Icons.directions_walk,
              onChanged: (value) {},
              controller: favSportController1,
            ),
            /*Container(
              margin: EdgeInsets.symmetric(vertical: 10),
              width: size.width * 0.8,
              child: ClipRRect(
                borderRadius: BorderRadius.circular(29),
                child: DropdownButton<String>(
                  dropdownColor: kPrimaryLightColor,
                  hint: Text('Skill Level'),
                  borderRadius: BorderRadius.circular(20),
                  items: <String>['Beginner', 'Intermediate', 'Advanced']
                      .map((String value) {
                    return DropdownMenuItem<String>(
                      value: value,
                      child: Text(value),
                    );
                  }).toList(),
                  onChanged: (_) {},
                ),
              ),
            ),*/
            RoundedInputField(
              hintText: "Skill level",
              icon: Icons.double_arrow,
              onChanged: (value) {},
              controller: levelController1,
            ),
            /*RoundedButton(
                text: "ADD MORE INTEREST",
                press: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) {
                        return FavSportsScreen(
                          name: widget.name,
                          surname: widget.surname,
                          email: widget.email,
                          username: widget.username,
                          pw1: widget.pw1,
                          pw2: widget.pw2,
                          favSports: {
                            "name": favSportController.text,
                            "level": levelController.text,
                          },
                        );
                      },
                    ),
                  );
                }),*/
            SizedBox(height: 20),
            RoundedInputField(
              hintText: "2. Favourite sport",
              icon: Icons.directions_walk,
              onChanged: (value) {},
              controller: favSportController2,
            ),
            RoundedInputField(
              hintText: "Skill level",
              icon: Icons.double_arrow,
              onChanged: (value) {},
              controller: levelController2,
            ),
            SizedBox(height: 30),
            RoundedButton(
                text: "COMPLETE SIGN UP",
                //textColor: Colors.black,
                //color: kPrimaryLightColor,
                press: () {
                  showAlertDialog(
                      context,
                      widget.name,
                      widget.surname,
                      widget.email,
                      widget.username,
                      widget.pw1,
                      widget.pw2,
                      favSportController1.text,
                      levelController1.text,
                      favSportController2.text,
                      levelController2.text);
                }),
            SizedBox(height: size.height * 0.03),
          ],
        ),
      ),
    );
  }
}

showAlertDialog(BuildContext context, name, surname, email, username, pw1, pw2,
    fs1, lvl1, fs2, lvl2) async {
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

  var user = {
    "actor": {
      "type": "Person",
      "name": name,
      "surname": surname,
      "username": username,
      "email": email,
      "password1": pw1,
      "password2": pw2,
    },
    "items": [
      {
        "name": fs1,
        "level": lvl1,
      },
      {
        "name": fs2,
        "level": lvl2,
      }
    ],
  };
  _futureResponse = createUser(user, context);
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

Future fetchRegister() async {
  final response = await http
      .get(Uri.parse('https://jsonplaceholder.typicode.com/albums/1'));

  if (response.statusCode == 200) {
    // If the server did return a 200 OK response,
    // then parse the JSON.
    return response.body;
  } else {
    // If the server did not return a 200 OK response,
    // then throw an exception.
    throw Exception('Failed to load album');
  }
}

Future<String> createUser(user,BuildContext context) async {
  final response = await http.post(
    Uri.parse('http://3.122.41.188:8000/register'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(user),
  );

  if (response.statusCode == 201) {

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) {
          return const LoginScreen(message:"Please check your email to verify your account.");
        },
      ),
    );

    //return response.body;
    return "";
  } else {
    // If the server did not return a 201 CREATED response,
    // then throw an exception.
    throw Exception(json.decode(response.body)['errormessage']);
  }
}


