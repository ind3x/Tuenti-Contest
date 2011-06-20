#!/usr/bin/php
<?php
foreach( file( 'php://stdin' ) as $line ) {
    preg_match_all( '/[\d-]+/', $line, $match );
    
    $add = 0;
    foreach ( $match[0] as $number ) $add = bcadd( $add, $number );
    
    echo $add."\r\n";
}
?>