$(document).ready(function(e) {
    var le = jsonObject.newslist;

    var news = function() {
        for (var i = 0; i < le.length; i++) {

            var z = le[i].title + ' - ' + le[i].description;
            var t = le[i].title;
            var u = le[i].url;
            var im = le[i].img;
            var d = le[i].published;

			var dt = new Date(d);
            var day = dt.getDate()
            var mounth = dt.getMonth() + 1;
            var year = dt.getFullYear();

            var txt = $("<div></div>").addClass("news-item col-sm-6 col-md-3");
            var link = $("<a></a>").attr({
                href: u,
                title: z,
                target: "_blank"
            }).text(t);

            var lm = $("<a class='btn btn-primary'>Читати</a>").attr({
                href: u,
                target: "_blank"
            });

            var date = $("<small></small>").text(day + '/' + mounth + '/' + year);

            var title = $("<h3 class='title'></h3>").append(link);
            var desc = $("<p class='description'></p>").text(z);

            var img = $("<img />").attr({
                src: im,
                alt: z
            });
            var thumbnail = $("<div class='thumbnail'></div>").append(img);

            var caption = $("<div class='caption'></div>").append(title, date, desc, lm);

            $("#json-news").append(txt.append(thumbnail, caption));

        }
    }

    news();

});
