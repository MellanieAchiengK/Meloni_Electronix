/* $.get('http://localhost:5000/api/v1/country/155/cities', function (data) {
    data.forEach(element => {
        console.log(element)
    });
}); */

const localhost = "http://localhost:5000"
let id_country = ""


$(document).ready(function(){
    $("select.contry").change(function(){
      id_country = $(this).children("option:selected").val();
      const url = localhost + '/api/v1/country/' + id_country + '/cities';
      $.get(url, function(data){
        let html = ""
        data.forEach(element => {
            console.log(element['id']+" "+ element['name'])
            html = html + '<option value='+ element['id'] +'> '+ element['name'] +'</option>'
        });
        $("#citie option").replaceWith(' ')
        $("#citie").append(html)
      })
    }); 

    $('input:submit').prop('disabled', true); 
    //$('#password').val()
    //$('#confirm_password').val()
    //$('input[name=username]'). val();
    let first_name=''
    let last_name=''
    let pass1=''
    let pass2=''
    let email=''

    $('#first_name').change(function() {
      first_name = $('#first_name').val()
      console.log(first_name)
    })

    $('#last_name').change(function() {
      last_name = $('#last_name').val()
      console.log(last_name)
    })


    $('#password').change(function() {
      pass1 = $('#password').val()
      console.log(pass1)
    })

    $('#confirm_password').change(function() {
      pass2 = $('#confirm_password').val()
      if(pass1 != pass2)
      {
        console.log("les deux password sont diffeent")
        $("#confirm_password").css("background-color", "red");
        $("#password").css("background-color", "red");
      }
      else
      {
        $("#confirm_password").css("background-color", "white");
        $("#password").css("background-color", "white");
      }
    })

    $('#email').change(function() {
      email = $('#email').val()
      let userexiste = false
      if(((pass1 == pass2) && (pass1 !='')) && userexiste == false){
        console.log("condition verifier")
        $('input:submit').prop('disabled', false);
      }
      console.log(email)
    })
});
