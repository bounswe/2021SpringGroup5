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
                    "Frizbi Oynayacak Arkadaş aranıyor!",
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
                    "Boğaziçi Üniversitesi Güney Çimler",
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
                    "Date&Time: 2021-12-17 15:00",
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
                    "Participants: ali,veli and 4 more",
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
                    "Organizator: kmlcgn",
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
