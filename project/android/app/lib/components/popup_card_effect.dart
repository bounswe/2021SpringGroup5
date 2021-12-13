import 'package:flutter/material.dart';

class PopupCardEffect<T> extends PageRoute<T> {
  PopupCardEffect({
    required WidgetBuilder builder,
    RouteSettings? settings,
    bool fullscreenDialog = false,
  })  : _builder = builder,
        super(settings: settings, fullscreenDialog: fullscreenDialog);

  final WidgetBuilder _builder;

  @override
  bool get opaque => false;

  @override
  bool get maintainState => true;

  @override
  bool get barrierDismissible => true; // close when click outside

  @override
  Duration get transitionDuration => const Duration(milliseconds: 400);

  @override
  Color get barrierColor => Colors.black.withOpacity(0.6);

  @override
  Widget buildTransitions(BuildContext context, Animation<double> animation,
      Animation<double> secondaryAnimation, Widget child) {
    return child;
  }

  @override
  Widget buildPage(BuildContext context, Animation<double> animation,
      Animation<double> secondaryAnimation) {
    return _builder(context);
  }

  @override
  String get barrierLabel => 'popup Event details open';
}
