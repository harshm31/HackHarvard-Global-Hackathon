function get_news()
{
	var title;
	var desc;
	var author;
	var link_to_news;
	var content;

	var today = new Date();
	var day = today.getDate();
	months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'),
	curMonth = months[today.getMonth()]
	var year = today.getFullYear();

	var news_date = curMonth + " " + day + " , " + year;

	$.ajax(
	{
		type : 'GET',
		url : 'https://newsapi.org/v2/everything?q=indian climate&pageSize=5&apiKey=2880f56c7bbb4311938d0025fb32ae34',
		dataType : 'json',
		crossOrigin : 'true',

		success : function(data,status) 
		{
			//console.log(data["articles"])
			$(".news-container").append("<div class='news_title'><p id ='news_title'>Today's Climate News <br> <span class='news_date'>" + news_date + "</span></div>");
			$.each(data["articles"],function(index,element)
			{
				$(".news-container").append("<hr>"+
					"<div class='articles'>" +
						"<a class='article_title' target='_blank' href = ' "+element.url + " '>" + element.title + " </a>"+
						"<br>"+
						"<div class='article_desc'>"+"<p id='article_desc'>" + element.description + "</p></div>" +
						"<div class='article_author'>" + "<p id = 'article_author'>-(" + element.author + ")</p></div>"+
					"</div>"
					);

			});
		}

	});
}

$(document).ready(function()
{
	get_news();
});