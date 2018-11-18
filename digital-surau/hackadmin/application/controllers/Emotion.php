<?php
defined('BASEPATH') OR exit('No direct script access allowed');

require(APPPATH.'libraries/REST_Controller.php');
use Restserver\Libraries\REST_Controller;

class Emotion extends REST_Controller
{
  public function __construct()
	  {
	    parent::__construct();
	    $this->load->helper('url');
	    $this->load->model('M_emotion', 'emotion');
	  }

  public function sendEmotion_post()
  {
    $parameter = array(
        'id_produk' => $this->post('id_produk'),
        'id_customer' => $this->post('id_customer'),
        'age' => $this->post('age'),
        'gender' => $this->post('gender'),
        'angry' => $this->post('angry'),
        'disgust' => $this->post('disgust'),
        'fear' => $this->post('fear'),
        'happy' => $this->post('happy'),
        'sad' => $this->post('sad'),
        'surprise' => $this->post('surprise'),
        'neutral' => $this->post('neutral'));
        print_r($parameter);
    $result = $this->emotion->insert($parameter);

        if($result === FALSE)
        {
            $this->response(array('status' => 'failed'));
        }

        else
        {
            $this->response(array('status' => 'success'));
        }
  }
}
