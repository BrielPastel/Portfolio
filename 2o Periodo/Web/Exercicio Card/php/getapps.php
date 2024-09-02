<?php

    $con = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");

    $resultado = mysqli_query($con, "SELECT * FROM aplicativo");

    $dados = array();

    while($registro = mysqli_fetch_assoc($resultado)){
        array_push($dados, $registro);
    }
    
    $json = json_encode($dados);
    echo $json;





?>