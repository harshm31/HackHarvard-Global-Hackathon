$(document).ready(function()
{
	$("#city_info").hide();
	$("#historical_data").hide()

	$("#select_city").change(function()
	{
		var selection = $("#select_city").val();
		var string_sel = String(selection);
		var pos = string_sel.search("-");
		var city = string_sel.substring(0,pos);
		var city_id = string_sel.substring(pos+1,string_sel.length);
		city_id = city_id.trim();
		city = city.trim();
		city = city.toLowerCase();
		getCityInfo(city);
		getClimateData(city_id);
		//add different methods like to show charts predictions tables etc 
	});
});

function getCityInfo(city)
{
	$("#city_info").show();
	$("#historical_data").show();

	network_url = "https://en.wikipedia.org/w/api.php?action=opensearch&origin=*&search="+city+"&limit=6&format=json";
	//console.log(network_url);
	$.ajax(
	{
		type : 'get',
		url : network_url,
		dataType : 'jsonp',
		crossOrigin : 'true',
		crossDomain :true,
		headers : 
		{
			'Access-Control-Allow-Origin': '*',
        	'Access-Control-Allow-Credentials': true,
		},	
		success : function(data,status)
		{
			$(".info_box").html("");
			//console.log(data[2]);
			text = "";
			for (i=0;i<data[2].length;i++)
			{
				text += data[2][i];
			}
			//console.log(text);
			$(".info_box").append(
				"<p id='city_info_text' > <img src = '../images/cities/"+city+".jpeg' class='info_box_img'>" + text + "</p>"
				);
		}

	});
}

function getClimateData(city_id) 
{
	console.log("1");
	data_url = "http://api.openweathermap.org/data/2.5/forecast?id="+city_id+"&cnt=15&appid=ac7c75b9937a495021393024d0a90c44";
	console.log(data_url);
	$.ajax(
	{
		type : 'GET',
		url : data_url,
		crossOrigin : 'true',
		crossDomain :'true',
		dataType : 'jsonp',
		headers : 
		{
			'Access-Control-Allow-Credentials' : true,
			'Access-Control-Allow-Origin' : '*',
			'Origin' : '*',
		},
		success : function(data,status)
		{
			$("#table_body").html("");
			//console.log("data : " + data);
			//console.log(data["weather"][0]["main"]);
			$.each(data["list"],function(index,element)
			{
				console.log(String(element['dt_txt']));
				$("#table_body").append(
					"<tr>"+
						"<td class='table_data'>"+element['dt_txt']+ "</td>"+
						"<td class='table_data'>"+element['main'].temp+"</td>"+
						"<td class='table_data'>"+element['main'].pressure+"</td>"+
						"<td class='table_data'>"+element['main'].humidity+"</td>"+
						"<td class='table_data'>"+element['main'].temp_min+"</td>"+
						"<td class='table_data'>"+element['main'].temp_max+"</td>"+
						"<td class='table_data'>"+element['wind'].speed+"</td>"+
						"<td class='table_data'>"+element['wind'].deg+"</td>"+
						"<td class='table_data'>"+element['clouds'].all+"</td>"+
						"<td class='table_data'>"+element['weather'][0]['description']+"</td>"+
					"</tr>"
					);
			});
			
		},
		error : function(data)
		{
			$("#table_body").html("");
			$("#table_body").append(
				"<tr>"+
					"<th class='table_header'></th>"+
					"<td class='table_data'>No Data Found</td>"+
					"<td class'table_data'>No Data Found</td>"+
					"<td class='table_data'>No Data Found</td>" +
					"<td class='table_data'>No Data Found</td>" +
					"<td class='table_data'>No Data Found</td>" +
					"<td class='table_data'>No Data Found</td>" +
					"<td class='table_data'>No Data Found</td>" +
					"<td class='table_data'>No Data Found</td>"+
				"</tr>"
				);
		}
	});
}
