import 'package:flutter/material.dart';
import 'package:ludo_app/screens/welcome/welcome_screen.dart';
import 'package:ludo_app/services/user_service.dart';
import 'package:ludo_app/globals.dart' as globals;
import 'package:http/http.dart' as http;
import 'dart:convert';

class ProfileScreen extends StatelessWidget {

  showAlertDialog(BuildContext context) async {
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

    _futureResponse = logout(context);
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

  Future<String> logout(BuildContext context) async {
    final response = await http.post(
      Uri.parse('http://3.122.41.188:8000/logout_user'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authentication': globals.access,
        'X-CSRFTOKEN': globals.csrftoken,
        'Cookie': 'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}'
      },
    );

    Map bodyMap = json.decode(response.body);
    print(bodyMap);
    print(response.statusCode);

    if (response.statusCode == 200 && bodyMap['has_error'] == false){
      globals.isLoggedIn = false;
      globals.name = "";
      globals.surname = "";
      globals.username = "";
      globals.userid = -1;
      globals.email = "";
      globals.access = "";
      globals.refresh = "";
      globals.csrftoken = "";
      globals.sessionid = "";

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) {
            return WelcomeScreen();
          },
        ),
      );

      return "";
    } else {
      throw Exception(bodyMap.toString());
    }


  }

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;

    return Stack(
      children: [
        Container(
          decoration: const BoxDecoration(
            color: Colors.blueGrey,
          ),
        ),
        Scaffold(
          backgroundColor: Colors.transparent,
          body: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 70),
              child: Column(
                children: [
                  const Text(
                    'Profile Info',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 25,
                    ),
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  Stack(children: [
                    Positioned(
                      child: Center(
                        child: Image.asset(
                          'assets/images/example-user.jpg',
                          width: width * 0.45,
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                  ],),
                  SizedBox(
                    height: height * 0.23,
                    child: LayoutBuilder(
                      builder: (context, constraints) {
                        return Stack(
                          children: [
                            Stack(children: [
                              Positioned(
                                bottom: 0,
                                left: 0,
                                right: 0,
                                top: 20,
                                child: Container(
                                  decoration: BoxDecoration(
                                    borderRadius: BorderRadius.circular(25),
                                    color: Colors.white,
                                  ),
                                  child: Column(
                                    children: [
                                      const SizedBox(
                                        height: 18,
                                      ),
                                      Text(
                                        globals.name + ' ' + globals.surname,
                                        style: const TextStyle(
                                          fontSize: 20,
                                        ),
                                      ),
                                      const SizedBox(
                                        height: 5,
                                      ),
                                      Stack(children: [
                                        Positioned(
                                          child: Text(
                                            globals.email,
                                            style: const TextStyle(
                                              fontSize: 14,
                                            ),
                                          ),
                                        ),
                                      ],),
                                      const SizedBox(
                                        height: 0.5,
                                      ),
                                      Row(
                                        mainAxisAlignment:
                                        MainAxisAlignment.center,
                                        children: [
                                          Column(
                                            children: const [
                                              Text(
                                                'Followers',
                                                style: TextStyle(
                                                  color: Colors.indigo,
                                                  fontSize: 20,
                                                ),
                                              ),
                                              Text(
                                                '120',
                                                style: TextStyle(
                                                  fontSize: 25,
                                                ),
                                              ),
                                            ],
                                          ),
                                          Padding(
                                            padding: const EdgeInsets.symmetric(
                                              horizontal: 24,
                                              vertical: 10,
                                            ),
                                            child: Container(
                                              height: height * 0.065,
                                              width: width * 0.0085,
                                              decoration: const BoxDecoration(
                                                color: Colors.indigo,
                                              ),
                                            ),
                                          ),
                                          Column(
                                            children: const [
                                              Text(
                                                'Following',
                                                style: TextStyle(
                                                  color: Colors.indigo,
                                                  fontSize: 20,
                                                ),
                                              ),
                                              Text(
                                                '100',
                                                style: TextStyle(
                                                  fontSize: 25,
                                                ),
                                              ),
                                            ],
                                          ),
                                        ],
                                      )
                                    ],
                                  ),
                                ),
                              ),
                            ],),
                          ],
                        );
                      },
                    ),
                  ),
                  const SizedBox(
                    height: 30,
                  ),
                  Container(
                    height: height * 0.5,
                    width: width,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(30),
                      color: Colors.white,
                    ),
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 15),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const SizedBox(
                            height: 10,
                          ),
                          Stack(children: const [
                            Positioned(
                                child: Text(
                                  "My Badges",
                                  style: TextStyle(fontSize: 17),
                                )),
                          ],),
                          Expanded(
                            child: ListView.builder(
                              itemCount: userInfo[0]["badges"].length,
                              itemBuilder: (context, index) => Card(
                                elevation: 5,
                                key: ValueKey([index][0]),
                                color: Colors.white,
                                margin:
                                    const EdgeInsets.symmetric(vertical: 10),
                                child: Padding(
                                  padding: const EdgeInsets.all(13.0),
                                  child: ListTile(
                                    onTap: () {},
                                    leading: Image(
                                      fit: BoxFit.cover,
                                      image: AssetImage(userInfo[0]['badges']
                                          [index]['image']),
                                    ),
                                    title: Text(userInfo[0]['badges'][index]["name"]),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 30,
                  ),
                  Container(
                    height: height * 0.5,
                    width: width,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(30),
                      color: Colors.white,
                    ),
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 15),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const SizedBox(
                            height: 10,
                          ),
                          Stack(children: const [
                            Positioned(
                              child: Text(
                                "Previously Joined Events",
                                style: TextStyle(fontSize: 17),
                              )),],
                          ),
                          Expanded(
                            child: ListView.builder(
                              itemCount: userInfo[0]["events"].length,
                              itemBuilder: (context, index) => Card(
                                elevation: 5,
                                key: ValueKey([index][0]),
                                color: Colors.white,
                                margin:
                                    const EdgeInsets.symmetric(vertical: 10),
                                child: Padding(
                                  padding: const EdgeInsets.all(13.0),
                                  child: ListTile(
                                    onTap: () {},
                                    leading: Image(
                                      fit: BoxFit.cover,
                                      image: AssetImage(userInfo[0]['events']
                                          [index]['image']),
                                    ),
                                    title: Text(
                                        userInfo[0]['events'][index]["name"]),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(
                    height: 15,
                  ),
                  ElevatedButton(
                    onPressed: () {
                      showAlertDialog(context);
                    },
                    child: const Text(
                      "Log-Out",
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            ),
          ),
        )
      ],
    );
  }
}
