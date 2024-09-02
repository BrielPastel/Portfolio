<?php

    $nome = $_POST["nome"];
    $sobrenome = $_POST["sobrenome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];
    $dia = $_POST["dia"];
    
    $anolimite = date("M-d-Y", mktime(0, 0, 0, 12, 32, 1997));
    $mensagem = "";



    if (strlen($nome) < 1 || strlen($sobrenome) < 1 || strlen($email) < 1 || strlen($senha) < 1)
    {

        $mensagem = "Todos os campos devem ser preenchidos.";
        $json = json_encode($mensagem);
        echo date("M-d-Y", mktime(0, 0, 0, 12, 32, 1997));

    }
    else
    {
        if (strlen($senha) < 10)
        {
                
        $mensagem = "Usuário deve ter mais de 18 anos.";
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