<?php
$S = fgets(STDIN);


for($i = 0; strlen($S)-1>$i; $i++){
  echo substr($S, $i, 1)."\n";
};

?>