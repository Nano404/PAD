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

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Capture the flag</title>
        <meta name="description" content="Capture the flag">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="ChangePSWPHP.css">
    </head>
    <body>
        <div class="grid-container">
            <div class="nav-bar">
                <span id="left">IC101-C5</span>
                <span id="right">Nino, Menno, Naoufal, Thomas, Tirez</span>
            </div>
            <div class="Main-page">
                $result = mysqli_query(con,"SELECT * FROM firstName");
                echo "<table border='1'>
                <tr>
                <th>firstName</th>
                </tr>";

                while($row = mysqli_fetch_array($result))
                {
                echo "<tr>";
                echo "<td>" . $row['firstName'] . "</td>";
                echo "</tr>";
                }
                echo "</table>";

            </div>
        </div>
    </body>
</html>

mysqli_close($con);
?>