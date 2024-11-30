<?php
session_start();
            if (isset($_SESSION['user'])) {
                
            } else {
                header("Location: ../index.php");
                exit();
            }
            ?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        Inicio|PHP Proyecto UTD
    </title>
    <link rel="stylesheet" href="../css/estilos.css" type="text/css">
</head>
<body>
    <header>
        <div id="logotipo">
            <img src="../img/logophp.png" alt="Imagen Django" title="Django">
            <h1>PHP Proyecto Web</h1>
        </div>
    </header>
    <nav>
        <ul>
                <li><a href="../index.php" >Inicio</a></li>
                <li><a href="mision.php">Mision</a></li>
                <li><a href="vision.php">Vision</a></li>
                <li><a href="acercade.php">Acerca de</a></li>
                <li><a href="registrar_articulo.php">Registrar articulos</a></li>
                <li><a href="mostrar_articulos.php">Articulos</a></li>
                <li><a href="mostrar_categorias.php">Categorias</a></li>
                <li><a href="cerrar_sesion.php">Cerrar sesión</a></li>
        </ul>
    </nav>
    <section id="content">
       <div class="box">
            <h1>Acerca de Nosotros</h1>
            <hr>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae perspiciatis assumenda sint dignissimos qui voluptates nobis! Odit nisi nemo vero eius porro nobis obcaecati est, eveniet alias voluptates, aliquam atque.</p>
       </div>
    </section>
    <footer>
        <p>PHP con Manuel Hernández | &copy; 2024 29/11/2024 </p>
    </footer>
</body>
</html>