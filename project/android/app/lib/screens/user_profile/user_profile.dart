import 'package:flutter/material.dart';
import 'package:ludo_app/screens/user_profile/components/body.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(body: ProfileScreen());
  }
}
