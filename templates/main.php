<?php
echo "WTF!!";
$fp = fopen('textfile.txt', 'a+');
fwrite($fp, "efsfsefsefesfs");
fclose($fp);
echo "WTF2!!";
?>
