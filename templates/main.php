<?php
$ress=$_POST['res'];
$fp = fopen('textfile.txt', 'a+');

$file = fwrite($fp, $ress);
$file = fwrite($fp, "\n");


fclose($fp);
?>
