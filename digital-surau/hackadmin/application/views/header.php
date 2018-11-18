<!doctype html>
<html class="fixed">
	<head>

		<!-- Basic -->
		<meta charset="UTF-8">

		<meta name="keywords" content="HTML5 Admin Template" />
		<meta name="description" content="Porto Admin - Responsive HTML5 Template">
		<meta name="author" content="okler.net">

		<!-- Mobile Metas -->
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

		<!-- Web Fonts  -->
		<link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800|Shadows+Into+Light" rel="stylesheet" type="text/css">

		<!-- Vendor CSS -->
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/bootstrap/css/bootstrap.css'); ?>" />
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/font-awesome/css/font-awesome.css'); ?>" />
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/magnific-popup/magnific-popup.css'); ?>" />
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/bootstrap-datepicker/css/datepicker3.css'); ?>" />

	<?php if (uri_string() == "" || uri_string() == "admin") { ?>
    <!-- Specific Page Vendor CSS -->
    <link rel="stylesheet" href="<?php echo site_url('asset/vendor/jquery-ui/css/ui-lightness/jquery-ui-1.10.4.custom.css'); ?>" />
    <link rel="stylesheet" href="<?php echo site_url('asset/vendor/bootstrap-multiselect/bootstrap-multiselect.css'); ?>" />
    <link rel="stylesheet" href="<?php echo site_url('asset/vendor/morris/morris.css'); ?>" />
  <?php } elseif ($_SERVER['REQUEST_URI'] === "/hackadmin/admin/listEmotion") { ?>
			<!-- Specific Page Vendor CSS -->
			<link rel="stylesheet" href="<?php echo site_url('asset/vendor/select2/select2.css'); ?>" />
			<link rel="stylesheet" href="<?php echo site_url('asset/vendor/jquery-datatables-bs3/assets/css/datatables.css'); ?>" />
  <?php } elseif ($_SERVER['REQUEST_URI'] === "/hackadmin/admin/produk") {?>
		<!-- Specific Page Vendor CSS -->
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/isotope/jquery.isotope.css'); ?>" />
		<link rel="stylesheet" href="<?php echo site_url('asset/vendor/morris/morris.css'); ?>" />
	<?php } ?>


		<!-- Theme CSS -->
		<link rel="stylesheet" href="<?php echo site_url('asset/stylesheets/theme.css'); ?>" />

		<!-- Skin CSS -->
		<link rel="stylesheet" href="<?php echo site_url('asset/stylesheets/skins/default.css'); ?>" />

		<!-- Theme Custom CSS -->
		<link rel="stylesheet" href="<?php echo site_url('asset/stylesheets/theme-custom.css'); ?>">

		<!-- Head Libs -->
		<script src="<?php echo site_url('asset/vendor/modernizr/modernizr.js'); ?>"></script>

	</head>
  <body>
