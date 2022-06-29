import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/myhomepage.dart';
import 'package:ipm/views/view01.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';




void main() { // Main construye mi apliación
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    return ChangeNotifierProvider(create: (context) => ProviderInst(),


      child: MaterialApp(
        title: 'Accesos COVID',
        theme: ThemeData(
          primarySwatch: Colors.pink,
        ),
        localizationsDelegates: const [
          AppLocalizations.delegate, // Add this line
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          GlobalCupertinoLocalizations.delegate,
        ],
        supportedLocales: const [
          Locale('es', ''), // Español
          Locale('gl', ''), // Gallego
        ],
        home: const MyHomePage(), // Mostramos la vista de inicio (lista de instalaciones)
      ),
    );
  }
}