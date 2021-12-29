import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:ludo_app/components/rounded_input_field.dart';
import 'package:ludo_app/components/rounded_password_field.dart';
import 'package:ludo_app/screens/login/login_screen.dart';

void main() {
  testWidgets('if username: bbbbbbbb and pasword is 123 ; user can login and see main page.',
      (WidgetTester tester) async {
    LoginScreen loginScreen = const LoginScreen(message: 'test');
    var app =  MediaQuery(
        data:  const MediaQueryData(),
        child:  MaterialApp(home: loginScreen));

    await tester.pumpWidget(app);

    Finder username = find.byType(RoundedInputField);

    await tester.enterText(username, 'bbbbbbbb');

    Finder password = find.byType(RoundedPasswordField);
    await tester.enterText(password, '123');

    Finder loginButton = find.byType(RaisedButton);
    await tester.tap(loginButton);

    await tester.pump();

    expect(find.text('PROFILE'), true);

      });
}
