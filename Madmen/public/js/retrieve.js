function saveData() {
    // console.log("Saving Data...")
    // for (i = 0; i < upload.legacyEmotion.length; i++) {
    //     console.log(upload.legacyEmotion[i])
    // }

    var emotionAnal = JSON.parse(localStorage.getItem("emotionAnal"));
    var entries = localStorage.getItem("total");
    console.log(emotionAnal);
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

    $('#btn-update').click(function (e) {
        loadTable('tableList', ['Emotion', 'Value'], items);
    });


}

function clearData(){
    var resetData = [0, 0, 0, 0, 0, 0, 0];
    localStorage.setItem('emotionAnal', JSON.stringify(resetData));
    localStorage.setItem('total', 0);
}