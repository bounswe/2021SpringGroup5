import 'package:flutter/material.dart';
import 'package:ludo_app/components/text_field_component.dart';
import 'package:ludo_app/constants.dart';

class RoundedInputField extends StatelessWidget {
  final String hintText;
  final IconData? icon;
  final ValueChanged<String> onChanged;
  const RoundedInputField({
    Key? key, required this.hintText, this.icon = Icons.person, required this.onChanged,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFieldContainer(
      child: TextField(
        onChanged: onChanged,
        decoration: InputDecoration(
            icon: Icon(icon, color: kPrimaryColor),
            hintText: hintText,
            border: InputBorder.none),
      ),
    );
  }
}
