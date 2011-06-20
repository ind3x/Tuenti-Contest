#!/usr/bin/php
<?
ini_set("memory_limit", "-1");

global $total_cows, $cows, $total_posibilities, $weight_limit, $cow_weight, $cow_milk;

function generate_posibilities() {
    global $total_cows, $cows;
    
    $posibilities_buffer = array();
    
    //var_dump($cows);
    
    foreach ( $cows as $cow ) {
        $posibilities_buffer[] = array($cow);
    
        for ( $i=0; $i < $total_cows-1; $i++ ) {
            $posibilities_buffer = generate_next_posibilities($posibilities_buffer);
        }
        
        $total_posibilities = array_merge_recursive((array) $total_posibilities, $posibilities_buffer);
    }
    unset($cow, $posibilities_buffer);

    $total_posibilities = filter_posibilities_per_weight($total_posibilities);
    
    return $total_posibilities;
}

function generate_next_posibilities($posibilities_buffer) {
    global $total_cows, $cows;
     
    foreach ( $posibilities_buffer as $key => $posibilities ) {
        foreach ( $cows as $key => $cow ) {
            if ( !in_array( $cow, $posibilities ) ) {
                $new_posibiliti = $posibilities;
                $new_posibiliti[] = $cow;
                
                $new_posibilities_buffer[] = $new_posibiliti;
                unset($new_posibiliti);
            }
        }
        
        unset( $posibilities_buffer[$key] );
        unset( $cow );
    }
    unset( $posibilities );
    
    $posibilities_buffer = array_merge_recursive(array(), $new_posibilities_buffer);
    unset($new_posibilities_buffer);
    return $posibilities_buffer;
}

function filter_posibilities_per_weight($total_posibilities) {
    global $weight_limit, $cow_weight;
    
    foreach ( $total_posibilities as &$posibiliti ) {
        $weight = 0;
        $new_posibiliti = array();
        
        foreach ( $posibiliti as $cow ) {
            if ( $weight + $cow_weight[$cow] <= $weight_limit ) {
                $weight += $cow_weight[$cow];
                $new_posibiliti[] = $cow;
            }
        }
        
        $posibiliti = $new_posibiliti;
    }
    
    return $total_posibilities;
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