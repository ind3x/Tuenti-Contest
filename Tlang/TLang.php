#!/usr/bin/php
<?php
/*
 * TLang
 *
 * @author Imanol Urra (index02@gmail.com)
 * 
 */

foreach( file( 'php://stdin' ) as $line ) {
    parser($line);   
}

function parser($line) {
    $split = preg_split("/[\^$]/", $line);
    
    foreach ($split as $split) {
        preg_match_all( '/[\d-]+/', $split, $matches );
    
        if ( count($matches[0]) ) {
            switch ($split[0]) {
                case '#':
                    $result = 1;
                    foreach($matches[0] as $number) $result *= $number;

                    break;
                case '=':
                    $result = 0;
                    foreach($matches[0] as $number) $result += $number;

                    break;
                case '@':
                    $result = 0;
                    foreach($matches[0] as $key => $number) {
                        if (count($matches[0]) == 1) {
                            $result -= $number;
                        } else {
                            if ($key == 0) {
                                $result += $number;
                            } else {
                                $result -= $number;
                            }
                        }
                    }

                    break;
            }
        }
        
        $line = str_replace('^'.$split.'$', $result, $line);
    }
    
    ( strpos($line, "$") !== false ) ? parser($line) : print($line);
}
?>