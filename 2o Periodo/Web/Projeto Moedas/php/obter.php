<?php

    $moeda = $_POST["moeda"];
    $mensagem = "";

    switch($moeda){
        case "EUA" : $mensagem = "dólar americano"; break;
        case "BR" : $mensagem = "real brasileiro"; break;
        case "ARG" : $mensagem = "peso argentino"; break;
        default: $mensagem = "não funcionou";
    }

    $json = json_encode($mensagem);

    echo $json;



?>