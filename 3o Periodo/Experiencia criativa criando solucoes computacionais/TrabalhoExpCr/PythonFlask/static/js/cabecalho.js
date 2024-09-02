function abrirmenu() {
    var menu = document.querySelector('.menu-lateral');
    if (menu.style.right === '0px') {
        menu.style.right = '-250px'; // Esconde o menu
    } else {
        menu.style.right = '0px'; // Mostra o menu
    }
}
