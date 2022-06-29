import 'package:flutter/material.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view01.dart';
import 'package:ipm/views/view03.dart';
import 'package:ipm/views/view04.dart';
import 'package:ipm/views/view07.dart';
import 'package:provider/provider.dart';
import 'alerts.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

import 'myhomepage.dart';

const List<Tab> tabs = <Tab>[ // Iconos que ponemos en la barra superior para navegar
  Tab(child: Icon(Icons.account_circle_outlined)),
  Tab(child: Icon(Icons.add)),
  Tab(child: Icon(Icons.access_time)),
];

class View02 extends StatelessWidget {  // Vista de la lista de accesos
  final instalacion;  // Variable que es la instalacion actual
  View02(this.instalacion, {Key? key}) : super(key: key);
  Alertas alerta = const Alertas(); // Instanciamos la clase alerta

  @override
  Widget build(BuildContext context) {
    final providerinst = Provider.of<ProviderInst>(context, listen:false);  //  Definimos el provider


    return DefaultTabController(  // Barra superior para navegar
      length: tabs.length,  // Longitud igual al numero de iconos
      child: Builder(builder: (BuildContext context) {
        final TabController tabController = DefaultTabController.of(context)!;  // Llamamos a la funcion que indica que pasa si les pulsas
        tabController.addListener(() {
          if (!tabController.indexIsChanging) {
          }
        });
        return DefaultTabController(  // Que ocurre si pulsas cada icono
          length: tabs.length,
          child: Scaffold(  // Devolvemos la misma estructura de vista, incluyendo tabs (botones de navegación)
            appBar: AppBar(
              title: Text(AppLocalizations.of(context)!.accesoscovid),
              bottom: TabBar(
                unselectedLabelColor: Colors.white,
                indicatorPadding: const EdgeInsets.only(left: 30, right: 30),
                indicator: ShapeDecoration(
                    color: Colors.pink,
                    shape: BeveledRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                        side: const BorderSide(
                          color: Colors.white,
                        ))),
                tabs: tabs,
              ),
            ),
            body: TabBarView(children: [
              Center(child: vista3(context, providerinst)), // Con el primer tab llamamos a la función vista3
              Center(child: View04()),  // Con el segundo tab llamamos a la clase View04
              Center(child: View07()),  // Con el tercer tab llamamos a la clase View07
            ]),
          ),
        );
      }),
    );

  }

  Widget vista3(context, providerinst) {  // Funcion que nos muestra la lista de accesos

    return Column(  // Columna principal con todos los Widgets
      children: <Widget>[
        Row(  // Fila con los botones de arriba
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: <Widget>[
              ElevatedButton(
                  onPressed: () => {
                    Navigator.push(context, MaterialPageRoute(builder: (context) => View03()))
                  },
                  child: Text(AppLocalizations.of(context)!.filtrar)),  // Botón que si pulsas lleva al calendario para filtrar por fechas

              ElevatedButton(
                  onPressed: () => {
                    mostrardatos(providerinst,context)
                  },
                  child: Text(AppLocalizations.of(context)!.verdatos)), // Botón que permite ver los datos de la instalación

              ElevatedButton(
                  onPressed: () => {
                    providerinst.filtrado=false,  // Si pulso el botón de quitar filtros guardo la variable como no filtrado
                    providerinst.startDate="Siempre",
                    providerinst.endDate="Siempre",
                    Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => View02(providerinst.instalacionactual)) // Actualizo la vista
                    )}, child: Text(AppLocalizations.of(context)!.sinfiltro)),
            ]),
        Row(
            children: <Widget>[
              Expanded(child:Column(children: <Widget>[Text(AppLocalizations.of(context)!.fechainicio),Text(formatfecha(providerinst.startDate, context))])),
              Expanded(child:Column(children: <Widget>[Text(AppLocalizations.of(context)!.fechafin),Text(formatfecha(providerinst.endDate, context))]))
            ]
        ),
        Expanded( // Para que ocupe toda la pantalla
          child: FutureBuilder( // Construcción de la lista de accesos
              future: providerinst.accesoss(),  // Obtenemos los datos del provider
              builder: (BuildContext context, AsyncSnapshot<List<List<String>>> snapshot) {
                if (snapshot.connectionState == ConnectionState.done &&
                    !snapshot.hasError) {
                  List<List<String>>? data = snapshot.data; // Guardamos en data los datos
                  return ListView.builder(
                      itemCount: data!.length,  // Longitud igual a la de la lista
                      itemBuilder: (BuildContext context, int index) {  // Para cada acceso
                        return ListTile(
                          onTap: () { // Si pulsas
                            mostrarUsuario( // Se llama a la funcion que saca la ventana con los datos, pasando los de ese acceso
                                context,
                                data[index][0],
                                data[index][1],
                                data[index][2],
                                data[index][3],
                                data[index][4],
                                data[index][5]);
                          },
                          title: Text(data[index][0]),    // Nombre de la persona en grande
                          subtitle: Text(data[index][1]), // En más pequeño el uuid
                          leading: CircleAvatar(
                            child: Text((index + 1).toString()),  // Círculo de la izquierda que muestra el puesto en la lista
                          ),
                          trailing: const Icon(Icons.arrow_forward_ios),  // Flechas de la derecha
                        );
                      });
                }
                else if (snapshot.connectionState != ConnectionState.done) {  //  Si no está cargada la base de datos muestra un spinner
                  return Center(
                    child: Column(
                      children: <Widget>[
                        Text(snapshot.connectionState.toString()),
                        Text(''),
                        CircularProgressIndicator(),
                      ],
                    ),
                  );
                }
                else {  // Si no existe muestra error
                  return Center(
                    child: SingleChildScrollView(
                      child: Column(
                        children: <Widget>[
                          Image.asset('images/snoopy-penalty666666666666-box.gif'),
                          Text(AppLocalizations.of(context)!.errorarchivo),
                        ],
                      ),
                    ),
                  );
                }
              }),
        ),
        ElevatedButton(
            onPressed: () => {
              if(providerinst.tablet==true){
                providerinst.instalacionactual=""
              },
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => const MyHomePage()))
            },
            child: Text(AppLocalizations.of(context)!.volver)), // Si pulsas este botón vuelves a la lista de instalaciones

      ],
    );
  }

  void mostrardatos(providerinst, context){ // Función que muestra los datos de la instalación
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text(AppLocalizations.of(context)!.datosactuales),
            content: Text(AppLocalizations.of(context)!.accesosactuales+providerinst.personasactuales.length.toString()  // Personas que hay ahora mismo dentro
                +AppLocalizations.of(context)!.accesostotales+providerinst.numaccesos.toString()), // Accesos que ha habido en la instalación en total
            actions: <Widget>[
              TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)), // Botón para cerrar el diálogo
            ],
          );
        });


  }

  void mostrarUsuario(BuildContext context, String nombre, String uuid,
      String f1, String t1, String f2, String t2) { // Función que muestra los datos del acceso
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text(nombre),
            content: Text("Uuid: " +
                uuid +
                "\n"+AppLocalizations.of(context)!.entrada +
                formatfecha(f1, context) +
                "\n"+AppLocalizations.of(context)!.temperaturaentrada +
                t1 +
                "\n"+AppLocalizations.of(context)!.salida +
                formatfecha(f2, context) +
                "\n"+AppLocalizations.of(context)!.temperaturasalida +
                t2),
            actions: <Widget>[
              TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)),
            ],
          );
        });
  }

  String formatfecha(String f, context) {  // Función que formatea la fecha para que sea más cómodo para el usuario
    var tag=Localizations.maybeLocaleOf(context)!.toLanguageTag();
    if (f != 'No') {
      if (f != 'Siempre') {
        if(tag=='es'){
          List divido = f.split('T');
          List fecha = divido[0].split('-');
          List hora = divido[1].split(':');
          String result = fecha[2] +
              '/' +
              fecha[1] +
              '/' +
              fecha[0] +
              " " +
              hora[0] +
              ":" +
              hora[1];
          return result;
        }else if(tag=='gl'){
          List divido = f.split('T');
          List fecha = divido[0].split('-');
          List hora = divido[1].split(':');
          String result = fecha[1] +
              '/' +
              fecha[2] +
              '/' +
              fecha[0] +
              " " +
              hora[0] +
              ":" +
              hora[1];
          return result;
        }
        return AppLocalizations.of(context)!.siempre;
      }else {
        return AppLocalizations.of(context)!.siempre;
      }} else {
      return AppLocalizations.of(context)!.no;
    }
  }




}


