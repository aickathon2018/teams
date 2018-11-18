<?php defined('BASEPATH') OR exit('No direct script access allowed');

class M_emotion extends CI_Model{

  public function __construct()
  {
    parent::__construct();
    $this->load->database();
  }

  public function insert($data)
  {
    // $data = array(
    //   'id_produk' => $data['id_']
    // );
    // print_r($data);
    $this->db->insert('emotion', $data);
    return TRUE;
  }

}
