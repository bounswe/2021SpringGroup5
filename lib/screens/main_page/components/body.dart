import 'package:flutter/material.dart';
import 'package:ludo_app/screens/main_page/components/background.dart';

class Body extends StatelessWidget {
  const Body({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Background(
      child: Column(
        children: <Widget>[
          SizedBox(
            height: 50,
          ),
          Text("You can see the events below.")
        ],
      ),
    );
  }
}
