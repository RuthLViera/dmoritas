   $(document).ready(function(){
      $("#btnSubmit").click(function(){
        error = 0;
        /* Valido el campo Nombre que no este Vacio*/
        if ($("#txtName").val()=='') {
            alert('El campo Nombre no puede estar vacio.');
            error++;
        }

        if ($("#txtName").val().length<3) {
            alert('El campo Nombre tiene que ser superior a 3 letras.');
            error++;            
        }

        if ($("#txtName").val()*1>0) {
            alert('El campo Nombre no puede contener numeros.');
            error++;
        }
        /*Fin validacion de campo nombre*/
        /* Valido el campo Apellido que no este Vacio*/
        if ($("#txtApellido").val()=='') {
            alert('El campo Apellido no puede estar vacio.');
            error++;
        }

        if ($("#txtApellido").val().length<4) {
            alert('El campo Apellido tiene que ser superior a 4 letras.');            
            error++;
        }

        if ($("#txtApellido").val()*1>0) {
            alert('El campo Apellido no puede contener numeros.');
            error++;
        }
        /*Fin validacion de campo Apellido*/
        /* Valido el campo Telefono que no este Vacio*/
        if ($("#txtPhone").val()=='') {
            alert('El campo Telefono no puede estar vacio.');
            error++;
        }

        if ($("#txtPhone").val().length==11) {
            alert('El campo Telefono tiene que ser de 11 numeros.');            
            error++;
        }

        /*Fin validacion de campo Telefono*/
        /* Valido el campo Mensaje que no este Vacio*/
        if ($("#txtMsg").val()=='') {
            alert('El campo Mensaje no puede estar vacio.');
            error++;
        }

        if ($("#txtMsg").val().length<4) {
            alert('El campo Mensaje tiene que ser superior a 4 letras.');            
            error++;
        }
        /*Fin validacion de campo Mensaje*/

        if (error==0) {
            $("#contact").submit();
        }else
        {
            return false;
        }
      })
    });
