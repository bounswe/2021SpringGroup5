import 'package:flutter/material.dart';
import 'package:ludo_app/constants.dart';


class ChangePassword extends StatelessWidget {
  final VoidCallback? press;
  const ChangePassword({
    Key? key, this.press,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          "Forgot your password? ",
          style: TextStyle(color: kPrimaryColor),
        ),
        GestureDetector(
          onTap: press,
          child: Text(
            "Change Password",
            style: TextStyle(
                color: kPrimaryColor, fontWeight: FontWeight.bold),
          ),
        )
      ],
    );
  }
}
