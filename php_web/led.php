<?php
require("outerDB.php");
require("dbcenter.php");

$dir = __DIR__."/../SAKS-SDK/examples";
echo "<pre>";
$type = getParam('type');
if($type=='led'){
	echo led($_POST[num]);
}
if($type=='digital'){
	echo digital($_POST[num]);
}
if($type=='int'){
    echo digitalint($_POST[num]);
}
if($type=='beep'){
	echo beep(getParam('num',1));
}
if($type=='cmd'){
    $action = getParam('action');
    echo raspsend("type=$action&num=$_POST[num]");  
}
if($type=='clear'){
	echo led(0);
	echo digital('####');
    echo raspsend("type=cancel");  
}
if($type=='wendu'){	
	echo wendu();
}
if($type=='mapping'){ 
    $num = getParam('num');
    $action = getParam('action');
    $data = json_decode(file_get_contents("mapping.json"),true);
    if($num){
       $data[$num] = $action;
       file_put_contents("mapping.json", json_encode($data));
    }
}
echo "</pre>";
?>
<br>
LED:
<form method=post>
<input type=text name=num value="<?php echo $_POST[num];?>">
<input type=hidden name=type value='led'>
<input type=submit>
</form>
DIGITAL:
<form method=post>
<input type=text name=num value="<?php echo $_POST[num];?>">
<input type=hidden name=type value='digital'>
<input type=submit>
</form>
INT:
<form method=post>
<input type=text name=num value="<?php echo $_POST[num];?>">
<input type=hidden name=type value='int'>
<input type=submit>
</form>
BEEP:
<form method=post>
<input type=text name=num value="<?php echo $_POST[num];?>">
<input type=hidden name=type value='beep'>
<input type=submit>
</form>
OTHER:
<form method=post>
<input type=hidden name=type value='cmd'>
<input type=radio  name=action value='reboot'>reboot
<input type=radio  name=action value='shutdown'>shutdown
<input type=radio  name=action value='cancel'>cancel
<input type=radio  name=action value='update'>update
<input type=radio  name=action value='wendu'>wendu
<input type=radio  name=action value='clear'>clear
<input type=radio  name=action value='net'>net
<input type=radio  name=action value='netled'>netled
<input type=radio  name=action value='alarm'>alarm
<input type=radio  name=action value='setalarm'>setalarm
<input type=radio  name=action value='notify'>notify
<input type=radio  name=action value='learning'>learning
<br>
<input type=text name=num value="<?php echo $_POST[num];?>">
<input type=submit>
</form>
MAPPING:
<form method=post>
<input type=hidden name=type value='mapping'>
<input type=text name=num value="<?php echo $_POST[num];?>">
<select name=action>
    <option value=''>--</option>
    <option value='shutdown'>shutdown</option>
    <option value='reboot'>reboot</option>
    <option value='cancel'>cancel</option>
    <option value='wendu'>wendu</option>
    <option value='clear'>clear</option>
    <option value='fireworks'>fireworks</option>
    <option value='dfireworks'>dfireworks</option>
    <option value='net'>net</option>
    <option value='netled'>netled</option>
    <option value='alarm'>alarm</option>
    <option value='setalarm'>setalarm</option>
    <option value='notify'>notify</option>
    <option value='learning'>learning</option>
</select>

<input type=submit>
</form>
UPLOAD:
<form class="form-wrapper" action="upload/upt.php" method="post" enctype="multipart/form-data" target=_blank>
    <input type="file" name="files" id="search">
   <input type="submit" id="submit" value="Upload">
</form>
PUSH:
<form class="form-wrapper" action="http://115.28.24.177:8092/sms/receive_pushover.php" method="get" target=_blank>    
     <input type="hidden" name="pass" value="s321">
    title<input type="text" name="title" id="search">
    message<input type="text" name="message" id="search">    
   <input type="submit" id="submit" value="Upload">
</form>
<br>
<?php

echo "<pre>",execute_command("ps aux | grep python"),"</pre>";
$map = json_decode(file_get_contents("mapping.json"),true);
echo "<table border=1>";
foreach($map as $k=>$v){
    echo "<tr><td>$k</td><td>$v</td></tr>";
}
echo "</table>";
?>