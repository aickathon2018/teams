<div class="row mg-files" data-sort-destination data-sort-id="media-gallery">
  <div class="isotope-item document col-sm-6 col-md-6 col-lg-6">
    <div class="thumbnail">
      <div class="thumb-preview">
        <a class="thumb-image" href="<?php echo $produk->gambar; ?>">
          <img style="max-width:400px;width: expression(this.width > 400 ? 400: true);" src="<?php echo $produk->gambar; ?>" class="img-responsive" alt="Project">
        </a>
      </div>
      <h2 class="mg-title text-semibold"><?php echo $produk->nama_produk; ?></h2>
    </div>
  </div>
</div>

<div class="col-md-6">
  <section class="panel">
    <header class="panel-heading">
      <div class="panel-actions">
        <a href="#" class="fa fa-caret-down"></a>
        <a href="#" class="fa fa-times"></a>
      </div>

      <h2 class="panel-title">Pie Chart</h2>
      <p class="panel-subtitle">Default Pie Chart</p>
    </header>
    <div class="panel-body">

      <!-- Flot: Pie -->
      <div class="chart chart-md" id="flotPie"></div>
      <script type="text/javascript">

        var flotPieData = [{
          label: "Angry",
          data: [
            [1, 60]
          ],
          color: '#0088cc'
        }, {
          label: "Disgust",
          data: [
            [1, 10]
          ],
          color: '#2baab1'
        }, {
          label: "Fear",
          data: [
            [1, 15]
          ],
          color: '#AC399A'
        }, {
          label: "Happy",
          data: [
            [1, 15]
          ],
          color: '#FFBE51'
        }, {
          label: "Sad",
          data: [
            [1, 15]
          ],
          color: '#4A561F'
        }, {
          label: "Surprise",
          data: [
            [1, 15]
          ],
          color: '#521E2A'
        }, {
          label: "Neutral",
          data: [
            [1, 15]
          ],
          color: '#E36159'
        }];

        // See: assets/javascripts/ui-elements/examples.charts.js for more settings.

      </script>

    </div>
  </section>
</div>
</div>
