#!/usr/bin/php
<?php

/**
 * The Biologist Problem
 * @author Imanol Urra (index02@gmail.com)
 * 
 * The important thing is not to stop questioning. Curiosity has its own reason for existing.
 *  - Albert Einstein
 *
 */

foreach (file( 'php://stdin' ) as $line) {
    $line = explode(" ", $line);

    $sequence1 = $line[0];
    $sequence2 = $line[1];

    print strlcs( $sequence1, $sequence2 )."\n\r";
}

function strlcs($str1, $str2){
    $str1Len = strlen($str1);
    $str2Len = strlen($str2);
    $ret = array();
 
    if( $str1Len == 0 || $str2Len == 0 ) return $ret; //no similarities
 
    $CSL = array(); //Common Sequence Length array
    $intLargestSize = 0;

    for ($i=0; $i<$str1Len; $i++) {
        $CSL[$i] = array();
        for($j=0; $j<$str2Len; $j++) $CSL[$i][$j] = 0;
    }
 
    for ( $i=0; $i<$str1Len; $i++ ) {
        for ($j=0; $j<$str2Len; $j++) {
            if ( $str1[$i] == $str2[$j] ) {
                if ($i == 0 || $j == 0) {
                    $CSL[$i][$j] = 1; 
                } else {
                    $CSL[$i][$j] = $CSL[$i-1][$j-1] + 1; 
                    
                    if ( $CSL[$i][$j] > $intLargestSize ) {
                        $intLargestSize = $CSL[$i][$j]; 
                        $ret = array();
                    }
                    
                    if( $CSL[$i][$j] == $intLargestSize ) $ret[] = substr($str1, $i-$intLargestSize+1, $intLargestSize);
                }
            }
        }
    }
        //return the list of matches
    return $ret[0];
}

?>