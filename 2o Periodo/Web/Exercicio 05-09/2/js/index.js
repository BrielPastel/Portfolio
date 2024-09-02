
async function obter()
{
    var form = document.getElementById('cadastro');
    var dados = new FormData(form);

    var promise = await fetch("php/cadastrar.php", {
        method: "POST",
        body: dados
    });

    var resposta = await promise.json();

    alert(resposta);

}