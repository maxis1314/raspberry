<?php
require("outerDB.php");
require("dbcenter.php");


$type = getParam('type');
$str = "";
if($type=='tact'){
	$pin = getParam('pin');
	if($pin==16){
		$str= led(1);
	}
	if($pin==20){
		$str= led(128);
	}
	 
}
if($type=='dip'){
	 
}
if($type=='remote'){
	$num = getParam('num',0);
	$data = json_decode(file_get_contents("mapping.json"),true);
	if($data[$num]){
		if($data[$num]){
			if(is_num($num)){
				$str = raspsend("type=".$data[$num]."&num=".$num);
			}else{
				$str = raspsend("type=".$data[$num]);
			}
		}else{
 			$str = raspsend("type=unknow&num=".$num);
 		}
 	}
 	/*
 	if($num=='chm'){
 		$str = raspsend("type=shutdown");
 	}
 	if($num=='chp'){
 		$str = raspsend("type=reboot");
 	}
 	if($num=='pp'){
 		$str = raspsend("type=cancel&num=1");
 	}*/
	 
}

echo $str;


var_dump($_GET);
var_dump($_POST);

$fp = fopen('log.txt','a');
fwrite($fp,var_export(array($_POST,$_GET,$str),true));
fclose($fp);
