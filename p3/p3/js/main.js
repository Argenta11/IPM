function comprobariniciosesion(user, password){
  if(user==="" || password===""){
    document.getElementById("error").innerHTML="* Usuario o contraseña no válidos"
    document.getElementById("error").style.visibility='visible';
  }else {
    document.getElementById("error").style.visibility = "hidden";
    var spinner = document.getElementById("spinner");
    spinner.style.visibility = 'visible';
    spinner.style.opacity = '100';
    let entrada = `http://localhost:8080/api/rest/login?username=${user}&password=${password}`
    fetch(entrada,
      {
        method: 'POST',
        headers: {"x-hasura-admin-secret": "myadminsecretkey"}
      }
    ).then((response) => {
      return response.json();
    }).catch((error) => {
      var spinner = document.getElementById("spinner");
      spinner.style.visibility = 'hidden';
      spinner.style.opacity = '0';
      document.getElementById("error").innerHTML = "* Error en la BD. Vuelve a intentarlo"
      document.getElementById("error").style.visibility = 'visible';

    })
      .then(usuario => login(usuario, user));
  }
}

function login(usuario, user){

  if(usuario["users"].length === 0){
    var spinner= document.getElementById("spinner");
    spinner.style.visibility='hidden';
    spinner.style.opacity='0';
    document.getElementById("error").innerHTML = "* Usuario o contraseña no válidos"
    document.getElementById("error").style.visibility = 'visible';
  }else{
    localStorage.uuid=usuario['users'][0]['uuid'];
    localStorage.username=user;
    localStorage.name=usuario['users'][0]['name'];
    localStorage.surname=usuario['users'][0]['surname'];
    localStorage.email=usuario['users'][0]['email'];
    localStorage.telephone=usuario['users'][0]['phone'];
    if(usuario['users'][0]['is_vaccinated']){
      localStorage.vacunado="Si";
    }else{
      localStorage.vacunado="No";
    }
    ultimoacceso(usuario['users'][0]['uuid']);
    document.form.submit();
  }
}


function ultimoacceso(uuid){
  var spinner= document.getElementById("spinner");
  spinner.style.visibility='visible';
  spinner.style.opacity='100';
  fetch(`http://localhost:8080/api/rest/user_access_log/${uuid}`,
    {headers:{"x-hasura-admin-secret":"myadminsecretkey"}})
    .then(response => {
          response.json().then(accesos => guardaraccesos(accesos));
    })
    .catch((error) => {
      var spinner = document.getElementById("spinner");
      spinner.style.visibility = 'hidden';
      spinner.style.opacity = '0';
      document.getElementById("error").innerHTML = "* Error en la BD. Vuelve a intentarlo"
      document.getElementById("error").style.visibility = 'visible';
    })
}

function formatearfecha(fecha) {
  fechayhora=fecha.split('T');
  fecha2=fechayhora[0].split('-');
  hora=fechayhora[1].split('.');
  fechafinal=fecha2[2]+'-'+fecha2[1]+'-'+fecha2[0]+" a las "+hora[0];
  return fechafinal
}

function guardaraccesos(accesos){
  vin=0;
  vout=0;
  acceso_entrada=0;
  acceso_salida=0;
  for (let i = 0; i < accesos['access_log'].length; i++) {

    if (accesos['access_log'][i].type === "IN") {
      if(vin===1){
        localStorage.entrada="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lentrada= accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_entrada++;
      }
      if(vin===2){
        localStorage.entrada2="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lentrada2= accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_entrada++;
      }
      if(vin===3){
        localStorage.entrada3="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lentrada3=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_entrada++;
      }
      if(vin===4){
        localStorage.entrada4="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lentrada4=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_entrada++;
      }
      if(vin===5){
        localStorage.entrada5="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lentrada5=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_entrada++;
      }
      vin++;
    } else {
      if(vout===1){
        localStorage.salida="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lsalida=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_salida++;
      }
      if(vout===2){
        localStorage.salida2="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lsalida2=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_salida++;
      }
      if(vout===3){
        localStorage.salida3="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lsalida3=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_salida++;
      }
      if(vout===4){
        localStorage.salida4="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lsalida4=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_salida++;
      }
      if(vout===5){
        localStorage.salida5="El día "+formatearfecha(accesos['access_log'][i].timestamp.toString());
        localStorage.lsalida5=accesos['access_log'][i]['facility'].name+" ("+accesos['access_log'][i]['facility'].id.toString()+")";
        acceso_salida++;
      }
      vout++;
    }
  }
  localStorage.nentrada=acceso_entrada;
  localStorage.nsalida=acceso_salida;
}

function formatoemail(email){
  if(!email.includes('@')){
    return false;
  }
  return email.includes('.');
}

function vacunadocorrecto(vacunado){
  return !(vacunado !== "S" && vacunado !== "N");
}

function telefonocorrecto(telefono){
  var valoresAceptados = /^[0-9]+$/;
  if(telefono.includes('-')){
    numeros=telefono.split('-');
    if(numeros.length!==3){
      return 0;
    }else{

      for(let i=0; i<3;i++)
      {
        if (!numeros[i].match(valoresAceptados))
        {
          return 0;
        }
      }
    }
    return 1;
  }else{
    if(telefono.length!==9){
      return 0;
    }else{
      if(telefono.match(valoresAceptados)){
        return 2;
      }else{
        return 0;
      }
    }
  }
}

function volveratras(){
  var resultado = window.confirm('¿Estas seguro de que quieres volver atrás? Se cerrará la sesión');
  if (resultado === true) {
    history.back()
  }else{

  }
}

