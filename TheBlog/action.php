<?php  
//action.php
$connect = mysqli_connect("localhost", "root", "", "webpython");

$input = filter_input_array(INPUT_POST);

$Title = mysqli_real_escape_string($connect, $input["Title"]);
$Subtitle = mysqli_real_escape_string($connect, $input["Subtitle"]);
$Name = mysqli_real_escape_string($connect, $input["Name"]);
$Date = mysqli_real_escape_string($connect, $input["Date"]);
$description = mysqli_real_escape_string($connect, $input["description"]);


if($input["action"] == 'edit')
{
 $query = "
UPDATE blog SET 
Subtitle = '".$Subtitle."', Name = '".$Name."' Date = '".$Date."'description = '".$description."'
WHERE Title = '".$input[Title]."'";
 mysqli_query($connect, $query);
}
if($input["action"] == 'delete')
{
 $query = "
 DELETE FROM blog 
 WHERE Title = '".$input["Title"]."'
 ";
 mysqli_query($connect, $query);
}

echo json_encode($input);

?>
