$( document ).ready(function() {
    var originplace = $("#id_originplace");
    var destinationplace = $("#id_destinationplace");
    var origincountry = $("#origin-country");
    var destinationcounty = $("#destination-country");
    originplace.keyup(function(){// $ je jquery objekt
        ajax_call_for_location(originplace, origincountry); //ili this- objek nad kojim je fcja pozvana
	});
    destinationplace.keyup(function(){// $ je jquery objekt
        ajax_call_for_location(destinationplace, destinationcounty); //ili this- objek nad kojim je fcja pozvana
  });
});

function ajax_call_for_location(element, country_element){
        $.ajax({
        /*url: "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/",
        type: "get", //send it through get method
        beforeSend: function(request) {
          request.setRequestHeader("X-RapidAPI-Key", "5908a87257msh999fa4b31ebaa8ap143422jsn1f46950fbff4");
        },*/
      url: "http://localhost:8000/locations/",
      type: "get",
      data: { 
        query: element.val() //ili this.value - get parametri
      },
        success: function(result){//poziv callback funkcije koja ce se dogoditi u slucaju uspjeha
          options = $("#options");
          options.html(""); //isprazni div od prethodnih rezultata
          result.Places.forEach(function(item, index){
            options.append(function() {
              return $("<div>" + item.PlaceName + "</div>").click(
                function handler() { 
                  element.val(item.PlaceId);
                  ajax_call_for_country_details(country_element);
                  }
                );
            })
          })  
        },
        error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
          }
      });
}

function ajax_call_for_country_details(element){
        $.ajax({
      url: "http://localhost:8000/country_details/",
      type: "get",
      data: { 
        country: 'Croatia' //ili this.value - get parametri
      },
        success: function(result){//poziv callback funkcije koja ce se dogoditi u slucaju uspjeha
          element.html(result); //isprazni/pregazi div (da ne naljepi i prethodne rezultate)     
        },
        error: function (xhr, ajaxOptions, thrownError) {
            console.log(xhr.status);
            console.log(thrownError);
          }
      });
}