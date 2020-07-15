<?php
$i1 = fgets(STDIN);
$i2 = fgets(STDIN);
$i3 = fgets(STDIN);


echo max(strlen($i1),strlen($i2),strlen($i3))-1;
?>