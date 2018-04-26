<?php
   /*
    * 自動建立資料庫及資料表
    * 欄位:
    *       id      -> int (主鍵)
    *       data    -> int
    *       time    -> TIMESTAMP (CURRENT_TIMESTAMP)
    */
    //IP、帳號資訊
    $host = "172.32.16.42";
    $user = "iot";
    $pass = "iot";
    //資料庫資訊
    $databaseName = "lightdb";
    $tableName = "light";
    //連線資料庫伺服器
    $con = mysqli_connect($host,$user,$pass);
    //建立資料庫
    $sql = "CREATE DATABASE $databaseName";
    mysqli_query($con, $sql);
    //連結資料庫
    $dbs = mysqli_select_db($con, $databaseName);
    //建立資料表
    $sql = "CREATE TABLE ". 
           "`$tableName`( `id` INT NOT NULL AUTO_INCREMENT , ".           
           "`value` INT NOT NULL , ".
           "`status` INT NOT NULL , ".
           "`time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,".        
           " PRIMARY KEY (`id`)) ENGINE = InnoDB";
	mysqli_query($con, $sql);
?>