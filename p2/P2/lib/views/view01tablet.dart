import 'package:flutter/material.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view02.dart';
import 'package:ipm/views/view04.dart';
import 'package:ipm/views/view07.dart';
import 'package:provider/provider.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';

const List<Tab> tabs = <Tab>[ // Iconos que ponemos en la barra superior para navegar
  Tab(child: Icon(Icons.account_circle_outlined)),
  Tab(child: Icon(Icons.add)),
  Tab(child: Icon(Icons.access_time)),
];

class View01Tablet extends StatefulWidget { // Vista Home de la aplicación

  const View01Tablet({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<View01Tablet> createState() => _View01TabletState();  // Creamos un estado (Vista Stateful)
}

class _View01TabletState extends State<View01Tablet> {


  Widget build(BuildContext context) {
    final providerinst = Provider.of<ProviderInst>(context, listen:false);  //  Definimos el provider
    providerinst.tablet=true;

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

  Widget vista3(context, providerinst){
    final view02 = View02(providerinst);
    return Row(
        children: <Widget>[
          //const View01(title:"Accesos COVID")
          Columna1(),
          SizedBox(
              width: 450,
              child: view02.vista3(context, providerinst)
          ),
          //Text("Aquí iría la segunda lista")
        ]
    );
  }

  Widget Columna1(){
    final providerinst = Provider.of<ProviderInst>(context,listen: false);
    providerinst.initdata();  // Inicializamos los datos de las instalaciones
    return SizedBox(
        width: 300.0,
      child: Column(
      children: [
        Container(
          child: Text(
            AppLocalizations.of(context)!.seleccionainstalacion,
            style: Theme.of(context).textTheme.headline5,
          ),
        ),

        Expanded(
          child: FutureBuilder( // Widget con la lista de instalaciones
              future: providerinst.instalacioness(),  // Depende de la lista de instalaciones del provider
              builder: (BuildContext context, AsyncSnapshot<List<String>> snapshot) {
                if (snapshot.connectionState == ConnectionState.done &&
                    !snapshot.hasError) {
                  List<String>? data = snapshot.data; // Guardamos en data los datos de la lista
                  return ListView.builder(
                      itemCount: data!.length,  // Tamaño del Widget, el de la lista
                      itemBuilder: (BuildContext context, int index) {
                        return ListTile(  // Cada una de las casillas de la ListView
                          onTap: () {
                            // En estas tres lineas recogemos la instalacion para inicializar los datos de la instalacion
                            final prep = data[index].split('(');
                            final ins = prep[1].split(')');
                            providerinst.initdata2(ins[0]);

                            Navigator.push(context,
                                MaterialPageRoute(builder: (context) =>
                                    View01Tablet(title: 'Accesos COVID Tablet')));  // Despues accedemos a la lista 2 (lista de accesos)
                          },
                          title: Text(data[index]), // Nombre de la instalacion y su id
                          leading: CircleAvatar(
                            child: Text((index + 1).toString()),  // Le ponemos el circulo de la izquierda con el puesto en la lista
                          ),
                          trailing: const Icon(Icons.arrow_forward_ios),  // Icono de las flechas de la derecha
                        );
                      });
                }
                else if (snapshot.connectionState != ConnectionState.done) {  // En caso de que no conecte la BD, activamos el spinner
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
                else {  // En caso de fallo de no existencia emitimos el error
                  return Center(
                    child: SingleChildScrollView(
                      child: Column(
                        children: <Widget>[
                          Image.asset('images/snoopy-penalty-box.gif'),
                          Text(AppLocalizations.of(context)!.errorarchivo),
                        ],
                      ),
                    ),
                  );
                }
              }),
        ),
      ],
    ));
  }
}
