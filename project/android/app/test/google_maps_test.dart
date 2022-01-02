import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:ludo_app/screens/main_events/main_event_screen.dart';

void main() {
  testWidgets('check if the map marker is working', (WidgetTester tester) async {
    MainEventScreen mainScreen = const MainEventScreen();
    var app = MediaQuery(
        data: const MediaQueryData(), child: MaterialApp(home: mainScreen));

    await tester.pumpWidget(app);

    await tester.tap(find.text('PROFILE'));

    await tester.pumpAndSettle();

    expect(find.widgetWithText(Scrollable, 'Profile Info'), findsOneWidget);


  });
}
