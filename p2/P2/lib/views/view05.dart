import 'package:flutter/material.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view02.dart';
import 'package:ipm/views/view06.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'alerts.dart';

class View05 extends StatelessWidget {

  View05({Key? key}) : super(key: key);
  Alertas alerta = const Alertas();
  @override
  Widget build(BuildContext context) {
    final providerinst = Provider.of<ProviderInst>(context);
    String instalacion = providerinst.instalacionactual;  // Guardamos la instalación actual para cuando vayamos a la vista 2
    TextEditingController _entradatemperatura=TextEditingController(text:"");
    return Scaffold(
      appBar: AppBar(
        title: Text(AppLocalizations.of(context)!.accesoscovid),
      ),
      body: Column(

          children: <Widget>[
            Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Container(child:View06().essalida(context)),  // Llamamos a la función de View06 que nos saca la lista de datos adecuados para el tipo de acceso
                  TextField(
                    controller:_entradatemperatura,
                    decoration: InputDecoration(  // Input de la temperatura
                      hintText: AppLocalizations.of(context)!.temperatura,
                      contentPadding: const EdgeInsets.all(10.0),
                    ),
                    // se dispara cuando el valor cambia
                  ),
                ]),
            ElevatedButton(
                onPressed: () => {
                  providerinst.hacerpost(_entradatemperatura.text),
                  mostrarMensaje(context, providerinst)
                },
                child: Text(AppLocalizations.of(context)!.anotar)),
            ElevatedButton(
                onPressed: () => {
                  traspost(context, providerinst),
                },
                child: Text(AppLocalizations.of(context)!.continuar)),

            ElevatedButton(
                onPressed: () => {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => View02(instalacion)))
                },
                child: Text(AppLocalizations.of(context)!.volver)),
          ]),

    );
  }

  void mostrarMensaje(BuildContext context, providerinst) {
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog( // Devuelve una alerta
            title: Text(AppLocalizations.of(context)!.conecbd), // Con titulo de error o peticion correcta
            content: Text(AppLocalizations.of(context)!.anabd), // El texto que el usuario quiera
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


  void traspost(context, providerinst){
    if(providerinst.resultadopost!=0) {
      if (providerinst.resultadopost == 200) {
        mostrarAlerta(context, AppLocalizations.of(context)!.anadidocorrecto, false, providerinst);

      } else {
        mostrarAlerta(context, AppLocalizations.of(context)!.noanadidocorrecto, true, providerinst);
      }
    }
  }
  void mostrarAlerta(BuildContext context, String texto, bool error,providerinst) {

    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(   // Devuelve una alerta
            title: Text(AppLocalizations.of(context)!.resultadobd),  // Con titulo de error o peticion correcta
            content: Text(texto), // El texto que el usuario quiera
            actions: <Widget>[
              TextButton(
                  onPressed: () {
                    providerinst.resultadopost = 0;
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => View02(providerinst.instalacionactual)));
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)), //Botón de cerrar el diálogo
            ],
          );
        });
  }

}