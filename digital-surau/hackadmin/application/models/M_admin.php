<?php defined('BASEPATH') OR exit('No direct script access allowed');

class M_admin extends CI_Model{

  var $table = 'webberita';
  var $column_order = array('username', null,'kategori','lat','lng','alamat','keterangan', 'gambar'); //set column field database for datatable orderable
  var $column_search = array('username','kategori','lat','lng','alamat','keterangan', 'gambar'); //set column field database for datatable searchable

  public function __construct()
  {
    parent::__construct();
    $this->load->database();
  }

  public function read($link = FALSE)
  {
    if ($link === FALSE) {
      $query = $this->db->get('emotion');
      return $query->result_array();
    } else {
      $query = $this->db->get_where('produk', array('id_produk' => $link));
      return $query->row();
    }
  }

  public function readEmotion($link)
  {
    $query = $this->db->get_where('emotion', array('id_produk' => $link));
    $array = $query->result_array();
    // foreach($array as $item) {
    //     $angry += $item['angry'];
    //     $disgust += $item['disgust'];
    //     $fear += $item['fear'];
    //     $happy += $item['happy'];
    //     $sad += $item['sad'];
    //     $surprise += $item['surprise'];
    //     $neutral += $item['neutral'];
    //
    //     // to know what's in $item
    //     echo '<pre>'; var_dump($item);
    // }
    // print_r($array);
    return $query->result_array();
  }

public function readCount($time)
  {
    $date = array(0, 1, 7, 14, 30);
    $result = array();
    foreach ($date as $value) {
      $date2 = $value-1;
      $query = $this->db->where('tanggal >= CURDATE() - INTERVAL '.$value.' DAY')
      ->where('tanggal < CURDATE() - INTERVAL '. $date2 .' DAY')
      ->get('laporan');
      $result[] = $query->num_rows();
      // echo $this->db->last_query();
      // echo '<pre>'; print_r($result); echo '</pre>';;
    }
    if($time === 'today') {
      $query = $this->db->where('tanggal >= CURDATE() - INTERVAL 30 DAY')
      ->where('tanggal < CURDATE() - INTERVAL  0 DAY')
      ->get('laporan');
      // $query = $this->db->get_where('laporan', array('tanggal' >= 'NOW() + INTERVAL -30 DAY', 'tanggal' < 'NOW() + INTERVAL  0 DAY'));
      // echo $this->db->last_query();
      return $query->num_rows();
    } else {
        return $result;
    }
  }

public function readArea()
  {
    $kecamatan = array("pancoran","beji","cipayung","sukmajaya","cilodong","limo","cinere","cimanggis","tapos","sawangan","bojongsari");
    $count = array();
    foreach ($kecamatan as $value) {
      $query = $this->db->like('alamat', $value)
      ->get('laporan');
      $count[] = $query->num_rows();
    }
    return $count;
  }

public function readUser()
  {
    $query = $this->db->get('app_user');
    return $query->result_array();
  }

public function readUserCount()
  {
    $date = array(0, 1, 7, 14, 30);
    $result = array();
    foreach ($date as $value) {
      $date2 = $value-1;
      $query = $this->db->where('join_date >= CURDATE() - INTERVAL '.$value.' DAY')
      ->where('join_date < CURDATE() - INTERVAL '. $date2 .' DAY')
      ->get('app_user');
      $result[] = $query->num_rows();
      // echo '<pre>'; print_r($result); echo '</pre>';
      // echo $this->db->last_query();

    }

    return $result;
  }

public function readCategory()
  {
    $kategori = array("angkutan","jalan","terminal","stasiun","lampu lalulintas","taman","toilet","lampu jalan","trotoar");
    $count = array();
    foreach ($kategori as $key => $value) {
      $query = $this->db->like('kategori', $value)
      ->get('laporan');
      $count[] = $query->num_rows();
    }
    return $count;
  }
  /*
  public function read($link = FALSE)
  {
    if ($link === FALSE) {
      $query = $this->db->get('post');
      return $query->result_array();
    } else {
      $query = $this->db->get_where('post', array('link' => $link));
      return $query->row();
    }
  }
*/
  public function delete($link)
  {
    $this->db->where('id_laporan', $link);
    return $this->db->delete('laporan');
  }

  public function update($linkLama)
  {
    //$linkBaru = url_title($this->input->post('judul'), 'dash', TRUE);

    $data = array(
        'username' => $this->input->post('username'),
        'kategori' => $this->input->post('kategori'),
		'tanggal' => $this->input->post('tanggal'),
		'lat' => $this->input->post('lat'),
		'lng' => $this->input->post('lng'),
		'alamat' => $this->input->post('alamat'),
		'keterangan' => $this->input->post('keterangan')
    );

    $this->db->where('id_laporan', $linkLama);
    return $this->db->update('laporan', $data);
  }


  function tambahUser()
  {
    $data = array(
      'username' => 'admin',
      'password' => password_hash("admin", PASSWORD_DEFAULT)
    );
    return $this->db->insert('user', $data);
  }

  function updateUser($user, $status)
  {
    $array = explode(",", $user);
    $data = array('status' => $status );
    $this->db->where_in('id_user', $array);
    return $this->db->update('app_user', $data);
  }
}