function seguroregistrar(formData){
  var resultado = window.confirm('¿Estas seguro de que quieres registrar estos datos?');
  if (resultado === true) {
    hacerpost(formData);
  }else{
    var spinner= document.getElementById("spinner");
    spinner.style.visibility='hidden';
    spinner.style.opacity='0';
  }
}

function ponerlinearoja(email,nombre,apellido, telefono, login,pass, pass2, vacunado){

  if (email === "") {document.getElementById("email").style.borderColor="red";}
  if(nombre === ""){document.getElementById("fname").style.borderColor="red";}
  if(apellido === ""){document.getElementById("lname").style.borderColor="red";}
  if(vacunado === ""){document.getElementById("vacunado").style.borderColor="red";}
  if(login === ""){document.getElementById("login").style.borderColor="red";}
  if(pass === "") {document.getElementById("password").style.borderColor="red";}
  if(pass2 === ""){document.getElementById("rpassword").style.borderColor="red";}
  if(telefono === ""){document.getElementById("tfn").style.borderColor="red";}

}
function volverasucolor(){
  document.getElementById("email").style.borderColor="white";
  document.getElementById("fname").style.borderColor="white";
  document.getElementById("lname").style.borderColor="white";
  document.getElementById("vacunado").style.borderColor="white";
  document.getElementById("login").style.borderColor="white";
  document.getElementById("password").style.borderColor="white";
  document.getElementById("rpassword").style.borderColor="white";
  document.getElementById("tfn").style.borderColor="white";
}

function registrar(email,nombre,apellido, telefono, login,pass, pass2, vacunado) {
  let tf;
  volverasucolor();
  document.getElementById("error").style.visibility="hidden";
  var spinner= document.getElementById("spinner");
  spinner.style.visibility='visible';
  spinner.style.opacity='100';
  if (email === "" || nombre === "" || apellido === "" || vacunado === "" || login === "" || pass === "" || pass2 === "" || telefono === "") {
    var spinner= document.getElementById("spinner");
    spinner.style.visibility='hidden';
    spinner.style.opacity='0';
    ponerlinearoja(email,nombre,apellido, telefono, login,pass, pass2, vacunado);
    document.getElementById("error").innerHTML="* Debes introducir todos los datos"
    document.getElementById("error").style.visibility='visible';

  } else {
    if (telefonocorrecto(telefono) === 0) {
      var spinner= document.getElementById("spinner");
      spinner.style.visibility='hidden';
      spinner.style.opacity='0';
      document.getElementById("tfn").style.borderColor="red";
      document.getElementById("error").innerHTML="* El formato del teléfono no es válido"
      document.getElementById("error").style.visibility='visible';
    } else {
      if (telefonocorrecto(telefono) === 1) {
        tf = telefono;
      } else {
        tf = telefono[0] + telefono[1] + telefono[2] + '-' + telefono[3] + + telefono[4] + telefono[5] + '-' + telefono[6] + telefono[7] + telefono[8];
      }
      if (!formatoemail(email)) {
        var spinner= document.getElementById("spinner");
        spinner.style.visibility='hidden';
        spinner.style.opacity='0';
        document.getElementById("email").style.borderColor="red";
        document.getElementById("error").innerHTML="* El formato del email no es válido"
        document.getElementById("error").style.visibility='visible';
      } else {

        if (pass !== pass2) {
          var spinner= document.getElementById("spinner");
          spinner.style.visibility='hidden';
          spinner.style.opacity='0';
          document.getElementById("password").style.borderColor="red";
          document.getElementById("rpassword").style.borderColor="red";
          document.getElementById("error").innerHTML="* Las dos contraseñas deben ser iguales"
          document.getElementById("error").style.visibility='visible';
        } else {
          if (!vacunadocorrecto(vacunado)) {
            var spinner= document.getElementById("spinner");
            spinner.style.visibility='hidden';
            spinner.style.opacity='0';
            document.getElementById("vacunado").style.borderColor="red";
            document.getElementById("error").innerHTML="* Los datos válidos son S si estás vacunado y N si no lo estás"
            document.getElementById("error").style.visibility='visible';

          } else {
            var formData = new FormData();
            formData.append("username", login);
            formData.append("password", pass);
            formData.append("name", nombre);
            formData.append("surname", apellido);
            formData.append("phone", tf);
            formData.append("email", email);
            if (vacunado === 'S') {
              formData.append("is_vaccinated", true);
            } else {
              formData.append("is_vaccinated", false);
            }
            seguroregistrar(formData);
          }
        }
      }
    }
  }

}

function hacerpost(formData){
  fetch("http://localhost:8080/api/rest/user",{
    method: 'POST',
    body: formData,
    headers: {"x-hasura-admin-secret":"myadminsecretkey"}}
  )
    .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      var spinner= document.getElementById("spinner");
      spinner.style.visibility='hidden';
      spinner.style.opacity='0';
      throw new Error('Something went wrong');

    }
  })
    .then((responseJson) => {
      var spinner= document.getElementById("spinner");
      spinner.style.visibility='hidden';
      spinner.style.opacity='0';
      alert("Se ha añadido correctamente");

      // Do something with the response
    }).catch((error) => {
    var spinner = document.getElementById("spinner");
    spinner.style.visibility = 'hidden';
    spinner.style.opacity = '0';
    document.getElementById("error").innerHTML = "* Error en la BD. Vuelve a intentarlo"
    document.getElementById("error").style.visibility = 'visible';
  })
}
