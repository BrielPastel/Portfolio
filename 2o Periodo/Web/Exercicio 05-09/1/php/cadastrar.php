<?php

    $nome = $_POST["nome"];
    $sobrenome = $_POST["sobrenome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];
    $mensagem = "";

    if (strlen($nome) < 1 || strlen($sobrenome) < 1 || strlen($email) < 1 || strlen($senha) < 1)
    {

        $mensagem = "Todos os campos devem ser preenchidos.";
        $json = json_encode($mensagem);
        echo $json;

    }
    else
    {
        if (strlen($senha) < 10)
        {
                
        $mensagem = "A senha não possui caracteres suficientes.";
        $json = json_encode($mensagem);
        echo $json;

        }
        else
        {
            $mensagem = "Gravado com sucesso.";
            $json = json_encode($mensagem);
            echo $json;
        }
    }




?>