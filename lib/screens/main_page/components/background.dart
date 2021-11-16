import 'package:flutter/material.dart';

class Background extends StatelessWidget {
  final Widget child;
  const Background({
    Key? key, required this.child,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;

    return Container(
      width: double.infinity,
      height: size.height,

      child: Padding(
        padding: const EdgeInsets.all(30.0),
        child: Stack(

          alignment: Alignment.topCenter,
          children: <Widget>[
            Positioned(
              child: Image.asset("assets/images/ludo_logo.png"),
              width: size.width * 0.15,
            ),
            child,
          ],
        ),
      ),
    );
  }
}
