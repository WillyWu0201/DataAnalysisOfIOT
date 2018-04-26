<?php

    $host = "172.32.16.42";
    $user = "iot";
    $pass = "iot";

    //資料庫資訊
    $databaseName = "lightdb";
    $tableName = "light";


    //連結資料庫
    $con = mysqli_connect($host,$user,$pass);
    $dbs = mysqli_select_db($con, $databaseName);


    for($i=0;$i<100;$i++) {
		$sql = "INSERT INTO $tableName (value,status) VALUES (".rand(0,1023).",".rand(0,1).")";
		mysqli_query($con, $sql);
    }
?>