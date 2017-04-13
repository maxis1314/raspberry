<?php
/**
 * Socket PHP客户端
 * 
 */
header ( 'Content-type:text/html;charset=utf8' );
$host = 'tcp://localhost:9999';
$fp = stream_socket_client ( $host, $errno, $error, 20 );
if (! $fp)
{
     
    echo "$error ($errno)";
} else
{
    fwrite ( $fp, 'one|two|three|caodan' );
    while ( ! feof ( $fp ) )
    {
        echo fgets ( $fp ); #获取服务器返回的内容
    }
    fclose ( $fp );
}
