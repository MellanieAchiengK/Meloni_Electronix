/**
 * retrieve the list of item categories and display them
 */

const HOST = 'http://127.0.0.1:5000'
$(document).ready(function () {
    let id=parseInt($('#store').text())
    $.get( HOST + "/api/v1/categorie/"+id, function( data ) {
        let code = ''
        data.listecategorie.forEach(element => {
            code += "<a href='/article/"+id+"'> <img src="+element.src+" alt='" + element.title + "' title='" + element.title + "' /> </a>"
        });
        console.log(id)
        $('#store').html(code) 
    });
})