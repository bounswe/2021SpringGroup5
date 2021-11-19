import 'package:flutter/material.dart';
import 'package:ludo_app/screens/email_confirm/components/body.dart';

class EmailConfirmScreen extends StatelessWidget {
  const EmailConfirmScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(body: Body());
  }
}
