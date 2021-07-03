$( document ).ready(function() {
    $("#home_page").removeClass("active");
    $("#filmes_page").removeClass("active");
    $("#streaming_page").removeClass("active");
    $("#contacto_page").removeClass("active");
    $("#comentarios_page").removeClass("active");

    $("#filmes_page").addClass("active");
    $('.ui.dropdown')
      .dropdown()
    ;

    const key = 'ljAqTZTAtGYTY5DDcADgW32IJkCEcPOr';

    $.ajax({

        'type': 'GET',
        'url': 'https://api.nytimes.com/svc/movies/v2/reviews/picks.json',
        data: {
            'q': '/reviews/picks.json',
            'response-format': "jsonp",
            'api-key': key,
            'callback': 'svc_search_v2_articlesearch'
        },
        success: function(data) {
            $.each(data.results, function(key, val) {
                const params = [];

                $.each(val, function(key, val1) {
                    params.push(val.display_title);
                    params.push(val.mpaa_rating);
                    params.push(val.critics_pick);
                    params.push(val.byline);
                    params.push(val.headline);
                    params.push(val.summary_short);
                    params.push(val.publication_date);
                    params.push(val.opening_date);
                    params.push(val.date_updated);
                    params.push(val.link);
                    params.push(val.multimedia);
                });
                appendFilmReview(params);
            });
        }
    });

});

function appendFilmReview(params) {
    var html = '<div class="ui raised fluid card"><div class="content">';
    html += '<div class="header">' + params[0] + '</div>';
    if (params[7] == null) {
       html += '<div className="meta">Estreia: data indisponivel</div>';
    } else {
        html += '<div className="meta"> <span className="category">Estreia: ' + params[7] + '</span></div>';
    }

    html += '<p></p>';
    html += '<div class="description"><p>' + params[5] + '</p></div>';
    html += '<p></p>';

    html += '<div class="extra content"><a class="header" href="' + params[9].url + '" target="_blank">Times review</a></div>';

    html += '</div></div>';
    $('#myCards').append(html);
}