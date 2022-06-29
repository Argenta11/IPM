import 'package:flutter/cupertino.dart';
import 'package:ipm/views/view01.dart';
import 'package:ipm/views/view01tablet.dart';

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth > 767) {
          return const View01Tablet(title: 'Accesos COVID Tablet');
        }
        else {
          return const View01(title: 'Accesos COVID');
        }
      },
    );
  }
}