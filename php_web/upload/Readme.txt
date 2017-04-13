如果遇到乱码等现象请检查浏览器是否为UTF-8

文件上传文件夹upload_folder
拷贝到Pi上之后要更改目录更改目录行在216行一般PHP5没装错www目录直接复制这行即可 /var/www/upload_folder/

Copy_upt_pure.php文件所纯PHP代码供大家进行折腾。

错误解决：
由于linux的安全机制，最好使用root帐户，更改www以及向下和向上的文件夹权限777

很有趣的是，windows的http pos机制和linux的不一样，（这个小问题折腾了我近3小时）
最后的解决方法是修改php.ini文件里的：
第二行前面的“；”号去掉保存然后Reboot即可

/****************************/
；Always populate the $HTTP_POS_DATA variable
always_populate_raw_post_data = On
/****************************/

1、文件上传失败，文件超过服务器设定大小！解决方法:更改PHP.ini设置中的dpload_max_filesize
2、文件上传失败，文件超过服务器表设定！解决方法：更改PHP.ini设置中的MAX_FILE_SIZE

/*注意，每次对 PHP.ini 和 put.php 的更改保存后必须重启Apache服务或者直接Reboot*/