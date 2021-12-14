import 'package:flutter/material.dart';

class PopupEventDetails extends StatelessWidget {
  const PopupEventDetails({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25),
      child: Material(
        color: Colors.white.withOpacity(0.95),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(15),
            child: Column(children: [
              Row(
                children: const [
                  Text(
                    "3v3 Tek Pota Besketbol Maçı: event.name",
                    style: TextStyle(fontSize: 16),
                  )
                ],
              ),
              SizedBox(
                height: MediaQuery.of(context).size.height * 0.025,
              ),
              Row(
                children: const [
                  Text(
                    "Uçaksavar Stadı: event.location",
                    style: TextStyle(fontSize: 16),
                  )
                ],
              ),
              SizedBox(
                height: MediaQuery.of(context).size.height * 0.025,
              ),
              Row(
                children: const [
                  Text(
                    "18:00",
                    style: TextStyle(fontSize: 16),
                  )
                ],
              ),
              SizedBox(
                height: MediaQuery.of(context).size.height * 0.025,
              ),
              Row(
                children: const [Text(
                    "Participants: event.participants",
                    style: TextStyle(fontSize: 16),
                  )
                ],
              ),
              SizedBox(
                height: MediaQuery.of(context).size.height * 0.025,
              ),
              Row(
                children: const [Text(
                    "Organizator: event.organizator",
                    style: TextStyle(fontSize: 16),
                  )
                ],
              ),
            ]),
          ),
        ),
      ),
    ));
  }
}
