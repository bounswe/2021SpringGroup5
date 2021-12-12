import 'package:flutter/material.dart';
import 'package:ludo_app/screens/fav_sports/components/body.dart';

class FavSportsScreen extends StatelessWidget {
  final String name;
  final String surname;
  final String email;
  final String username;
  final String pw1;
  final String pw2;
  final favSports;

  const FavSportsScreen({
    Key? key,
    required this.name,
    required this.surname,
    required this.email,
    required this.username,
    required this.pw1,
    required this.pw2,
    this.favSports,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Body(
            name: this.name,
            surname: this.surname,
            email: this.email,
            username: this.username,
            pw1: this.pw1,
            pw2: this.pw2));
  }
}
