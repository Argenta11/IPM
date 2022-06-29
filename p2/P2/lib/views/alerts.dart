import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class Alertas extends StatelessWidget {
  const Alertas({Key? key}) : super(key: key);

  void mostrarAlerta(BuildContext context, String texto, bool error) {
    String cabecera = "null";
    if (error = true) { // Si se trata de un error
      cabecera = AppLocalizations.of(context)!.error;
    } else if (error = false) {  // Si se trata de una petición correcta
      cabecera = AppLocalizations.of(context)!.seharealizadocorrectamente;
    }
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(   // Devuelve una alerta
            title: Text(cabecera),  // Con titulo de error o peticion correcta
            content: Text(texto), // El texto que el usuario quiera
            actions: <Widget>[
              TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)), //Botón de cerrar el diálogo
            ],
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    throw UnimplementedError();
  }
}
