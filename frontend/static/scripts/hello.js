$(document).ready(function () {
    console.log("jQuery Activate")
    $.get('http://127.0.0.1:5000/api/v1/produit/', function (data) {
        let text =$('p').text()
        data.produit.forEach(element => {
            text = text + ' ' +element
            $('p').text(text)
        });     
    });
})