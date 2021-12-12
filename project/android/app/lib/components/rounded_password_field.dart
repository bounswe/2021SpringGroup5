import 'package:flutter/material.dart';
import 'package:ludo_app/components/text_field_component.dart';
import 'package:ludo_app/constants.dart';

class RoundedPasswordField extends StatefulWidget {
  final ValueChanged<String> onChanged;
  final String hintText;
  final controller;

  const RoundedPasswordField({
    Key? key,
    required this.onChanged,
    this.hintText = "Password",
    this.controller,
  }) : super(key: key);

  @override
  State<RoundedPasswordField> createState() => _RoundedPasswordFieldState();
}

class _RoundedPasswordFieldState extends State<RoundedPasswordField> {
  @override
  Widget build(BuildContext context) {
    return TextFieldContainer(
      child: TextField(
        obscureText: true,
        onChanged: widget.onChanged,
        decoration: InputDecoration(
          hintText: widget.hintText,
          icon: Icon(
            Icons.lock,
            color: kPrimaryColor,
          ),
          border: InputBorder.none,
        ),
        controller: widget.controller,
      ),
    );
  }
}
