const createFooter = () => {
    let footer = document.querySelector('footer');

    footer.innerHTML = `
    <div class="footer-contact-container">
        <div>
           <p><image src="../static/images/phone-call.png">0712345678</p>
           <p><image src="../static/images/email.png">melonielectronix@gmail.com</p>
           <p><image src="../static/images/whatsapp.png">0712345678</p>
           <p><image src="../static/images/instagram.png">@melonielectronix</p> 
    </div>
    <p class="footer-credit">Quality and Affordable</p>
    `;
}

createFooter();