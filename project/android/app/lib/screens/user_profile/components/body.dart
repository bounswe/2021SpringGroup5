import 'package:flutter/material.dart';
import 'package:ludo_app/components/popup_card_effect.dart';
import 'package:ludo_app/screens/popup_send_badge/popup_Send_badge.dart';
import 'package:ludo_app/screens/welcome/welcome_screen.dart';
import 'package:ludo_app/services/user_service.dart';

class ProfileScreen extends StatelessWidget {
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
                  Positioned(
                    child: Center(
                      child: Image.asset(
                        'assets/images/example-user.jpg',
                        width: width * 0.45,
                        fit: BoxFit.cover,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: height * 0.23,
                    child: LayoutBuilder(
                      builder: (context, constraints) {
                        return Stack(
                          children: [
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
                                      userInfo[0]["name"],
                                      style: const TextStyle(
                                        fontSize: 20,
                                      ),
                                    ),
                                    const SizedBox(
                                      height: 5,
                                    ),
                                    Positioned(
                                      child: Text(
                                        userInfo[0]["mail"],
                                        style: const TextStyle(
                                          fontSize: 14,
                                        ),
                                      ),
                                    ),
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
                                              'Followings',
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
                          const Positioned(
                              child: Text(
                            "My Badges",
                            style: TextStyle(fontSize: 17),
                          )),
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
                                    onTap: () {
                                      Navigator.of(context).push(
                                        PopupCardEffect(
                                          builder: (context) {
                                            return PopupSendBadge();
                                          },
                                        ),
                                      );
                                    },
                                    leading: Image(
                                      fit: BoxFit.cover,
                                      image: AssetImage(userInfo[0]['badges']
                                          [index]['image']),
                                    ),
                                    title: Text(
                                        userInfo[0]['badges'][index]["name"]),
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
                          const Positioned(
                              child: Text(
                            "Previously Joined Events",
                            style: TextStyle(fontSize: 17),
                          )),
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
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) {
                            return WelcomeScreen();
                          },
                        ),
                      );
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
