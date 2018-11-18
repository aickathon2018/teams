  <!-- start: page -->
    <section class="panel">
      <header class="panel-heading">
        <div class="panel-actions">
          <a href="#" class="fa fa-caret-down"></a>
          <a href="#" class="fa fa-times"></a>
        </div>

        <h2 class="panel-title">Basic with Table Tools</h2>
      </header>
      <div class="panel-body">
        <table class="table table-bordered table-striped mb-none" id="datatable-tabletools" data-swf-path="<?php echo site_url('asset/vendor/jquery-datatables/extras/TableTools/swf/copy_csv_xls_pdf.swf'); ?>">
          <thead>
            <tr>
              <th>ID Emotion</th>
              <th>ID Produk</th>
              <th>ID Customer</th>
              <th>Age</th>
              <th>Gender</th>
              <th>Angry</th>
              <th>Disgust</th>
              <th>Fear</th>
              <th>Happy</th>
              <th>Sad</th>
              <th>Surprise</th>
              <th>Neutral</th>
            </tr>
          </thead>
          <tbody>
          <?php foreach ($lists as $list) :?>
            <tr class="gradeX">
              <td><?= $list['id_emotion']; ?></td>
              <td><?= $list['id_produk']; ?></td>
              <td><?= $list['id_customer']; ?></td>
              <td><?= $list['age']; ?></td>
              <td><?= $list['gender']; ?></td>
              <td><?= $list['angry']; ?></td>
              <td><?= $list['disgust']; ?></td>
              <td><?= $list['fear']; ?></td>
              <td><?= $list['happy']; ?></td>
              <td><?= $list['sad']; ?></td>
              <td><?= $list['surprise']; ?></td>
              <td><?= $list['neutral']; ?></td>
            </tr>
          <?php endforeach; ?>
          </tbody>
        </table>
      </div>
    </section>
  <!-- end: page -->
</section>
</div>

<aside id="sidebar-right" class="sidebar-right">
<div class="nano">
  <div class="nano-content">
    <a href="#" class="mobile-close visible-xs">
      Collapse <i class="fa fa-chevron-right"></i>
    </a>

    <div class="sidebar-right-wrapper">

      <div class="sidebar-widget widget-calendar">
        <h6>Upcoming Tasks</h6>
        <div data-plugin-datepicker data-plugin-skin="dark" ></div>

        <ul>
          <li>
            <time datetime="2014-04-19T00:00+00:00">04/19/2014</time>
            <span>Company Meeting</span>
          </li>
        </ul>
      </div>

      <div class="sidebar-widget widget-friends">
        <h6>Friends</h6>
        <ul>
          <li class="status-online">
            <figure class="profile-picture">
              <img src="assets/images/!sample-user.jpg" alt="Joseph Doe" class="img-circle">
            </figure>
            <div class="profile-info">
              <span class="name">Joseph Doe Junior</span>
              <span class="title">Hey, how are you?</span>
            </div>
          </li>
          <li class="status-online">
            <figure class="profile-picture">
              <img src="assets/images/!sample-user.jpg" alt="Joseph Doe" class="img-circle">
            </figure>
            <div class="profile-info">
              <span class="name">Joseph Doe Junior</span>
              <span class="title">Hey, how are you?</span>
            </div>
          </li>
          <li class="status-offline">
            <figure class="profile-picture">
              <img src="assets/images/!sample-user.jpg" alt="Joseph Doe" class="img-circle">
            </figure>
            <div class="profile-info">
              <span class="name">Joseph Doe Junior</span>
              <span class="title">Hey, how are you?</span>
            </div>
          </li>
          <li class="status-offline">
            <figure class="profile-picture">
              <img src="assets/images/!sample-user.jpg" alt="Joseph Doe" class="img-circle">
            </figure>
            <div class="profile-info">
              <span class="name">Joseph Doe Junior</span>
              <span class="title">Hey, how are you?</span>
            </div>
          </li>
        </ul>
      </div>

    </div>
  </div>
</div>
</aside>
</section>
