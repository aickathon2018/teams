'use strict';

const
  request = require('request'),
  fs = require('fs'),
  bodyParser = require('body-parser');

var
  admin = require("firebase-admin"),
  serviceAccount = require("./ez-grocer-firebase-adminsdk-bjskl-5bdd90bf39");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://ez-grocer.firebaseio.com"
});
var db = admin.firestore();

function upload_storage() {

  // Your Google Cloud Platform project ID
  const projectId = 'aickerthon-fd';

  // Imports the Google Cloud client library
  const { Storage } = require('@google-cloud/storage');

  // Creates a client
  const storage = new Storage();

  const bucketName = 'fd-photo-dump';
  const filename = 'receipt.jpeg';
  // Uploads a local file to the bucket
  storage.bucket(bucketName).upload(filename, {
    // Support for HTTP requests made with `Accept-Encoding: gzip`
    metadata: {
      // Enable long-lived HTTP caching headers
      // Use only if the contents of the file will never change
      // (If the contents will change, use cacheControl: 'no-cache')
      cacheControl: 'public, max-age=31536000',
    },
  });

  console.log(`${filename} uploaded to ${bucketName}.`);
}

function post_person(image_name) {
  const API_URL = 'https://fashion.recoqnitics.com/detect-person';
  const ACCESS_KEY = '36b1ccc780b35c95c508';
  const SECRET_KEY = '7a41d4acaa62812acafa15e3353769525ce6dd75';

  let formdata = {
    filename: fs.createReadStream(__dirname + '/' + image_name),
    access_key: ACCESS_KEY,
    secret_key: SECRET_KEY
  }

  request.post({ url: API_URL, formData: formdata },
    function (err, res, body) {
      doSomethingWith(JSON.parse(res.body), image_name);
    })
}

function doSomethingWith(data, image_name) {
  // console.log(image_name);
  // console.log(Object.keys(data.persons).length);
  var docRef = db.collection('num_ppl').doc('recoqnitics');
  var num = Object.keys(data.persons).length;
  var stamp = Date.now();
  var post_person = docRef.update({ [stamp]: num });
}
function post_receipt(receipt_name) {
  const API_KEY = '3ff21e50e9b311e8989bebb60acaaa28'

  let FormData = {
    file: fs.createReadStream(__dirname + '/' + receipt_name)
  }

  request.post({ url: "https://api.taggun.io/api/receipt/v1/simple/file", formData: FormData, headers: { apikey: API_KEY } }, (err, res, body) => {
    if (err) {
      return console.error("Upload Failed:", err);
    }
    console.log('Uploaded Successfully: Server response: ', body)
    var docRef = db.collection('receipt').doc('receipt_data');
    var stamp = Date.now();
    var post_person = docRef.update({ [stamp]: body });
  }
  )
}

/* 
Uncomment below function to test
*/

//post_person("face5.jpeg");
//post_person("face4.jpeg");
//upload_storage();
//post_receipt("receipt.jpeg");