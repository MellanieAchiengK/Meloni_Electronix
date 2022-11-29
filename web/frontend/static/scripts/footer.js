const createFooter = () => {
    let footer = document.querySelector('footer');

    footer.innerHTML = `
    <div class="footer-social-container">
        <div>
           <a href="#" class="fa fa-phone"></a>
           <a href="#" class="fa fa-envelope"></a>
           <a href="#" class="fa fa-whatsapp"></a>
           <a href="#" class="fa fa-instagram"></a>
    </div>
    `;
}

createFooter();