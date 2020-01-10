
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
    <a href="./inbox.html" class="buttonw3">Inbox</a>
  </nav>
  <br><br><br><br>
  <p>
    Email sent!
  </p>
  <p>
    &ltoutput&gt
    <?php
        $email = $_GET['recipient'];
        $subject = $_GET['subject'];
        $body = $_GET['body'];
        $password = $_GET['password']; // TODO: get each slave unit to use an induvidual client id
        echo("<br />EMAIL: ".$email);
        echo("<br />SUBJECT: ".$subject);
        echo("<br />BODY: ".$body);
        echo("<br />SECRET PASSWORD: ".$password);
        // TODO: send to Python
        $command = escapeshellcmd('python3 ./python/send_to_master.py -r "'.$email.'" -s "'.$subject.'" -b"'.$body.'"');
        $output = shell_exec($command);
        shell_exec($command);
        echo($output);

     ?>
    <br />
    &lt/output&gt
  </p>

</body>
