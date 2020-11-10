<?php
$ress=$_POST['res'];
//$fp = fopen('textfile.txt', 'a+');
$fp = fopen("webdictionary.txt", "r") or die("Unable to open file!");

$file = fwrite($fp, $ress);
$file = fwrite($fp, "\n");


fclose($fp);
?>
