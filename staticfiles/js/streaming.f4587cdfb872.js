$( document ).ready(function() {
    $("#home_page").removeClass("active");
    $("#filmes_page").removeClass("active");
    $("#streaming_page").removeClass("active");
    $("#contacto_page").removeClass("active");
    $("#comentarios_page").removeClass("active");

    $("#streaming_page").addClass("active");
    $('.ui.dropdown')
      .dropdown()
    ;
});