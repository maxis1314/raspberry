<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
    <title>上传结果</title>
    <style>
    body {
        background: #eee;
        font: 12px 'Lucida sans', Arial, Helvetica;
        color: #333;
        text-align: center;
    }
    
    a {
        color: #2A679F;
    }
    
    /*-------------------------------------*/
    
    .form-wrapper {
	width: 450px;
	padding: 8px;
	margin: 100px auto;
	overflow: hidden;
	border-width: 1px;
	border-style: solid;
	border-color: #dedede #bababa #aaa #bababa;
	-moz-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
	-webkit-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
	box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
	-moz-border-radius: 10px;
	-webkit-border-radius: 10px;
	border-radius: 10px;
	background-color: #f6f6f6;
	background-image: -webkit-gradient(linear, left top, left bottom, from(#f6f6f6), to(#eae8e8));
	background-image: -webkit-linear-gradient(top, #f6f6f6, #eae8e8);
	background-image: -moz-linear-gradient(top, #f6f6f6, #eae8e8);
	background-image: -ms-linear-gradient(top, #f6f6f6, #eae8e8);
	background-image: -o-linear-gradient(top, #f6f6f6, #eae8e8);
	background-image: linear-gradient(top, #f6f6f6, #eae8e8);
    }
    
    .form-wrapper #search {
        width: 330px;
        height: 20px;
        padding: 10px 5px;
        float: left;    
        font: bold 16px '微软雅黑', '黑体', '宋体';
        border: 1px solid #ccc;
        -moz-box-shadow: 0 1px 1px #ddd inset, 0 1px 0 #fff;
        -webkit-box-shadow: 0 1px 1px #ddd inset, 0 1px 0 #fff;
        box-shadow: 0 1px 1px #ddd inset, 0 1px 0 #fff;
        -moz-border-radius: 3px;
        -webkit-border-radius: 3px;
        border-radius: 3px;      
    }
    
    .form-wrapper #search:focus {
        outline: 0; 
        border-color: #aaa;
        -moz-box-shadow: 0 1px 1px #bbb inset;
        -webkit-box-shadow: 0 1px 1px #bbb inset;
        box-shadow: 0 1px 1px #bbb inset;  
    }
    
    .form-wrapper #search::-webkit-input-placeholder {
       color: #999;
       font-weight: normal;
    }
    
    .form-wrapper #search:-moz-placeholder {
        color: #999;
        font-weight: normal;
    }
    
    .form-wrapper #search:-ms-input-placeholder {
        color: #999;
        font-weight: normal;
    }    
    
    .form-wrapper #submit {
	float: right;
	border: 1px solid #00748f;
	height: 42px;
	width: 100px;
	padding: 0;
	cursor: pointer;
	font: bold 15px 微软雅黑, 黑体;
	color: #fafafa;
	text-transform: uppercase;
	background-color: #0483a0;
	background-image: -webkit-gradient(linear, left top, left bottom, from(#31b2c3), to(#0483a0));
	background-image: -webkit-linear-gradient(top, #31b2c3, #0483a0);
	background-image: -moz-linear-gradient(top, #31b2c3, #0483a0);
	background-image: -ms-linear-gradient(top, #31b2c3, #0483a0);
	background-image: -o-linear-gradient(top, #31b2c3, #0483a0);
	background-image: linear-gradient(top, #31b2c3, #0483a0);
	-moz-border-radius: 3px;
	-webkit-border-radius: 3px;
	border-radius: 3px;
	text-shadow: 0 1px 0 rgba(0, 0 ,0, .3);
	-moz-box-shadow: 0 1px 0 rgba(255, 255, 255, 0.3) inset, 0 1px 0 #fff;
	-webkit-box-shadow: 0 1px 0 rgba(255, 255, 255, 0.3) inset, 0 1px 0 #fff;
	box-shadow: 0 1px 0 rgba(255, 255, 255, 0.3) inset, 0 1px 0 #fff;
    }
      
    .form-wrapper #submit:hover,
    .form-wrapper #submit:focus {		
        background-color: #31b2c3;
        background-image: -webkit-gradient(linear, left top, left bottom, from(#0483a0), to(#31b2c3));
        background-image: -webkit-linear-gradient(top, #0483a0, #31b2c3);
        background-image: -moz-linear-gradient(top, #0483a0, #31b2c3);
        background-image: -ms-linear-gradient(top, #0483a0, #31b2c3);
        background-image: -o-linear-gradient(top, #0483a0, #31b2c3);
        background-image: linear-gradient(top, #0483a0, #31b2c3);
    }	
      
    .form-wrapper #submit:active {
        outline: 0;    
        -moz-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.5) inset;
        -webkit-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.5) inset;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.5) inset;    
    }
      
    .form-wrapper #submit::-moz-focus-inner {
        border: 0;
    }
    .form-wrapper1 {        width: 450px;
        padding: 8px;
        margin: 100px auto;
        overflow: hidden;
        border-width: 1px;
        border-style: solid;
        border-color: #dedede #bababa #aaa #bababa;
        -moz-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        -webkit-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        -moz-border-radius: 10px;
        -webkit-border-radius: 10px;
        border-radius: 10px;    
        background-color: #f6f6f6;
        background-image: -webkit-gradient(linear, left top, left bottom, from(#f6f6f6), to(#eae8e8)); 
        background-image: -webkit-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -moz-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -ms-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -o-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: linear-gradient(top, #f6f6f6, #eae8e8);
}
    .form-wrapper2 {        width: 450px;
        padding: 8px;
        margin: 100px auto;
        overflow: hidden;
        border-width: 1px;
        border-style: solid;
        border-color: #dedede #bababa #aaa #bababa;
        -moz-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        -webkit-box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        box-shadow: 0 3px 3px rgba(255,255,255,.1), 0 3px 0 #bbb, 0 4px 0 #aaa, 0 5px 5px #444;
        -moz-border-radius: 10px;
        -webkit-border-radius: 10px;
        border-radius: 10px;    
        background-color: #f6f6f6;
        background-image: -webkit-gradient(linear, left top, left bottom, from(#f6f6f6), to(#eae8e8)); 
        background-image: -webkit-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -moz-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -ms-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: -o-linear-gradient(top, #f6f6f6, #eae8e8);
        background-image: linear-gradient(top, #f6f6f6, #eae8e8);
}
.logo_div{
	width: 235px;
	height: 300px;
	top: 10px;
	margin: auto;
	background-image: url(img/pilogo.png);
	padding-top: 0px;
	}
.up_box{
	padding-top: 0px;
	margin-top: -50px;
	}
    </style>
</head>

<body>
<br /><br /><br /><!--<div class="logo_div"></div>-->
  <div class="up_box">
    <form class="form-wrapper">
    <input type="submit" id="submit" formaction="index.php" value="返回">
 <div id="search"><?php
@$fileInfo=$_FILES['files'];
$filename=$fileInfo['name'];
$type=$fileInfo['type'];
$tmp_name=$fileInfo['tmp_name'];
$size=$fileInfo['size'];
$error=$fileInfo['error'];
$maxSize=8388608;//文件大小限制(1024*1024*xMB)
$allowExt=array('jpeg','jpg','png','gif');//文件扩展名限制

//检查是否有选择文件
if ($error==UPLOAD_ERR_OK){    
  //上传限制
        if ($fileInfo['size']>$maxSize) {
            exit('上传文件大小超过设定值');
        }
        $ext=pathinfo($fileInfo['name'],PATHINFO_EXTENSION);
        if (!in_array($ext,$allowExt)) {
         //   exit('文件错误或损坏无法无法读取！');
        }
        //检查是否通过HTTP POS方式上传
        if (!is_uploaded_file($fileInfo['tmp_name'])) {
            exit('上传错误！请使用HTTP POS方式上传文件。');
        }
        
    //输出提示
    if (move_uploaded_file($tmp_name, __DIR__."/upload_folder/".$filename)) {
        echo '文件：“'.$filename.'”上传成功！';
    }else{
        echo '文件：“'.$filename.'上传失败！';          
    } 
  
}else{    
    //输出错误信息
    switch ($error){
        case 1:
            echo '文件上传失败，文件超过服务器设定大小！解决方法:更改PHP.ini设置中的dpload_max_filesize';
            break;
            
            case 2:
                echo '文件上传失败，文件超过服务器表设定！解决方法：更改PHP.ini设置中的MAX_FILE_SIZE';
                break;
                
                case 3:
                    echo '文件部分上传失败，请再试一次！';
                    break;
                    
                    case 4:
                        echo '没有选择文件！';
                        break;
                        
                        case 6:
                            echo '没有找到上传目录！';
                            break;
                        
                            case 7:
                            case 8:
                                echo '系统错误！';
                                break;
                    
    }
}
?>
</div>
  </form>
  </div>
<script src="js/jquery.min.js"></script>
</body>
</html>
