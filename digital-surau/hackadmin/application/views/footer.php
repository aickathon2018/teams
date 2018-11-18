    <!-- Vendor -->
    <script src="<?php echo site_url('asset/vendor/jquery/jquery.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/jquery-browser-mobile/jquery.browser.mobile.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/bootstrap/js/bootstrap.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/nanoscroller/nanoscroller.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/bootstrap-datepicker/js/bootstrap-datepicker.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/magnific-popup/magnific-popup.js'); ?>"></script>
		<script src="<?php echo site_url('asset/vendor/jquery-placeholder/jquery.placeholder.js'); ?>"></script>

<!-- Theme Base, Components and Settings -->
<script src="<?php echo site_url('asset/javascripts/theme.js'); ?>"></script>

<!-- Theme Custom -->
<script src="<?php echo site_url('asset/javascripts/theme.custom.js'); ?>"></script>

<!-- Theme Initialization Files -->
<script src="<?php echo site_url('asset/javascripts/theme.init.js'); ?>"></script>
<?php if (uri_string() == "" || uri_string() == "admin") { ?>

  <!-- Specific Page Vendor -->
  <script src="<?php echo site_url('asset/vendor/jquery-ui/js/jquery-ui-1.10.4.custom.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-ui-touch-punch/jquery.ui.touch-punch.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-appear/jquery.appear.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/bootstrap-multiselect/bootstrap-multiselect.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-easypiechart/jquery.easypiechart.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot-tooltip/jquery.flot.tooltip.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.pie.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.categories.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.resize.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-sparkline/jquery.sparkline.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/raphael/raphael.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/morris/morris.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/gauge/gauge.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/snap-svg/snap.svg.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/liquid-meter/liquid.meter.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/jquery.vmap.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/data/jquery.vmap.sampledata.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/jquery.vmap.world.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.africa.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.asia.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.australia.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.europe.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.north-america.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jqvmap/maps/continents/jquery.vmap.south-america.js'); ?>"></script>

  <!-- Examples -->
  <script src="<?php echo site_url('asset/javascripts/dashboard/examples.dashboard.js'); ?>"></script>
<?php } elseif ($_SERVER['REQUEST_URI'] === "/hackadmin/admin/listEmotion") {?>
  <!-- Specific Page Vendor -->
  <script src="<?php echo site_url('asset/vendor/select2/select2.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-datatables/media/js/jquery.dataTables.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-datatables/extras/TableTools/js/dataTables.tableTools.min.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-datatables-bs3/assets/js/datatables.js'); ?>"></script>

  <!-- Theme Base, Components and Settings -->
  <script src="<?php echo site_url('asset/javascripts/theme.js'); ?>"></script>

  <!-- Theme Custom -->
  <script src="<?php echo site_url('asset/javascripts/theme.custom.js'); ?>"></script>

  <!-- Theme Initialization Files -->
  <script src="<?php echo site_url('asset/javascripts/theme.init.js'); ?>"></script>

  <!-- Examples -->
  <script src="<?php echo site_url('asset/javascripts/tables/examples.datatables.default.js'); ?>"></script>
  <script src="<?php echo site_url('asset/javascripts/tables/examples.datatables.row.with.details.js'); ?>"></script>
  <script src="<?php echo site_url('asset/javascripts/tables/examples.datatables.tabletools.js'); ?>"></script>
<?php } else if ($this->uri->segment(2) === 'produk') { ?>
  <!-- Specific Page Vendor -->
  <script src="<?php echo site_url('asset/vendor/isotope/jquery.isotope.js'); ?>"></script>
  <!-- Specific Page Vendor -->
  <script src="<?php echo site_url('asset/vendor/jquery-appear/jquery.appear.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-easypiechart/jquery.easypiechart.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot-tooltip/jquery.flot.tooltip.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.pie.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.categories.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/flot/jquery.flot.resize.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/jquery-sparkline/jquery.sparkline.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/raphael/raphael.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/morris/morris.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/gauge/gauge.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/snap-svg/snap.svg.js'); ?>"></script>
  <script src="<?php echo site_url('asset/vendor/liquid-meter/liquid.meter.js'); ?>"></script>

  <!-- Examples -->
  <script src="<?php echo site_url('asset/javascripts/pages/examples.mediagallery.js'); ?>" /></script>
  <script src="<?php echo site_url('asset/javascripts/ui-elements/examples.charts.js'); ?>"></script>

<?php } ?>
</body>
</html>
