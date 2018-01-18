# ***** BOOTSTRAP ******
BOOTSTRAP_WEB_SITE = """<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>TBD Labs</title>
    <link rel="icon" href="bootstrap/img/favicon.ico" type="image/icon" />

    <!-- Bootstrap Core CSS -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="bootstrap/css/agency.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="bootstrap/font-awesome-4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Kaushan+Script' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Droid+Serif:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,100,300,700' rel='stylesheet' type='text/css'>


</head>

<body id="page-top" class="index">

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                
                <a class="navbar-brand page-scroll" href="#page-top">TBD Labs</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li class="hidden">
                        <a href="#page-top"></a>
                    </li>
   
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>

    <!-- Header -->
    <header>
        <div class="container">
            <div class="intro-text">
                
                <!-- User View -->
                <div class="intro-heading">NVDA</div>
                <div class="intro-lead-in">Today's Avg: TBD </div>
                <div class="intro-lead-in">Tomorrow's Avg*: TBD </div>

                <!-- Developer View -->
                <div class="intro-heading">Ticker</div>
                <div class="intro-lead-in">Date: TBD </div>
                <div class="intro-lead-in">Open Price: TBD </div>
                <div class="intro-lead-in">Day Price: TBD </div>
                <div class="intro-lead-in">Close Price: TBD </div>
                <div class="intro-lead-in">Today's Avg: TBD </div>
                <div class="intro-lead-in">Tomorrow's Avg*: TBD </div>

            </div>
        </div>
    </header>

    <footer>
        <div class="container">
            <div class="row">
                    <span class="copyright">Copyright &copy; TBD Labs 2017</span>

            </div>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="bootstrap/js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="bootstrap/js/bootstrap.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
    <script src="bootstrap/js/classie.js"></script>
    <script src="bootstrap/js/cbpAnimatedHeader.js"></script>

    <!-- Contact Form JavaScript -->
    <script src="bootstrap/js/jqBootstrapValidation.js"></script>
    <script src="bootstrap/js/contact_me.js"></script>

    <!-- Custom Theme JavaScript -->
    <script src="bootstrap/js/agency.js"></script>

</body>

</html>"""


PLAIN_WEB_SITE = """<!doctype html> 
<html> 
  
  <body>  
    <h1 style="width: 100%; text-align: center;" >STOCKBOT</h1> 

    <h1 style="width: 100%; text-align: center;" > NVDA </h1>
    <h2 style="width: 100%; text-align: center;" > Quantity: {quatity} </h2>
    <h2 style="width: 100%; text-align: center;" > Last Price: {last_price} </h2>
    <h2 style="width: 100%; text-align: center;" > Current Value: {current_value} </h2> 

  </body>
</html>"""