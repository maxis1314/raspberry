<?php
header('content-type:text/html;charset=GB2312');
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
            exit('文件错误或损坏无法无法读取！');
        }
        //检查是否通过HTTP POS方式上传
        if (!is_uploaded_file($fileInfo['tmp_name'])) {
            exit('上传错误！请使用HTTP POS方式上传文件。');
        }
        
    //输出提示
    if (move_uploaded_file($tmp_name, "upload_folder/".$filename)) {
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