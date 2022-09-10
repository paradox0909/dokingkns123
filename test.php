<?php

$link = mysqli_connect(localhost, ‘test’, ‘test’, ‘solution’);


if (mysqli_connect_errno()) {
    die('Connect Error: '.mysqli_connect_error());
}
$query = “update set link_click=1 where email=‘{$_GET[email]}’”;

$result = mysqli_query($link, $query);

mysqli_close();

?>