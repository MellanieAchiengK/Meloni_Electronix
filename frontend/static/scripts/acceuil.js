/**
 * retrieve the list of item categories and display them
 */

const HOST = 'http://127.0.0.1:5000'
$(document).ready(function () {
    
    $.get( HOST + "/api/v1/categorie", function( data ) {
        let code=''
        data.categorie.forEach(element => {
            code += '<img src="'+element.src+'"title="'+element.title+'">'
        });
        $('#store').html(code) 
    });
})