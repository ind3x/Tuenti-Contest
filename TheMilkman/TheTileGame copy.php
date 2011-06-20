#!/usr/bin/php
<?php
ini_set("default_charset", "utf-8");

$lines = file( 'php://stdin' );
$line = explode(" ", $lines[0]);

$set1 = $line[0];
$set2 = $line[1];
$costs = explode(",", $line[2]);

//print strlen($set1)."\n\r\n\r";
//print strlen($set2)."\n\r";
//var_dump($costs);

$total_cost = 0;
if ( strlen($set1) == strlen($set2) ) {
    if ( compare_costs($costs) ) {
        if ( $set1[$i] != $set2[$i] ) {
            $total_cost = switch_tile($costs[2], $total_cost);
        }
    } else {
        for ($i=0; $i < strlen($set1); $i++) {
            if ( $set1[$i] !== $set2[$i] ) {
                $total_cost = delete_tile($costs[1], $total_cost);
                $total_cost = insert_tile($costs[0], $total_cost);
            }
        }
    }
    
    print $total_cost;
} else {
    print 'nooooo!';
}

/*
 * compare_cost: compare if replace costs less than insert+remove
 *  return: true if replace is less, false if cost more
 */
function compare_costs($costs) {
    if ( $costs[2] <= $costs[0]+$costs[1] ) {
        return true;
    } else {
        return false;
    }
}

function insert_tile($cost, $total_cost) {
    return $total_cost += $cost;
}

function delete_tile($cost, $total_cost) {
    return $total_cost += $cost;
}

function switch_tile($cost, $total_cost) {
    return $total_cost += $cost;
}

?>