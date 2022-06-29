import 'dart:convert';
import 'package:http/http.dart' as http;

class Model {
  late List<List<String>> lista=[];
  late bool existe=false;

  Future<List<String>> getInstalaciones() async { // Función que devuelve la lista de instalaciones
    List<String> facilities = [];
    var url = Uri.parse("http://10.0.2.2:8080/api/rest/facilities");
    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);
    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      facilities = ListaInstalaciones(jsonData);
    } else {
      facilities.add("Error en la BD: "+response.statusCode.toString());
    }
    return facilities;
  }

  List<String> ListaInstalaciones(jsonData) { // Formatea la lista de instalaciones
    List<String> facilities = [];
    // Para cada instalación, la guardamos con el formato Nombre (id)
    for (int a = 0; a < jsonData['facilities'].length; a++) {
      String fac = jsonData['facilities'][a]['name'];
      fac = fac + " (" + jsonData['facilities'][a]['id'].toString() + ")";
      facilities.add(fac);
    }

    return facilities;
  }

  Future<List<List<String>>> getAccesos(facility) async { // Función que devuelve la lista de accesos
    List<List<String>> accesos = [];
    var url = Uri.parse(
        "http://10.0.2.2:8080/api/rest/facility_access_log/" + facility);

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);

    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      accesos = ListaAccesos(jsonData);
    } else {
      // accesos.add("Error en la BD: "+response.statusCode.toString());
    }
    return accesos;
  }

  Future<List<List<String>>> getAccesosFiltrados(facility,String startDate, String endDate) async { // Función que devuelve la lista de accesos filtrada por fechas
    List<List<String>> accesos = [];
    var url =
    Uri.parse( "http://10.0.2.2:8080/api/rest/facility_access_log/" + facility+"/daterange");
    var data = {
      "startdate": startDate,
      "enddate": endDate,
    };

    var request = http.Request("GET", url)
      ..body = json.encode(data)
      ..headers.addAll({"x-hasura-admin-secret": "myadminsecretkey"});

    var client = http.Client();
    var response = client.send(request).then( (streamedResponse) {
      streamedResponse.stream.bytesToString().then((dataAsString) {
        final jsonData = jsonDecode(dataAsString);
        lista = ListaAccesos(jsonData);
      });
    }).whenComplete(() {
      client.close();
    });

    return lista;

  }

  Future<int> getnumAccesos(facility) async { // Función que devuelve el número de accesos
    List accesos = [];
    var url = Uri.parse(
        "http://10.0.2.2:8080/api/rest/facility_access_log/" + facility);

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);

    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      accesos = ListaAccesos(jsonData);
    } else {
    }
    return accesos.length;
  }

  Future<List> getAccesosTotales() async {  // Función que devuelve los accesos totales (para los datos)
    List accesos = [];
    var url = Uri.parse("http://10.0.2.2:8080/api/rest/facility_access_log");

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);

    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      accesos = ListaAccesos(jsonData);
    } else {
      accesos.add("Error en la BD: "+response.statusCode.toString());
    }
    return accesos;
  }

  Future<List> getAccesosActuales(facility) async { // Función que devuelve los datos actuales (para los datos)
    List accesos = [];
    var url = Uri.parse(
        "http://10.0.2.2:8080/api/rest/facility_access_log/" + facility);

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);

    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      accesos = ListaAccesosActuales(jsonData);
    } else {
      accesos.add("Error en la BD: "+response.statusCode.toString());
    }
    return accesos;
  }

  List ListaAccesosActuales(jsonData) { // Función que formatea la lista de accesos actuales
    List access = [];
    for (int a = jsonData['access_log'].length-1; a>=0; a--) { // Recorremos la lista
      int va = 0;
      if (jsonData['access_log'][a]['type'] == "IN") {  // Si es de tipo IN
        List x = [];

        for (int b = a; b >=0; b--) {// Buscamos un OUT desde su posición para el mismo uuid

          if (jsonData['access_log'][a]['user']['uuid'] ==
              jsonData['access_log'][b]['user']['uuid'] &&
              jsonData['access_log'][b]['type'] == "OUT") {
            va++; // Si lo encontramos sumamos a la variable
          }

          if (va == 0 && b == 0) {  // Si no hemos encontrado ningún out, guardamos
            x.add(jsonData['access_log'][a]['user']['name'] + " " +
                jsonData['access_log'][a]['user']['surname']);
            x.add(jsonData['access_log'][a]['user']['uuid']);
            x.add(jsonData['access_log'][a]['timestamp'].toString());
            x.add(jsonData['access_log'][a]['temperature'].toString());
            access.add(x);
          }
        }
      }
    }
    return access;
  }

  List<List<String>> ListaAccesos(jsonData) { // Función que guarda los datos de la lista de accesos en el formato adecuado
    List<List<String>> access = [];
    for(int a=jsonData['access_log'].length-1;a>=0;a--){
      int va = 0;
      if (jsonData['access_log'][a]['type'] == "IN") {
        List<String> x = [];
        x.add(jsonData['access_log'][a]['user']['name'] + " " +
            jsonData['access_log'][a]['user']['surname']);
        x.add(jsonData['access_log'][a]['user']['uuid']);
        x.add(jsonData['access_log'][a]['timestamp'].toString());
        x.add(jsonData['access_log'][a]['temperature'].toString());
        for (int b = 0; b >= 0; b--) {

          if (va == 0) {
            if (jsonData['access_log'][a]['user']['uuid'] ==
                jsonData['access_log'][b]['user']['uuid']){
              if (jsonData['access_log'][b]['type'] == "OUT") {
                x.add(jsonData['access_log'][b]['timestamp'].toString());
                x.add(jsonData['access_log'][b]['temperature'].toString());
                va++;
              }
          }
          }
          if (va == 0 && b == 0) { // Si solo hay entrada, guardamos los datos de salida como 'No'
            x.add('No');
            x.add('No');
          }
        }
        access.add(x);
      }
    }
    return access;
  }

  Future<int> anadirAcceso(nuevoacceso) async { // Función que añade un acceso a la BD
    var data = {
      "user_id": nuevoacceso[0],
      "facility_id": int.parse(nuevoacceso[1]),
      "timestamp": nuevoacceso[2],
      "type": nuevoacceso[3],
      "temperature": nuevoacceso[4]
    };
    var url = Uri.parse("http://10.0.2.2:8080/api/rest/access_log");

    var response = await http.post(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },
      body: json.encode(data),
    );
    return response.statusCode;
  }

  Future <List> getUltimoAcceso(uuid, localizacion) async { // Función que encuentra el último acceso de un user
    List result = [];
    var url = Uri.parse(
        "http://10.0.2.2:8080/api/rest/facility_access_log/" + localizacion);

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);

    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      result = UltimoResultado(jsonData, uuid);
    } else {
      result.add("Error en la BD: " + response.statusCode.toString());
    }
    return result;
  }

  List UltimoResultado(jsonData, uuid) {  // Función auxiliar que guarda el último resultado
    List access = [];
    int va = 0;
    for (int a = 0; a < jsonData['access_log'].length - 1; a++) {  // Recorremos los datos a la inversa
      if (jsonData['access_log'][a]['user']['uuid'] == uuid && va == 0) { // Si encontramos al usuario y no entramos en el if antes lo almacenamos
        access.add(jsonData['access_log'][a]['timestamp'].toString());
        access.add(jsonData['access_log'][a]['temperature'].toString());
        access.add(jsonData['access_log'][a]['type'].toString());
        va++;
      }
    }
    if (va == 0) {  // Si nunca entro guardamos como OUT para que la siguiente sea IN
      for(int x = 0; x<6;x++){
      access.add('OUT');
      }
    }
    return access;
  }


  Future<List> getNombreApellido(uuid, fecha) async {  // Función a la que le pasas un uuid y te devuelve el nombre y el apellido
    List result = [];
    var url = Uri.parse("http://10.0.2.2:8080/api/rest/users/" + uuid);
    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);
    if (response.statusCode == 200) {
      String body = utf8.decode(response.bodyBytes);
      final jsonData = jsonDecode(body);
      result = NombreApellido(jsonData, fecha);
    } else {
      result.add("Error en la BD: "+response.statusCode.toString());
    }
    return result;
  }

  List NombreApellido(jsonData, fecha) { // Función auxiliar que almacena uuid, nombre y apellido
    List resultado = [];
    List partimos = [];
    resultado.add(jsonData['users'][0]['uuid'].toString());
    resultado.add(jsonData['users'][0]['name']);
    resultado.add(jsonData['users'][0]['surname']);
    if(fecha=='NO') {
      partimos = DateTime.now().toString().split(' ');

    }else{
      List partimosaux = fecha.split(' ');
      List partimosaux2 = partimosaux[0].split('-');
      String partimos1=partimosaux2[2]+'-'+partimosaux2[1]+'-'+partimosaux2[0];
      String partimos2=partimosaux[1]+':00.000000';
      partimos.add(partimos1);
      partimos.add(partimos2);
    }
    String anadir = partimos[0] + 'T' + partimos[1] + 'Z';
    resultado.add(anadir);
    return resultado;
  }

  Future <bool> existeuuid(uuid) async{ // Función que comprueba si existe un uuid en la BD

    var url = Uri.parse("http://10.0.2.2:8080/api/rest/users/"+uuid);

    var response = await http.get(
      url,
      headers: {
        "x-hasura-admin-secret": "myadminsecretkey",
      },);
    if (response.statusCode == 200) {
    if(response.body=='{"users":[]}'){
      existe = false;
      return false;
    }else{
      existe = true;
      return true;
    }}else{
      return false;
    }
  }
}