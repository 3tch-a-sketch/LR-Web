
<?php
if($_GET['recipient'] == "15matthewmiles@catmosecollege.com")
{
  header("location: https://www.youtube.com/watch?v=dQw4w9WgXcQ");
}
?>
<!DOCTYPE html>
<head>
  <link rel="stylesheet" type="text/css" href="theme.css">

  <!meta http-equiv="refresh" content="60"> <! DEV only >

  <title>LR-Web Client: Email</title>
</head>
<body>

  <nav class="floating-menu">
    <a href="./index.html" class="buttonw3">LR-Web User Page</a>
    <a href="./send.html" class="buttonw3">Send an e-mail</a>
    <a href="./help.html" class="buttonw3">HELP!</a>
  </nav>
  <br><br><br><br><br><br>
  <p>
    <?php
        $field = $_GET;
        echo("OUTPUTTING");
        //echo("<br>".$field." - ".$value);
        echo("<br>"$_GET['recipient']);
     ?>
    Complete!
  </p>

</body>
