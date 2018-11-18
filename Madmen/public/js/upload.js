  // Initialize Firebase
  var config = {
      apiKey: "AIzaSyBRk3QQ_sISX-_YUl1T0f_A35Wyj2J2os0",
      authDomain: "camera-sensor-ef345.firebaseapp.com",
      databaseURL: "https://camera-sensor-ef345.firebaseio.com",
      projectId: "camera-sensor-ef345",
      storageBucket: "camera-sensor-ef345.appspot.com",
      messagingSenderId: "808807412191"
  };
  firebase.initializeApp(config);

  var databaseTable = firebase.database().ref('database');

  var threshold = 0.8;
  var emotionList = [];
  var emotionAnal = [0, 0, 0, 0, 0, 0, 0];
  var legacyEmotion = [0, 0, 0, 0, 0, 0, 0];
  var emotionCount = 0;
  var entries = 0;
  var legacyEntries = 0;
  //changes JSON.stringify to array with its individual emotion
  function getEmotion(strDisplay) {
      var emotion = [null, null, null, null, null, null, null];
      var strSplit = strDisplay.split(' ');
      var i = 0;

      console.log('Person');
      while (i != strSplit.length) {
          // console.log(strSplit[i]);
          switch (strSplit[i]) {
              case '"angry":':
                  ++entries;
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionAngry = ' + emotion[0]);
                  break;
              case '"disgust":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionDisgust = ' + emotion[1]);
                  break;
              case '"fear":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionFear = ' + emotion[2]);
                  break;
              case '"happy":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionHappy = ' + emotion[3]);
                  break;
              case '"sad":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionSad = ' + emotion[4]);
                  break;
              case '"surprise":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionSurprise = ' + emotion[5]);
                  break;
              case '"neutral":':
                  emotion[emotionCount++] = removeComma(strSplit[i + 1]);
                  console.log('emotionNuetral = ' + emotion[6]);
                  emotionCount = 0;
                  let cloneArray = JSON.parse(JSON.stringify(emotion));
                  emotionList.push(cloneArray);
                  break;
          }
          console.log('Entries = ' + entries);
          i++;
      }
  }

  //get rid of the comma behind the numbers
  function removeComma(value) {
      var valueSplit = value.split('');
      var output = '';
      var i;

      for (i = 0; i < valueSplit.length - 2; i++) {
          output = output + valueSplit[i];
      }
      return output;
  }

  //get the highest value of each array 
  //if more than threshold (0.8) the emotion of the value will be 1 
  function calEmotions() {
      //parseFloat(str)
      let array = null;
      for (i = 0; i < emotionList.length; i++) {
          var count = 0;
          array = emotionList[i];

          let highest = parseFloat(array[0]);

          for (j = 0; j < array.length; j++) {
              if (highest < parseFloat(array[j])) {
                  count = j;
                  highest = parseFloat(array[j]);
              }
          }

          emotionAnal[count]++;
      }
  }


  //function to print array => emotionList
  //just for testing. No actual use
  function printArray(array) {
      var str = '';
      let arraylist = null;
      for (i = 0; i < array.length; i++) {
          arraylist = array[i];
          for (j = 0; j < arraylist.length; j++) {
              str = str + arraylist[j] + '\t';
          }
          str = str + '\n';
      }
      return str;
  }

  //get picture and post to API
  //starts other functions
  function uploadPhoto() {

    //   databaseInit();
    //   retrieveFirebase();
      console.log('Get face');

      var strDisplay = '';
      var API_URL = 'https://face.recoqnitics.com/analyze'
      var ACCESS_KEY = 'cc7d67f2adb06edcb419';
      var SECRET_KEY = 'e10f180f2fdf99ec9eae2c92c4e3bc8c9373198f';
      var formData = new FormData(document.forms.namedItem('fileinfo'))
      formData.append("access_key", ACCESS_KEY);
      formData.append("secret_key", SECRET_KEY);

      console.log("Before ajax")
      $.ajax({
          url: API_URL,
          type: "POST",
          data: formData,
          processData: !1,
          contentType: !1,
          success: function (response) {
              console.log("After ajax")
              responseJSONstr = JSON.stringify(response, null, 5);
              strDisplay = responseJSONstr + "\n";
              responseJSON = response
              console.log(response)

              emotionList = [];
              getEmotion(strDisplay);
              calEmotions();
              saveData();
              saveToFirebase();
              console.log("Ajax Emotion Anal")
              console.log(emotionAnal);
          },
          error: function (jqXHR, textStatus, errorMessage) {

          }
      })
  }

  // Table stuff
  function saveData() {
      console.log("Saving Data...")
      for (i = 0; i < legacyEmotion.length; i++) {
          console.log(legacyEmotion[i])
      }
      var items = [{
              Emotion: "Angry",
              Value: emotionAnal[0]
          },
          {
              Emotion: "Disgust",
              Value: emotionAnal[1]
          },
          {
              Emotion: "Fear",
              Value: emotionAnal[2]
          },
          {
              Emotion: "Happy",
              Value: emotionAnal[3]
          },
          {
              Emotion: "Sad",
              Value: emotionAnal[4]
          },
          {
              Emotion: "Surprised",
              Value: emotionAnal[5]
          },
          {
              Emotion: "Neutral",
              Value: emotionAnal[6]
          },
          {
              Emotion: "TOTAL:",
              Value: entries
          }
      ];

      function loadTable(tableId, fields, data) {
          console.log("Loading table..")
          var rows = '';
          $.each(data, function (index, item) {
              var row = '<tr">';
              $.each(fields, function (index, field) {
                  row += '<td>' + item[field + ''] + '</td>';
              });
              rows += row + '<tr>';
          });

          $('#' + tableId + ' tbody').html(rows);
      }

      loadTable('tableList', ['Emotion', 'Value'], items);


      var emotionalAnal = JSON.parse(localStorage.getItem("emotionAnal"));
      localStorage.setItem('emotionAnal', JSON.stringify(emotionAnal));
      localStorage.setItem('emotionAnalysis', JSON.stringify(emotionalAnal));
      localStorage.setItem('total', entries);

      $('#btn-update').click(function (e) {
          loadTable('tableList', ['Emotion', 'Value'], items);
      });


  }

  //Saving and Overiding the Database
  function saveToFirebase() {
      console.log("saveToFirebase...")
      //   for (i = 0; i < legacyEmotion.length; i++) {
      //       console.log(legacyEmotion[i])
      //   }
      //   console.log(legacyEntries)
      var a = emotionAnal[0] + legacyEmotion[0];
      console.log("A = " + a);
      console.log("anal = " + emotionAnal[0]);
      console.log("lega = " + legacyEmotion[0]);
      var b = emotionAnal[1] + legacyEmotion[1];
      var c = emotionAnal[2] + legacyEmotion[2];
      var d = emotionAnal[3] + legacyEmotion[3];
      var e = emotionAnal[4] + legacyEmotion[4];
      var f = emotionAnal[5] + legacyEmotion[5];
      var g = emotionAnal[6] + legacyEmotion[6];
      var h = entries + legacyEntries;
      databaseTable.child("Angry").set(a);
      databaseTable.child("Disgust").set(b);
      databaseTable.child("Fear").set(c);
      databaseTable.child("Happy").set(d);
      databaseTable.child("Sad").set(e);
      databaseTable.child("Surprised").set(f);
      databaseTable.child("Neutral").set(g);
      databaseTable.child("Total").set(h);
  }

  //   Initialize Database
  function databaseInit() {
      console.log("saveToFirebase...")
      for (i = 0; i < legacyEmotion.length; i++) {
          console.log(legacyEmotion[i])
      }
      console.log(legacyEntries)
      databaseTable.child("Angry").set(1);
      databaseTable.child("Disgust").set(1);
      databaseTable.child("Fear").set(1);
      databaseTable.child("Happy").set(1);
      databaseTable.child("Sad").set(1);
      databaseTable.child("Surprised").set(1);
      databaseTable.child("Neutral").set(1);
      databaseTable.child("Total").set(1);
  }

  function retrieveFirebase() {

      console.log("Retrieving Data...")
      var usersRef = firebase.database().ref('database');
      var users = [];
      usersRef.on('value', function (snap) {
          users.push(snap.val()); // Push children to a local users array
      });

      console.log("Users Array")
      for (i = 0; i < users.length; i++) {
          console.log("Users = " + users[i]);
      }

      console.log("Emotion Analysis... Before")
      for (i = 0; i < emotionAnal.length; i++) {
          console.log(emotionAnal[i]);
      }
      console.log(entries)

      console.log("Printing data...")
      // for(i=0; i<users.length; i++){
      //     emotionAnal[i] = users[i];
      //     console.log(users[i]);
      // }

      legacyEmotion[0] = users[0];
      legacyEmotion[1] = users[1];
      legacyEmotion[2] = users[2];
      legacyEmotion[3] = users[3];
      legacyEmotion[4] = users[4];
      legacyEmotion[5] = users[5];
      legacyEmotion[6] = users[6];
      legacyEntries = users[7];


      console.log("Emotion Analysis... After")
      for (i = 0; i < emotionAnal.length; i++) {
          console.log(emotionAnal[i]);
      }
      console.log(entries)


  }