import 'package:flutter/material.dart';
import 'package:ipm/provider/providerinstalaciones.dart';
import 'package:ipm/views/view02.dart';
import 'package:provider/provider.dart';
import 'package:syncfusion_flutter_datepicker/datepicker.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'alerts.dart';


/// My app class to display the date range picker
class View03 extends StatefulWidget {
  const View03({Key? key}) : super(key: key);

  @override
  MyAppState createState() => MyAppState();

}

/// State for MyApp
class MyAppState extends State<View03> {  // Vista para seleccionar las fechas
  String fechas="";
  Alertas alerta = const Alertas();

  void _onSelectionChanged(
       DateRangePickerSelectionChangedArgs dateRangePickerSelectionChangedArgs) {
     fechas=dateRangePickerSelectionChangedArgs.value.toString(); // Convertimos las fechas a String para poder guardarlas
   }
  @override
  Widget build(BuildContext context) {
    final providerinst = Provider.of<ProviderInst>(context);
    List<String> formato;
    List inicio;
    List<String> fin;
    String finicio;
    String ffin;
    return MaterialApp(
        home: Scaffold(
            appBar: AppBar(
              title: Text(AppLocalizations.of(context)!.accesoscovid),
            ),
            body: Column(
              children: <Widget>[
                  Text(
                    AppLocalizations.of(context)!.elrangodefechases,
                  style: Theme.of(context).textTheme.headline5,
                  ),
                  SfDateRangePicker(
                  view: DateRangePickerView.month,
                  monthViewSettings: DateRangePickerMonthViewSettings(firstDayOfWeek: 1), // Ponemos primer día de la semana en lunes
                    onSelectionChanged: _onSelectionChanged,  // Controlador
                    selectionMode: DateRangePickerSelectionMode.range,  // Modo de seleccionar un rango de fechas

                  ),

                ElevatedButton(
                  onPressed:() async {
                    // Formateamos las fechas en las siguientes lineas
                    formato=fechas.split('(')[1].split(')')[0].split(',');
                    inicio = formato[0].split(' ');
                    fin = formato[1].split(' ');
                    finicio=inicio[1]+'T'+inicio[2]+'+00:00';
                    ffin=fin[2]+'T'+fin[3]+'+00:00';

                    providerinst.filtrarfecha(finicio, ffin); // Enviamos el rango en el provider
                    mostrarAviso(context, providerinst);  // Mostramos el aviso de que ha ocurrido de forma correcta

                  },
                  child: Text(AppLocalizations.of(context)!.filtrar),
                ),
              ],
            )));
  }
  void mostrarAviso(BuildContext context, providerinst) { // Función que muestra que se ha filtrado
    String cabecera = "null";

      cabecera = AppLocalizations.of(context)!.seharealizadocorrectamente;
    showDialog(
        barrierDismissible: false,
        context: context,
        builder: (context) {
          return AlertDialog(
            title: Text(cabecera),
            content: Text(AppLocalizations.of(context)!.sehafiltradodeformacorrecta),
            actions: <Widget>[
              TextButton(
                  onPressed: () => {
                    Navigator.push(context,
                        MaterialPageRoute(
                            builder: (context) => View02(providerinst.instalacionactual)))  // Actualizamos la vista 2
                  },
                  child: Text(AppLocalizations.of(context)!.cerrar)),
            ],
          );
        });
  }
}