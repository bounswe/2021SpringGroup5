import 'package:flutter/material.dart';
import 'package:ludo_app/components/text_field_component.dart';
import 'package:ludo_app/constants.dart';

class RoundedInputField extends StatefulWidget {
  final String hintText;
  final IconData? icon;
  final ValueChanged<String> onChanged;
  final controller;

  const RoundedInputField({
    Key? key,
    required this.hintText,
    this.icon = Icons.person,
    required this.onChanged,
    this.controller,
  }) : super(key: key);

  @override
  State<RoundedInputField> createState() => _RoundedInputFieldState();
}

class _RoundedInputFieldState extends State<RoundedInputField> {
  // Create a text controller and use it to retrieve the current value
  // of the TextField.

  @override
  Widget build(BuildContext context) {
    return TextFieldContainer(
      child: TextField(
        controller: widget.controller,
        onChanged: widget.onChanged,
        decoration: InputDecoration(
            icon: Icon(widget.icon, color: kPrimaryColor),
            hintText: widget.hintText,
            border: InputBorder.none),
      ),
    );
  }
}