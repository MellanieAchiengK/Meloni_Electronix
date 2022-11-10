/**
 * retrieve the list of item categories and display them
 */

const HOST = 'http://127.0.0.1:5000'
$(document).ready(function () {
    
    $.get( HOST + "/api/v1/categorie", function( data ) {
        let code=''
        data.categorie.forEach(element => {
            code += "<a href='/categorie/"+element.id+"'> <img src="+element.src+" alt='" + element.title + "' title='" + element.title + "' /> </a>"
        });
        $('#store').html(code) 
    });
})