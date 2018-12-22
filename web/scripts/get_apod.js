var url;
var title;
var img_copyright;
var img_date;


var nasa_api_key = "BAGV1YD0sK0ln96PDnZp47Q1UYuCEhOTr9yRNsIh"

function get_apod()
{		
		$.ajax(
		{
			type :'GET',
			url : 'https://api.nasa.gov/planetary/apod?api_key='+nasa_api_key,
			crossOrigin : 'true',
			dataType : 'json',

			success :function(data,status)
			{
				img_copyright = data["copyright"];
				img_date = data["date"];
				title = data["title"];
				url = data["hdurl"];
				desc = data["explanation"];

				$("#banner").append(
					"<div class='img_container'>" +  
  						"<img src = ' "+url + " ' alt = 'apod image' class='banner_image' >"+
 					 	"<div class='top-left'>"+img_date+"</div>"+
  						"<div class='top-right'>"+img_copyright+"</div>"+
  						"<div class='centered'>"+title+"</div>"+
					"</div>"
					);
			},
			error : function(data) 
			{
				console.log("error loading image");
				$("#banner").append(
					"<img src = '../images/img_not_found' class = 'banner_image' >"
				);
			}
		});
}


$(document).ready(function()
{
	get_apod();
});

