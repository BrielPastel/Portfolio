
window.onload = async function () {
    var resultado = await fetch("php/getapps.php", {
        method: "GET"
    });

    var dados = await resultado.json();

    for( var i = 0 ; i < dados.length ; i++ ){

        var conteudo = 
    `<div class="card">
        <div class="logo">
            <img src="https://about.twitter.com/content/dam/about-twitter/x/brand-toolkit/logo-black.png.twimg.1920.png" width="40px" />
        </div>
        <div class="titulo">
            ${dados[i].nome}
        </div>
        <div class="descricao">
            ${dados[i].descricao}
        </div>
        <div class="acao">
            <button class="btn"> READ MORE </button>
        </div>
    </div>`;

    document.getElementById('aplicativos').innerHTML += conteudo;
    }
}
