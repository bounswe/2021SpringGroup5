import 'package:flutter/material.dart';

class UploadImage extends StatefulWidget {
  const UploadImage({Key? key}) : super(key: key);

  @override
  _UploadImageState createState() => _UploadImageState();
}

class _UploadImageState extends State<UploadImage> {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            RaisedButton(
              color: Colors.greenAccent,
              onPressed: (){},
              child: Text('Choose Image'),
            ),
            SizedBox(width: 8.0),
            RaisedButton(
              color: Colors.greenAccent,
              onPressed: (){},
              child: Text('Upload Image'),
            )
          ],
        ),
      ],
    );
  }
}
