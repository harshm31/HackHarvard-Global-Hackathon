$(document).ready(function()
{
	$("#city_info").hide();

	$("#select_city").change(function()
	{
		var city = $("#select_city").val();
		city = city.toLowerCase();
		console.log(city)
		getCityInfo(city);
		//add different methods like to show charts predictions tables etc 
	});
});

function getCityInfo(city)
{
	$("#city_info").show();

	network_url = "https://en.wikipedia.org/w/api.php?action=opensearch&origin=*&search="+city+"&limit=6&format=json";
	console.log(network_url);
	$.ajax(
	{
		type : 'get',
		url : network_url,
		dataType : 'json',
		crossOrigin : 'true',
		crossDomain :'true',
		beforeSend : function(request) 
		{
			request.setRequestHeader("Access-Control-Allow-Credentials","true");
			request.setRequestHeader("Access-Control-Allow-Origin"," * ");
			request.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
			request.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
			//request.setRequestHeader("Origin","*");
		},
		success : function(data,status)
		{
			$(".info_box").html("");
			console.log(data[2]);
			text = "";
			for (i=0;i<data[2].length;i++)
			{
				text += data[2][i];
			}
			console.log(text);
			$(".info_box").append(
				"<p id='city_info_text' > <img src = '../images/cities/"+city+".jpeg' class='info_box_img'>" + text + "</p>"
				);
		}

	});
}