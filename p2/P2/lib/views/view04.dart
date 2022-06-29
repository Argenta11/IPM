import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_barcode_scanner/flutter_barcode_scanner.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view05.dart';
import 'dart:async';
import 'package:provider/provider.dart';
import 'alerts.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

class View04 extends StatefulWidget {
  const View04({Key? key}) : super(key: key);
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<View04> {
  String stringqr = '';
  bool qr=false;
  Alertas alerta = const Alertas();

  @override
  void initState() {
    super.initState();
  }

  Future<void> scanQR() async { // Función que escanea el QR
    String barcodeScanRes;
    // Platform messages may fail, so we use a try/catch PlatformException.
    try {
      barcodeScanRes = await FlutterBarcodeScanner.scanBarcode(
          '#ff6666', 'Cancel', true, ScanMode.QR);  // Modo de escanear QR
      stringqr = barcodeScanRes;
      qr=true;
    } on PlatformException {
      barcodeScanRes = 'Failed to get platform version.';
    }

    if (!mounted) return;

    setState(() {
    });
  }

  String qrpreparado(stringqr) {  // Función que coge solo el uuid del qr
    String stringqr2 = stringqr.replaceAll('{', '').replaceAll('}', '');
    List partesqraux = stringqr2.split(',');
    return partesqraux[0];
  }

  @override
  Widget build(BuildContext context) {
    final providerinst = Provider.of<ProviderInst>(context);
    TextEditingController _entradauuid = TextEditingController(text: "");

    return Column(children: <Widget>[
      Text(
        '',
        style: Theme.of(context).textTheme.headline5,
      ),
      ElevatedButton( // Icono con forma de cámara que te lleva a la función que abre la cámara para escanear QR
        onPressed: () => scanQR(),
        child: Icon(Icons.camera_alt_outlined, size: 90, color: Colors.white),
        style: ElevatedButton.styleFrom(
          shape: CircleBorder(),

          padding: EdgeInsets.all(10),
          primary: Colors.black, // <-- Button color
          onPrimary: Colors.pink, // <-- Splash color
        ),
      ),
      Text(
        AppLocalizations.of(context)!.seleccionainstalacion,
        style: Theme.of(context).textTheme.headline5,
      ),
      Text(
        stringqr, // Mostramos lo leido por el QR o por la entrada de texto
        style: Theme.of(context).textTheme.headline6,
      ),
      Text(
        AppLocalizations.of(context)!.escanearaqui,
        style: Theme.of(context).textTheme.headline6,
      ),
      Container(
          child: TextField( // Recogemos la entrada del usuario
            controller: _entradauuid, // Controlador
            decoration: const InputDecoration(
              hintText: 'Uuid',
              contentPadding: EdgeInsets.all(10.0),
            ),
            // se dispara cuando el valor cambia
          )),



      ElevatedButton(
          onPressed: () => {
            stringqr=_entradauuid.text,
            formateuuid(stringqr, context),
          },
          child: Text(AppLocalizations.of(context)!.cargaruuid)),  // Botón que carga el uuid seleccionado en el texto

      ElevatedButton(

          onPressed: () => {
            if(qr==true){ // Si es el qr el que hemos leido, comprobamos su formato y recogemos el uuid de él
              if(_formatocorrecto(stringqr)){
                if(formatouuid(qrpreparado(stringqr), context)){
                  providerinst.anadirpersona(qrpreparado(stringqr),'NO'),
                  mostrarAviso(context, providerinst)
                }
                else
                  {
                    alerta.mostrarAlerta(context, AppLocalizations.of(context)!.noencontraruuid, true),
                  }} else
                {
                  alerta.mostrarAlerta(context, AppLocalizations.of(context)!.qrnovalido, true),
                }
            }else{  // Si no es qr, solo comprobamos el uuid añadido
              if(formatouuid(stringqr, context)){
                providerinst.anadirpersona(qrpreparado(stringqr),'NO'),
                mostrarAviso(context, providerinst)
              }
              else
                {
                  alerta.mostrarAlerta(context, AppLocalizations.of(context)!.noencontraruuid, true),
                }
            }
          },
          child: Text(AppLocalizations.of(context)!.continuar)),  // Botón para ir a añadir el acceso

    ]);
  }

  void formateuuid(uuid, context){  // Función que hace que el provider guarde si el uuid es correcto
    final providerinst = Provider.of<ProviderInst>(context,listen: false);
    providerinst.comprobaruuid(uuid);
    qr=false;
  }

  bool formatouuid(uuid, context){  // Función que comprueba si el uuid fue correcto
    final providerinst = Provider.of<ProviderInst>(context,listen: false);
    return providerinst.euuid();
  }

  void mostrarAviso(BuildContext context, providerinst) { // Función que muestra que el uuid añadido es correcto
    String cabecera = "null";

    cabecera = AppLocalizations.of(context)!.realizadocorrecto;
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text(cabecera),
            content: Text(AppLocalizations.of(context)!.uuidcorrecto),
            actions: <Widget>[
              TextButton(
                  onPressed: () => {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => View05())),
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)),
            ],
          );
        });
  }
  bool _formatocorrecto(String texto) { // Comprueba si el formato del qr es correcto
    List partes = texto.split(',');
    if (partes.length != 3) {
      return false;
    }
    if (!partes[0].contains('{') || !partes[0].contains('}')) {
      return false;
    }
    if (!partes[1].contains('{') || !partes[1].contains('}')) {
      return false;
    }
    if (!partes[2].contains('{') || !partes[2].contains('}')) {
      return false;
    }
    return true;
  }
}

