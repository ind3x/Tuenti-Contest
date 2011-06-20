#!/usr/bin/php
<?
ini_set("memory_limit", "-1");

global $total_cows, $cows, $total_posibilities, $weight_limit, $cow_weight, $cow_milk;

function generate_posibilities() {
    global $total_cows, $cows;
    
    for ($i++; $i<$total_cows-1; $i++) {
        
    }
}

function milk_per_posibilities($total_posibilities) {
    global $cow_milk;
    
    $total_milk = array();
    
    foreach ( $total_posibilities as $posibiliti ) {
        $milk = 0;
        
        foreach ( $posibiliti as $cow ) {
            $milk += $cow_milk[$cow];
        }
        
        $total_milk[] = $milk;
        
    }
    
    $total_milk = array_merge_recursive(array(), array_unique($total_milk));
    rsort($total_milk);
    
    return $total_milk;
}

function maximized_milk_production($milk_per_posibilities) {
    return $milk_per_posibilities[0];
}

#main
//foreach( file( 'php://stdin' ) as $line ) {
$lines = file( 'php://stdin' );
    $line = explode(" ", $lines[3]);
    
    $total_cows = (int) $line[0];
    
    $weight_limit = (int) $line[1];
    $cows = range(0, $total_cows-1);
    
    $cow_weight = preg_split("/,/", $line[2]);
    $cow_milk = preg_split("/,/", $line[3]);
    
    $total_posibilities = generate_posibilities(array());
    $milk_per_posibilities = milk_per_posibilities($total_posibilities);
    $output = maximized_milk_production($milk_per_posibilities);
    
    print "\n\r\n\r".$output."\n\r";
//}
?>