import 'package:flutter/material.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view02.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
class View06 extends StatelessWidget{
  const View06({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
      return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(AppLocalizations.of(context)!.accesoscovid),
      ),
      body: essalida(context),
      //), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
  String formatfecha(String f,context){ // Función que formatea la fecha al formato de la BD
    var tag=Localizations.maybeLocaleOf(context)!.toLanguageTag();
    List divido = f.split('T');
    List fecha = divido[0].split('-');
    List hora = divido[1].split(':');
    String result="Error";
    if(tag=='es'){
       result = fecha[2]+'-'+fecha[1]+'-'+fecha[0]+" "+hora[0]+":"+hora[1];
    }else if(tag=='gl'){
      result = fecha[1]+'-'+fecha[2]+'-'+fecha[0]+" "+hora[0]+":"+hora[1];
    }
  return result;
  }
  Widget salida(context) {
    // Lista de datos que saca cuando se trata de una salida

    final providerinst = Provider.of<ProviderInst>(context);
    List datosanteriores = providerinst
        .datosanadirpersona; // Recoge nombre y apellidos
    if (compruebaerror(providerinst.datosanadirpersona)) {
      if(compruebaerror(providerinst.ultimoacceso)) {
        for (int i = 0; i < providerinst.ultimoacceso.length; i++) {
          datosanteriores.add(providerinst
              .ultimoacceso[i]); // Recoge sus datos del ultimo acceso (la entrada)
        }
        return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Text(
                AppLocalizations.of(context)!.informacionrecogida,
                style: Theme
                    .of(context)
                    .textTheme
                    .headline3,
              ),
              Text(
                AppLocalizations.of(context)!.uuid + datosanteriores[0],
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.nombre + datosanteriores[1],
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.apellido + datosanteriores[2],
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.instalacion + providerinst.instalacionactual,
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.entrada + formatfecha(datosanteriores[4],context),
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.temperaturaentrada + datosanteriores[5],
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),

              Text(
                AppLocalizations.of(context)!.salida + formatfecha(providerinst.datosanadirpersona[3],context),
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),
              Text(
                AppLocalizations.of(context)!.introducelossiguientesdatos,
                style: Theme
                    .of(context)
                    .textTheme
                    .headline5,
              ),

            ]);
      }else{
        mostrarAviso(context,providerinst);
        return Text(AppLocalizations.of(context)!.error);
      }
    }else{
      mostrarAviso(context,providerinst);
      return Text(AppLocalizations.of(context)!.error);

    }
  }
  Widget entrada(context){  // Lista de datos si es una entrada
    final providerinst = Provider.of<ProviderInst>(context);
    if (compruebaerror(providerinst.datosanadirpersona)) {
    return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text(
            AppLocalizations.of(context)!.informacionrecogida,
            style: Theme.of(context).textTheme.headline3,
          ),
          Text(
            AppLocalizations.of(context)!.uuid + providerinst.datosanadirpersona[0],
            style: Theme.of(context).textTheme.headline5,
          ),
          Text(
            AppLocalizations.of(context)!.nombre + providerinst.datosanadirpersona[1],
            style: Theme.of(context).textTheme.headline5,
          ),
          Text(
            AppLocalizations.of(context)!.apellido + providerinst.datosanadirpersona[2],
            style: Theme.of(context).textTheme.headline5,
          ),
          Text(
            AppLocalizations.of(context)!.entrada + formatfecha(providerinst.datosanadirpersona[3],context),
            style: Theme.of(context).textTheme.headline5,
          ),
          Text(
            AppLocalizations.of(context)!.instalacion + providerinst.instalacionactual,
            style: Theme.of(context).textTheme.headline5,
          ),
          Text(
            AppLocalizations.of(context)!.introducelossiguientesdatos,
            style: Theme.of(context).textTheme.headline5,
          ),
        ]);
    }else{
      mostrarAviso(context,providerinst);
      return Text(AppLocalizations.of(context)!.error);

    }
  }
  Widget essalida(context) {
    final providerinst = Provider.of<ProviderInst>(context);
    List ultimo = providerinst.ultimoacceso;
    if (ultimo[ultimo.length - 1] == 'IN') {
      return salida(context);
    } else {
      return entrada(context);
    }
  }

  bool compruebaerror(List comprobamos){
    if(comprobamos[0].contains(':')) {
      List comprueba=comprobamos[0].split(':');
      if (comprueba[0]=='Error en la BD') {
        return false;
      }
    }
    return true;
    }

  void mostrarAviso(BuildContext context, providerinst) { // Función que muestra que el uuid añadido es correcto
    String cabecera = "null";

    cabecera = AppLocalizations.of(context)!.errorenlabasededatos;
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text(cabecera),
            content: Text(AppLocalizations.of(context)!.intentelodenuevo),
            actions: <Widget>[
              TextButton(
                  onPressed: () => {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => View02(providerinst.instalacionactual))),
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)),
            ],
          );
        });
  }

}