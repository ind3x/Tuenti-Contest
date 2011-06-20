#!/usr/bin/php
<?php
/*
 * The Tile Game
 * @author Imanol Urra (index02@gmail.com)
 * 
 * If you fall seven times, get up eight.
 *  - Chinese proverb
 *
 * Patience is a bitter root tree, but bears very sweet fruit.
 *  - Persian proverb
 */

foreach (file( 'php://stdin' ) as $line) {
    $line = explode(" ", $line);

    $set1 = $line[0];
    $set2 = $line[1];
    $costs = explode(",", $line[2]);

    print get_levenshtein( $set1, $set2, (int) $costs[0], (int) $costs[2], (int) $costs[1] )."\n\r";
}

/*
 * get_levenshtein: equivalent to levenshtein native function in php, but in this case without limit
 *
 */
function get_levenshtein($s, $t, $cost_ins = 1, $costs_rep = 1, $cost_del = 1) { 
    $m = strlen($s);
    $n = strlen($t);
 
    for($i=0;$i<=$m;$i++) $d[$i][0] = $i*$cost_ins;
    for($j=0;$j<=$n;$j++) $d[0][$j] = $j*$cost_del;
 
    for($i=1;$i<=$m;$i++) {
        for($j=1;$j<=$n;$j++) {
            $c = ( $s[$i-1] == $t[$j-1] ) ? 0 : $costs_rep;
            $d[$i][$j] = min( $d[$i-1][$j] + $cost_ins, $d[$i][$j-1] +$cost_del, $d[$i-1][$j-1] + $c);
        }
    }
 
    return $d[$m][$n];
}

?>