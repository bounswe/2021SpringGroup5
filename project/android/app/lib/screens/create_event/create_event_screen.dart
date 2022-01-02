import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:ludo_app/screens/google_maps/google_maps_screen_no_radius.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';
import 'dart:io';
import 'package:ludo_app/globals.dart' as globals;
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart' as intl;

class CreateEventScreen extends StatefulWidget {
  const CreateEventScreen({Key? key}) : super(key: key);

  @override
  _CreateEventScreenState createState() => _CreateEventScreenState();
}

class _CreateEventScreenState extends State<CreateEventScreen> {
  bool _beginnerFlag = true;
  bool _averageFlag = true;
  bool _skilledFlag = true;
  bool _expertFlag = true;
  List<double> mapCallback = [];
  late ImagePicker imagePicker;
  var _image;
  DateTime selectedDateTime = DateTime.now();

  final eventNameController = TextEditingController();
  final eventDescriptionController = TextEditingController();
  final sportNameController = TextEditingController();
  final participantLimitController = TextEditingController();
  final spectatorLimitController = TextEditingController();
  final rulesController = TextEditingController();
  final equipmentRequirementController = TextEditingController();
  final contactInfoController = TextEditingController();

  _updateLocation(List<double> maps) {
    setState(() {
      mapCallback = maps;
    });
  }

