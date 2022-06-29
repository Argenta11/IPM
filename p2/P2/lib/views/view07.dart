import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_barcode_scanner/flutter_barcode_scanner.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view05.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

import 'alerts.dart';

class View07 extends StatefulWidget {
  const View07({Key? key}) : super(key: key);
  @override
  _MyAppState2 createState() => _MyAppState2();
}

class _MyAppState2 extends State<View07> {
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
    TextEditingController _entradauuid2 = TextEditingController(text: "");
    var tag=Localizations.maybeLocaleOf(context)!.toLanguageTag();


    return Column(children: <Widget>[
      Text(
        '',
        style: Theme.of(context).textTheme.headline5,
      ),
      ElevatedButton( // Icono con forma de cámara que te lleva a la función que abre la cámara para escanear QR
        onPressed: () => scanQR(),
        child: Icon(Icons.camera_alt_outlined, size: 60, color: Colors.white),
        style: ElevatedButton.styleFrom(
          shape: CircleBorder(),

          padding: EdgeInsets.all(10),
          primary: Colors.black, // <-- Button color
          onPrimary: Colors.pink, // <-- Splash color
        ),
      ),
      Text(
        AppLocalizations.of(context)!.qriconouuid,
        style: Theme.of(context).textTheme.headline6,
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
          child: TextField(
            controller: _entradauuid,
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

      TextField(
        controller: _entradauuid2,
        decoration: InputDecoration(
          hintText: AppLocalizations.of(context)!.formatofechahora,
          contentPadding: EdgeInsets.all(10.0),
        ),

        // se dispara cuando el valor cambia
      ),


      ElevatedButton(

          onPressed: () => {
            if(qr==true){ // Si es el qr el que hemos leido, comprobamos su formato y recogemos el uuid de él
              if(_formatocorrecto(stringqr)){
                if(formatofecha(_entradauuid2.text)){
                  if(formatouuid(qrpreparado(stringqr), context)){
                    providerinst.anadirpersona(qrpreparado(stringqr),formatearfechaBD(_entradauuid2.text)),
                    mostrarAviso(context, providerinst)
                  }
                  else
                    {
                      alerta.mostrarAlerta(context, AppLocalizations.of(context)!.noencontraruuid, true),
                    }
                }else{
                  alerta.mostrarAlerta(context, AppLocalizations.of(context)!.fechanovalida, true),
                }

              } else
                {
                  alerta.mostrarAlerta(context, AppLocalizations.of(context)!.qrnovalido, true),
                }
            }else{  // Si no es qr, solo comprobamos el uuid añadido
              if(formatofecha(_entradauuid2.text)){
                if(formatouuid(stringqr, context)){
                  providerinst.anadirpersona(qrpreparado(stringqr),formatearfechaBD(_entradauuid2.text)),
                  mostrarAviso(context, providerinst)
                }
                else
                  {
                    alerta.mostrarAlerta(context, AppLocalizations.of(context)!.noencontraruuid, true),
                  }
              }else{
                alerta.mostrarAlerta(context, AppLocalizations.of(context)!.fechanovalida, true),
              }
            }
          },
          child: Text(AppLocalizations.of(context)!.continuar)),

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
  
  String formatearfechaBD(String entrada){
    var tag=Localizations.maybeLocaleOf(context)!.toLanguageTag();
    String result="error";
    if(tag=='es'){
      result=entrada;
    }else if(tag=='gl'){
      List fechayhora=entrada.split(' ');
      List fecbase=fechayhora[0].split('-');
      List hora=fechayhora[1].split(':');
      
      result = fecbase[1]+'-'+fecbase[0]+'-'+fecbase[2]+" "+hora[0]+":"+hora[1];
    }
    return result;
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

  bool formatofecha(String fecha){  // Función que comprueba si una fecha es correcta
    var tag=Localizations.maybeLocaleOf(context)!.toLanguageTag();
    List fechayhora=fecha.split(' ');
    List fecbase=fechayhora[0].split('-');
    List hora=fechayhora[1].split(':');
    String fechactual = DateTime.now().toString();
    List fechayhora2=fechactual.split(' ');
    List fecaux=fechayhora2[0].split('-');
    List fec=[];
    List fec2=[];
    fec2.add(fecaux[2]);
    fec2.add(fecaux[1]);
    fec2.add(fecaux[0]);
    List hora2=fechayhora2[1].split(':');
    if(tag=='gl'){
      fec.add(fecbase[1]);
      fec.add(fecbase[0]);
      fec.add(fecbase[2]);
    }else if(tag=='es'){
      fec.add(fecbase[0]);
      fec.add(fecbase[1]);
      fec.add(fecbase[2]);
    }


    // Líneas que comprueban que no pasan del máximo de día, mes, hora o minutos
    if(int.parse(fec[1])>12){
      return false;
    }
    int diasdelmes = daysInMonth(int.parse(fec[1]), int.parse(fec[2])); // Llamamos a una función auxiliar que nos devuelve cuantos días tiene un mes en un año
    if(int.parse(fec[0])>diasdelmes){
      return false;
    }
    if(int.parse(hora[0])>23){
      return false;
    }
    if(int.parse(hora[1])>59){
      return false;
    }
    // Comprobación de que la fecha de salida no es anterior a la de entrada
    if(int.parse(fec[2])>int.parse(fec2[2])){
      return false;
    }else if(int.parse(fec[2])==int.parse(fec2[2])){
      if(int.parse(fec[1])>int.parse(fec2[1])){
        return false;
      }else if(int.parse(fec[1])==int.parse(fec2[1])){
        if(int.parse(fec[0])>int.parse(fec2[0])){
          return false;
        }else if(int.parse(fec[0])==int.parse(fec2[0])){
          if(int.parse(hora[0])>int.parse(hora2[0])){
            return false;
          }else if(int.parse(hora[0])==int.parse(hora2[0])){
            return false;
          }
        }
      }
    }
    return true;
  }


  static int daysInMonth(int month, int year) { // Devuelve los días que tiene un mes de un año
    int days = 28 + (month + (month/8).floor()) % 2 + 2 % month + 2 * (1/month).floor();
    return (isLeapYear(year) && month == 2)? 29 : days;
  }

  static bool isLeapYear(int year)  // Comprueba si ese año es bisiesto
  => (( year % 4 == 0 && year % 100 != 0 ) || year % 400 == 0 );

}