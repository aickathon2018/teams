<html>
<head>

<link href="https://fonts.googleapis.com/css?family=Black+And+White+Picture|Cabin+Sketch" rel="stylesheet">

<style>


h1 {color:yellow;}

* {
	font-family: 'Black And White Picture', sans-serif;
	font-family: 'Cabin Sketch', cursive;
}

p {
	color: white;
	font-size: 18px;
	font-weight: ;

}

#desc {
	color: red;
	font-size: 28px;

}

#teamname {
	color: blue;
	font-size: 20px;
	font-weight: bold;

}


</style>



</head>
<body>
<body bgcolor="black">

<center>


<h1>Welcome to GXC Cinema</h1>
<p id="desc">CamSeG</p>
<p id="teamname">UoL-W.E.B</p>


<input type='file' id="filechooser" onchange="readURL(this);" />

<br>
    <img id="blah" src="#" alt="your image" />
<br>
<br>


<button onclick="uploadFile()">Analyze</button>
<p id="output">Verification in process</p>
</center>

<script
  src="https://code.jquery.com/jquery-3.3.1.js"
  integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
  crossorigin="anonymous"></script>

<script>



function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#blah')
                    .attr('src', e.target.result)
                    .width(150)
                    .height(200);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }



function uploadFile() {
  var blobFile = $('#filechooser')[0].files[0];
  var formData = new FormData();

  // upload image through form (jpg/jpeg/png)
  formData.append("filename", blobFile);

  // change the access_key and secret_key here
  formData.append("access_key", "1b59fceb71a718cdb238");
  formData.append("secret_key", "42e29e878b49131b6afca0705ab99fe7546538da");

  //To use Jquery, you can download it from http://jquery.com/download/
  //or include it from a CDN into your HTML.
  $.ajax({
     url: "https://face.recoqnitics.com/analyze",
     type: "POST",
     data: formData,
     processData: false,
     contentType: false,
     success: function(response) {




         console.log(response);
 	 $('#output').html("Age: " + response['faces'][0]['age']);


	if (response['faces'][0]['age'] >=  18) {
		alert("PLEASE PROCEED");
	} else {
		alert("UNDER AGE!!!\nACCESS DENIED");
	}





     },
     error: function(jqXHR, textStatus, errorMessage) {
         console.log(errorMessage); // Optional
     }
  });
}



</script>

</body>

</html>
