import 'package:flutter/material.dart';
import 'package:ludo_app/screens/login/components/body.dart';

class LoginScreen extends StatelessWidget {
  final String? message;

  const LoginScreen({Key? key, this.message}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Body(message:message));
  }
}