  showAlertDialog(BuildContext context) async {
    Future<String>? _futureResponse;
    FutureBuilder<String> buildFutureBuilder() {
      return FutureBuilder<String>(
        future: _futureResponse,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return Text(snapshot.data!);
          } else if (snapshot.hasError) {
            return Text('${snapshot.error}');
          }

          return const CircularProgressIndicator();
        },
      );
    }

    _futureResponse = createEvent(context);
    // late var futureRegister = fetchRegister();
    // print(futureRegister);
    // set up the AlertDialog
    AlertDialog alert = AlertDialog(
      content: buildFutureBuilder(),
    );

    // show the dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }

  Future<String> createEvent(BuildContext context) async {
    String skillLevel = "beginner";
    if (_beginnerFlag == false) {
      skillLevel = "beginner";
    } else if (_averageFlag == false) {
      skillLevel = "average";
    } else if (_skilledFlag == false) {
      skillLevel = "skilled";
    } else if (_expertFlag == false) {
      skillLevel = "expert";
    }
    var params = {
      "@context": "https://www.w3.org/ns/activitystreams",
      "summary": "${globals.name} is creating an event post",
      "type": "Create",
      "actor": {
        "type": "Person",
        "name": globals.name,
        "surname": globals.surname,
        "username": globals.username,
        "Id": globals.userid,
      },
      "object": {
        "type": "EventPost",
        "owner_id": globals.userid,
        "post_name": eventNameController.text,
        "sport_category": sportNameController.text,
        "longitude": mapCallback[0],
        "latitude": mapCallback[1],
        "description": eventDescriptionController.text,
        "pathToEventImage": null,
        "date_time":
            intl.DateFormat("yyyy-MM-dd hh:mm").format(selectedDateTime),
        "participant_limit": int.parse(participantLimitController.text),
        "spectator_limit": int.parse(spectatorLimitController.text),
        "rule": rulesController.text,
        "equipment_requirement": equipmentRequirementController.text,
        "location_requirement": "",
        "contact_info": contactInfoController.text,
        "skill_requirement": skillLevel,
        "repeating_frequency": 1,
        "badges": [
          {
            "id": 1,
            "name": "friendly",
            "description": "You are a friendly player",
            "wikiId": ""
          }
        ]
      }
    };

    var uri = Uri.parse('http://3.122.41.188:8000/post/create_event_post/');
    var request = http.MultipartRequest('POST', uri);
    request.headers.addAll(
      <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authentication': globals.access,
        'X-CSRFTOKEN': globals.csrftoken,
        'Cookie':
            'csrftoken=${globals.csrftoken}; sessionid=${globals.sessionid}'
      },
    );
    request.files.add(await http.MultipartFile.fromPath('image', _image));
    request.fields['json'] = jsonEncode(params);
    var response = await request.send();

    print(response.statusCode);
    print(response.stream.toString());
    if (response.statusCode == 201) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) {
            return MainEventScreen(willFetchAllEvents: true);
          },
        ),
      );
      return response.toString();
    } else {
      throw Exception(response.stream.toString());
    }
  }

  void _showPicker(context) {
    showModalBottomSheet(
        context: context,
        builder: (BuildContext bc) {
          return SafeArea(
            child: Container(
              child: Wrap(
                children: <Widget>[
                  ListTile(
                      leading: const Icon(Icons.photo_library),
                      title: const Text('Photo Library'),
                      onTap: () {
                        _imgFromGallery();
                        Navigator.of(context).pop();
                      }),
                  ListTile(
                    leading: const Icon(Icons.photo_camera),
                    title: const Text('Camera'),
                    onTap: () {
                      _imgFromCamera();
                      Navigator.of(context).pop();
                    },
                  ),
                ],
              ),
            ),
          );
        });
  }

  _imgFromCamera() async {
    final XFile? image = await imagePicker.pickImage(
        source: ImageSource.camera,
        imageQuality: 50,
        preferredCameraDevice: CameraDevice.rear);
    setState(() {
      _image = image!.path;
    });
  }

  _imgFromGallery() async {
    final XFile? image = await imagePicker.pickImage(
        source: ImageSource.gallery, imageQuality: 50);
    setState(() {
      _image = image!.path;
    });
  }

  @override
  void initState() {
    super.initState();
    imagePicker = ImagePicker();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Create Your Event"),
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(5.0),
          child: Column(
            children: [
              const SizedBox(height: 15, width: 10),
              Center(
                child: GestureDetector(
                  onTap: () {
                    _showPicker(context);
                  },
                  child: Container(
                    width: 320,
                    height: 180,
                    decoration: BoxDecoration(color: Colors.white),
                    child: _image != null
                        ? Image.file(
                            File(_image),
                            width: 280.0,
                            height: 210.0,
                            fit: BoxFit.fitHeight,
                          )
                        : Container(
                            decoration: BoxDecoration(color: Colors.grey[100]),
                            width: 280,
                            height: 210,
                            child: Icon(
                              Icons.camera_alt,
                              color: Colors.grey[800],
                            ),
                          ),
                  ),
                ),
              ),
              const SizedBox(height: 10, width: 10),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Type Your Event Name",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                      decoration: InputDecoration(
                      hintText: ('Type here...'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.text,
                    controller: eventNameController,
                  )
              ),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Type Your Event Description",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),

              Container(
                  child: TextFormField(
                    decoration: InputDecoration(
                      hintText: ('Type here...'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.text,
                    controller: eventDescriptionController,
                  )
              ),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Enter Sport Name",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),

              Container(
                  child: TextFormField(
                    decoration: InputDecoration(
                      hintText: ('e.g. tennis'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.text,
                    controller: sportNameController,
                  )
              ),

              Padding(
                padding: const EdgeInsets.only(
                    left: 8.0, right: 8.0, top: 6.0, bottom: 8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Select the Skill Level Requirement",
                            style: TextStyle(fontSize: 16))),
                    //type
                  ],
                ),
              ),
              const SizedBox(height: 1, width: 10),

              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(10)),
                child: Padding(
                  padding: const EdgeInsets.only(
                      left: 6.0, right: 6.0, top: 3.0, bottom: 3.0),
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _beginnerFlag = !_beginnerFlag),
                          child: Text(_beginnerFlag ? 'BEGINNER' : 'BEGINNER'),
                          style: ElevatedButton.styleFrom(
                            primary: _beginnerFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _averageFlag = !_averageFlag),
                          child: Text(_averageFlag ? 'AVERAGE' : 'AVERAGE'),
                          style: ElevatedButton.styleFrom(
                            primary: _averageFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _skilledFlag = !_skilledFlag),
                          child: Text(_skilledFlag ? 'SKILLED' : 'SKILLED'),
                          style: ElevatedButton.styleFrom(
                            primary: _skilledFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                        const SizedBox(
                          width: 1,
                          height: 1,
                        ),
                        ElevatedButton(
                          onPressed: () =>
                              setState(() => _expertFlag = !_expertFlag),
                          child: Text(_expertFlag ? 'EXPERT' : 'EXPERT'),
                          style: ElevatedButton.styleFrom(
                            primary: _expertFlag
                                ? Colors.grey
                                : Colors.lightBlue, // This is what you need!
                          ),
                        ),
                      ]),
                ),
              ),
              const SizedBox(height: 1, width: 10),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(children: [
                  Container(
                      decoration:
                          BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                      child: const Text("Mark Exact Location of Event",
                          style: TextStyle(fontSize: 16)))
                ]),
              ),
              const SizedBox(height: 1, width: 10),
              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(10)),
                child: Padding(
                  padding: const EdgeInsets.all(6.0),
                  child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        SizedBox(
                          child: GoogleMapsNoRadiusScreen(
                              parentAction: _updateLocation),
                          height: MediaQuery.of(context).size.height * 0.59,
                          width: MediaQuery.of(context).size.width * 0.93,
                        ),
                      ]),
                ),
              ),
              const SizedBox(height: 1, width: 10),
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Select the Date and Time of Event",
                            style: TextStyle(fontSize: 16))),
                    //type
                  ],
                ),
              ),

              Container(
                decoration: BoxDecoration(
                    border: Border.all(),
                    borderRadius: BorderRadius.circular(20)),
                height: 200,
                child: CupertinoDatePicker(
                  mode: CupertinoDatePickerMode.dateAndTime,
                  initialDateTime: DateTime.now(),
                  onDateTimeChanged: (DateTime newDateTime) {
                    setState(() {
                      selectedDateTime = newDateTime;
                    });
                  },
                  use24hFormat: false,
                  minuteInterval: 1,
                ),
              ),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Participant Limit",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                decoration: InputDecoration(
                  hintText: ('e.g. 5'),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: BorderSide(),
                  ),
                ),
                keyboardType: TextInputType.number,
                controller: participantLimitController,
              )),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Spectator Limit",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                decoration: InputDecoration(
                  hintText: ('e.g. 2'),
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(10.0),
                    borderSide: BorderSide(),
                  ),
                ),
                keyboardType: TextInputType.number,
                controller: spectatorLimitController,
              )),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                            BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Enter Event Rules",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                    decoration: InputDecoration(
                      hintText: ('e.g. "Be kind!"'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.text,
                    controller: rulesController,
                  )
              ),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                        BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Enter Any Equipment Requirements",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                    decoration: InputDecoration(
                      hintText: ('e.g. "tennis racket"'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.text,
                    controller: equipmentRequirementController,
                  )
              ),

              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(
                  children: [
                    Container(
                        decoration:
                        BoxDecoration(color: Colors.blue.withOpacity(0.4)),
                        child: const Text("Enter Contact Info",
                            style: TextStyle(fontSize: 16)))
                  ],
                ),
              ),
              Container(
                  child: TextFormField(
                    decoration: InputDecoration(
                      hintText: ('05xxxxxxxxx'),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10.0),
                        borderSide: BorderSide(),
                      ),
                    ),
                    keyboardType: TextInputType.phone,
                    controller: contactInfoController,
                  )
              ),
              const SizedBox(height: 15, width: 10),
              ElevatedButton(
                onPressed: () {
                  showAlertDialog(context);
                },
                child: const Text(
                  "CREATE",
                  style: TextStyle(fontSize: 16),
                ),
              ), //map
              const SizedBox(height: 20, width: 10),
            ],
          ),
        ));
  }
}
