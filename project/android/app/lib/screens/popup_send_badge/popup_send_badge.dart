import 'package:flutter/material.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';

class PopupSendBadge extends StatefulWidget {
  const PopupSendBadge({Key? key}) : super(key: key);

  @override
  State<PopupSendBadge> createState() => _PopupSendBadgeState();
}

class _PopupSendBadgeState extends State<PopupSendBadge> {
  int? dropdown_value;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 25),
        child: Material(
          color: Colors.white.withOpacity(0.95),
          shape:
          RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(15),
              child: Column(
                children: [
                  Row(
                    children: const [
                      Text(
                        "Send this badge to a friend:",
                        style: TextStyle(fontSize: 16),
                      )
                    ],
                  ),
                  SizedBox(
                    height: MediaQuery.of(context).size.height * 0.025,
                  ),
                  Row(children: [
                    DropdownButton(
                      value: dropdown_value,
                      icon: const Icon(Icons.keyboard_arrow_down),
                      items: const [
                        DropdownMenuItem(child: Text("Player 1"), value: 1,),
                        DropdownMenuItem(child: Text("Player 2"), value: 2,),
                        DropdownMenuItem(child: Text("Player 3"), value: 3,),
                        DropdownMenuItem(child: Text("Player 4"), value: 4,),
                        DropdownMenuItem(child: Text("Player 5"), value: 5,),
                      ],
                      onChanged: (int? newValue){
                        setState(() {
                          dropdown_value = newValue!;
                        });
                      },
                      hint: Text("Select a number"),
                    ),
                  ]),
                  ElevatedButton(
                    onPressed: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) {
                            return const MainEventScreen();
                          },
                        ),
                      );
                    },
                    child: const Text(
                      "SEND",
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}