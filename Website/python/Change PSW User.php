<?php
$servername = "localhost";
$username = "CTF";
$password = "Welkom123";
$database = "CTF";

$con=mysqli_connect($servername,$username, $password);

if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

?>
