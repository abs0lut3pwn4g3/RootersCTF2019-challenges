<?php
$link = mysqli_connect("database", "root", "password", "sql_injection");

if (!$link) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}


if(isset($_GET['search'])){
	$search = $_GET['search'];
	if(preg_match('/(union|sleep|\'|\"| or |-|benchmark)/i', $search)){
		exit();
	}
	else{
		$query = "SELECT * FROM users WHERE uniqueid=$search";
		$result=mysqli_query($link,$query) or die(mysqli_error($link));
		$count = mysqli_num_rows($result);
		if(mysqli_num_rows($result) === 1){
			while($row = mysqli_fetch_array($result)){
                        	$pass = $row['uniqueid'];
			}
			header("Location: https://babyweb.rootersctf.in/flag0flag0123456789.php?id=".$pass);
			die();
		}

		echo $query;
	}
}

mysqli_close($link);
?>

<!doctype html>
<html lang="en">
  <head>
<style>
.my {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

.my-l {
  float: left;
}

.my-l a {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.my-l a:hover {
  background-color: #111;
}

.active {
  background-color: red;
}
</style>
  </head>
  <body>
    <div class='container'>
        <div class='row'>
            <div class='col-6 mx-auto'>
<h1>This page is protected by super strong password with 18 digit numeric characters</h1>
<p>banned words and characters <b>UNION SLEEP ' " OR - BENCHMARK</b></p>
	<form action ="index.php" method = "get">
	  Enter unique id: 
          <input name="search" type="text" size="30" placeholder=""/>
          <input type="submit" value="Search"/>
          </form>
		<br />
		<br />
            </div>
        </div>
    </div>

</body>
</html>

