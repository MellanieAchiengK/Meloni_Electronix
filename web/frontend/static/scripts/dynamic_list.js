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
});
