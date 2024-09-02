<?php

    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];
    $titulo = $_POST["titulo"];
    $duracao = $_POST["duracao"];
    $compositor = $_POST["compositor"];
    $album = $_POST["album"];

    $con = mysqli_connect("localhost:3306", "root", "PUC@1234", "pucpr");
    $query = "INSERT INTO estudante (nome, email, senha) VALUES ('$nome', '$email', '$senha')";
    $query2 = "INSERT INTO musica (titulo, duracao, compositor, album) VALUES ('$titulo', $duracao, '$compositor', '$album')";

    mysqli_query($con, $query);
    mysqli_query($con, $query2);

?>