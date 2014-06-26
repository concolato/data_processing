<?php
// Perform linear transformation to manipulate image grey scales by 20 pixels
function makeImgLighter($lines){
	$dataArray = array();

	try{
		for($i = 0; $i < count($lines); $i++){
			//Read file lines by row
			$lineArray = explode(" ", $lines[$i]);

			for($j = 0; $j < count($lineArray); $j++){	
			//Read line rows by column	
				if(is_numeric($lineArray[$j])){			
					if($lineArray[$j] >= 256){
						$lineArray[$j] = 256;
					}else{
						//y=mx + b
						$lineArray[$j] = $lineArray[$j] + 20; 
						//This will lighten the image and -20 will darken it
					}
					array_push($dataArray, $lineArray[$j]);
				}			
			}
		}

		return $dataArray; 
	} catch(Exception $e){
		error_log("Linear Transformation failed.");
	}
}

$oldfile = "sample_images/lena256_PPM.ppm";
$lines = file($oldfile);
//Process the image
$dataArray = makeImgLighter($lines);
$dataString = implode(" ", $dataArray);
$dataString = "P3\n".$dataString;
$newfile = "sample_images/newlightImage.ppm";

if (!$handle = fopen($newfile, 'w')) {
     echo "Cannot open file ($filename)";
     exit;
}
if (fwrite($handle, $dataString) === FALSE) {
    echo "Cannot write to file ($filename)";
    exit;
}
//Image has been processed
echo "Success, wrote data to file ($filename)";
fclose($handle);
?>
