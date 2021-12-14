import 'package:flutter/material.dart';
import 'package:ludo_app/screens/user_create/components/body.dart';

class UserCreateScreen extends StatelessWidget {
  final String name;
  final String surname;
  final String email;

  const UserCreateScreen(
      {Key? key,
      required this.name,
      required this.surname,
      required this.email})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Body(
        name: this.name, surname: this.surname, email: this.email));
  }
}
