#!/usr/bin/php
<?php
/*
 * Emirp
 *
 * @author Imanol Urra (index02@gmail.com)
 * 
 */

foreach( file( 'php://stdin' ) as $line ) {
    $result = 0;
    
    for ($i = 12; $i <= $line; $i++ ) {
        if ( is_prime( $i ) == true && is_prime( strrev($i) ) == true && $i != strrev($i) ) {
            $result += $i;
        }
    }

    print($result."\n\r");
}

function is_prime($number) {
    if ( $number % 2 == 0 ) {
        return false;
    }

    for ($i = 3; $i <= floor(sqrt($number)); $i++) {
        if ($number % $i == 0) return false;
    }
    
    return true;
}
?>