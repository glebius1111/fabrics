// ----- custom js ----- //

// hide initial
$("#searching").hide();
$("#results-table").hide();
$("#error").hide();

// global
var url = '';
var data = [];

$(function() {

  // sanity check
  console.log( "ready!" );

  // image click
  $("run").click(function() {

    // empty/hide results
    $("#results").empty();
    $("#results-table").hide();
    $("#error").hide();

    // show searching text
    $("#searching").show();
    console.log("searching...")

    // ajax request
    $.ajax({
      type: "POST",
      url: "/load",
      data : { img : image },
      // handle success
      success: function(result) {
        console.log(result.results);
        var data = result.results
        // show table
        $("#results-table").show();
        // loop through results, append to dom
        for (i = 0; i < data.length; i++) {
          $("#results").append('<tr><th><a href="'+url+data[i]["image"]+'"><img src="'+url+data[i]["image"]+
            '" class="result-img"></a></th><th>'+data[i]['score']+'</th></tr>')
        };
      },
      // handle error
      error: function(error) {
        console.log(error);
        // append to dom
        $("#error").append()
      }
    });

  });

});