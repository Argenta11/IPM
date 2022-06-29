import 'dart:core';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ipm/model/model.dart';

class ProviderInst with ChangeNotifier {
  late List<String> _instalaciones=[];  // lista de instalaciones
  late List _uuids; // lista de uuids
  int _numuuids=0;  // numero de uuids
  late List _accesos =[]; // lista de accesos
  int _numinstalaciones=0;  // numero de instalaciones
  int _numaccesos=0;  // numero de accesos
  late String _instalacionactual="";  // instalacion de la que vemos los accesos
  late List _datosanadirpersona=[]; // datos para añadir a una persona
  late List _ultimoacceso=[]; // datos sobre el ultimo acceso de una persona
  late List _personasactuales=[]; // lista de pesrsonas actuales en la instalacion
  bool _existeuuid=false; // bool de si existe el uuid que se busco
  bool _filtrado=false; // bool de si la lista de accesos esta filtrada
  String _startDate="Siempre"; // fecha de inicio del filtro
  String _endDate="Siempre"; // fecha de fin del filtro
  late int _resultadopost=0;
  bool _tablet=false;
  final Model model = Model();  // modelo


  Future<List<String>> instalacioness() async{  // Función del FutureBuilder
    return  model.getInstalaciones();
  }

  Future<List<List<String>>> accesoss() async{  // Función del FutureBuilder
    if(filtrado==false){
      return  model.getAccesos(instalacionactual);  }
    else{
      return model.lista;
    }
  }

  Future initdata() async { // Función que inicializa los datos de las instalaciones
    instalaciones = await model.getInstalaciones();
    numinstalaciones = _instalaciones.length;
    filtrado=false;
  }

  Future initdata2(instalacionactualv) async{ // Función que inicializa los datos de los accesos
    instalacionactual=instalacionactualv;
    accesos = await model.getAccesos(instalacionactualv);
    numaccesos = await model.getnumAccesos(instalacionactualv);
    personasactuales = await model.getAccesosActuales(instalacionactualv);
  }

  Future anadirpersona(uuid, fecha) async {  // Función que obtiene los datos de la persona y su último acceso
    datosanadirpersona=await model.getNombreApellido(uuid, fecha);
    ultimoacceso=await model.getUltimoAcceso(uuid,_instalacionactual);

  }

  Future  comprobaruuid(String uuid) async{ // Función que comprueba si el uuid existe
    existeuuid= await model.existeuuid(uuid);
    notifyListeners();

  }

  bool euuid(){ // Función que devuelve si el uuid existía
    return model.existe;
  }

  Future filtrarfecha(String fi, String ff) async{  // Función que filtra obtiene los accesos filtrados por fechas
    startDate=fi;
    endDate=ff;
    filtrado=true;
    return model.getAccesosFiltrados(instalacionactual, startDate, endDate);

  }


  Future<int> hacerpost(temperatura) async{  // Función para añadir a una persona
    List datosfinales=[];
    // A los datos de la persona se le añaden los que faltan
    datosfinales.add(datosanadirpersona[0]);
    datosfinales.add(instalacionactual);
    datosfinales.add(datosanadirpersona[3]);
    if(ultimoacceso[ultimoacceso.length-1]=='IN'){
      datosfinales.add('OUT');
    }else{
      datosfinales.add('IN');
    }
    datosfinales.add(temperatura);

    var response = await Model().anadirAcceso(datosfinales); // Llamamos la función del modelo que lo sube
    resultadopost=response;
    return response;
  }


  // LISTA DE GETTERS Y SETTERS

  List<String> get instalaciones {
    return _instalaciones;
  }

  set instalaciones(List<String> instalaciones) {
    _instalaciones=instalaciones;
    notifyListeners();
  }
  List get uuids {
    return _uuids;
  }

  set uuids(List uuids) {
    _uuids=uuids;
    notifyListeners();
  }
  int get numuuids {
    return _numuuids;
  }
  set numuuids(int numuuids) {
    _numuuids=numuuids;
    notifyListeners();
  }

  int get numinstalaciones {
    return _numinstalaciones;
  }
  set numinstalaciones(int numinstalaciones) {
    _numinstalaciones=numinstalaciones;
    notifyListeners();
  }

  List get accesos {
    return _accesos;
  }

  set accesos(List accesos) {
    _accesos=accesos;
    notifyListeners();
  }

  int get numaccesos {
    return _numaccesos;
  }
  set numaccesos(int numaccesos) {
    _numaccesos=numaccesos;
    notifyListeners();
  }

  String get instalacionactual {
    return _instalacionactual;
  }
  set instalacionactual(String instalacionactual) {
    _instalacionactual=instalacionactual;
    notifyListeners();
  }

  List get datosanadirpersona {
    return _datosanadirpersona;
  }

  set datosanadirpersona(List datospersona) {
    _datosanadirpersona=datospersona;
    notifyListeners();
  }

  List get ultimoacceso {
    return _ultimoacceso;
  }

  set ultimoacceso(List ultimoacceso) {
    _ultimoacceso=ultimoacceso;
    notifyListeners();
  }
  List get personasactuales {
    return _personasactuales;
  }

  set personasactuales(List personasactuales){
    _personasactuales=personasactuales;
    notifyListeners();
  }

  bool get existeuuid{
    return _existeuuid;
  }

  set existeuuid(bool existeuuid){
    _existeuuid=existeuuid;
    notifyListeners();
  }

  bool get filtrado{
    return _filtrado;
  }

  set filtrado(bool filtrado){
    _filtrado=filtrado;
    notifyListeners();
  }

  String get startDate{
    return _startDate;
  }

  set startDate(String startDate){
    _startDate=startDate;
    notifyListeners();
  }

  String get endDate{
    return _endDate;
  }

  set endDate(String endDate){
    _endDate=endDate;
    notifyListeners();
  }

  int get resultadopost{
    return _resultadopost;
  }

  set resultadopost(int resultadopost){
    _resultadopost=resultadopost;
    notifyListeners();
  }

  bool get tablet{
    return _tablet;
  }

  set tablet(bool tablet){
    _tablet=tablet;
    notifyListeners();
  }

}