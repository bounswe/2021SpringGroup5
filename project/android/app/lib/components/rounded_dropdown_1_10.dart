import 'package:flutter/material.dart';

class RoundedDropdownButton extends StatefulWidget {
  const RoundedDropdownButton({Key? key}) : super(key: key);

  @override
  _RoundedDropdownButtonState createState() => _RoundedDropdownButtonState();
}

class _RoundedDropdownButtonState extends State<RoundedDropdownButton> {
  int dropdown_value = 1;
  @override
  Widget build(BuildContext context) {
    return Container(
      child: DropdownButton(
        value: dropdown_value,
        icon: const Icon(Icons.keyboard_arrow_down),
        items: const [
          DropdownMenuItem(child: Text("1"), value: 1,),
          DropdownMenuItem(child: Text("2"), value: 2,),
          DropdownMenuItem(child: Text("3"), value: 3,),
          DropdownMenuItem(child: Text("4"), value: 4,),
          DropdownMenuItem(child: Text("5"), value: 5,),
          DropdownMenuItem(child: Text("6"), value: 6,),
          DropdownMenuItem(child: Text("7"), value: 7,),
          DropdownMenuItem(child: Text("8"), value: 8,),
          DropdownMenuItem(child: Text("9"), value: 9,),
          DropdownMenuItem(child: Text("10"), value: 10,),
        ],
        onChanged: (int? newValue){
          setState(() {
            dropdown_value = newValue!;
          });
        },
        hint: Text("Select a number"),
      ),
    );
  }
}

