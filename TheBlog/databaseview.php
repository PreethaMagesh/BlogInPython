<?php
$connect = mysqli_connect("localhost", "root", "", "webpython");
$query = "SELECT * FROM blog ORDER BY Title DESC";
$result = mysqli_query($connect, $query);
?>
<html>  
 <head>  
           
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>            
    <script src="jquery.tabledit.min.js"></script>
     
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v5.0.29, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
  <link rel="shortcut icon" href="assets/images/mbr-121x121.png" type="image/x-icon">
  <meta name="description" content="">
     
      <link rel="stylesheet" href="assets/web/assets/mobirise-icons2/mobirise2.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/formstyler/jquery.formstyler.css">
  <link rel="stylesheet" href="assets/formstyler/jquery.formstyler.theme.css">
  <link rel="stylesheet" href="assets/datepicker/jquery.datetimepicker.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link rel="preload" as="style" href="assets/mobirise/css/mbr-additional.css"><link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
     
    </head>  
    <body>  
        
        <section class="menu cid-s48OLK6784" once="menu" id="menu1-h">
    
    <nav class="navbar navbar-dropdown navbar-fixed-top navbar-expand-lg">
        <div class="container">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="index.html#top">
                        <img src="assets/images/mbr-121x121.png" alt="The Blog" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-black display-7" href="index.html#top">The Blog</a></span>
            </div>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <div class="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html#top">Home<br></a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html#testimonials1-k">About<br></a></li><li class="nav-item"><a class="nav-link link text-black display-4" href="index.html#form7-l">Write<br></a></li><a class="nav-link link text-black display-4" href="datareview.py">Read<br></a></li> <a class="nav-link link text-black display-4" href="databaseview.php">Edit<br></a></li></ul>
                
                
            </div>
        </div>
    </nav>

</section>

  <div class="container">  
   <br />  
   <br />  
   <br />  
            <div class="table-responsive">  
    <h2 align="center">Edit Table</h2><br />  
    <table id="editable_table" class="table table-bordered table-striped">
     <thead>
      <tr>
       <th>Title</th>
       <th>Subtitle</th>
       <th>Name</th>
       <th>Date</th>
       <th>description</th>
      </tr>
     </thead>
     <tbody>
     <?php
     while($row = mysqli_fetch_array($result))
     {
      echo '
      <tr>
       <td>'.$row["Title"].'</td>
       <td>'.$row["Subtitle"].'</td>
       <td>'.$row["Name"].'</td>
       <td>'.$row["Date"].'</td>
       <td>'.$row["description"].'</td>
      </tr>
      ';
     }
     ?>
     </tbody>
    </table>
   </div>  
  </div>  

 </body>  

</html>  

<script>  
$(document).ready(function(){  
     $('#editable_table').Tabledit({
      url:'action.php',
      columns:{
       identifier:[0, "Title"],
       editable:[[1, 'Subtitle'], [2, 'Name'], [3, 'Date'], [4, 'description']]
      },
      restoreButton:false,
      onSuccess:function(data, textStatus, jqXHR)
      {
       if(data.action == 'delete')
       {
        $('#'+data.id).remove();
       }

      }	
});
});
 </script>