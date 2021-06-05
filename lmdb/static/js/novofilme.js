$( document ).ready(function() {
    $("#home_page").removeClass("active");
    $("#filmes_page").removeClass("active");
    $("#streaming_page").removeClass("active");
    $("#contacto_page").removeClass("active");
    $("#comentarios_page").removeClass("active");

    $('.ui.dropdown')
      .dropdown()
    ;
});

$('#novo_realizador_button').on('click', function() {
    $('#modal_novo_realizador')
      .modal('show')
    ;
});

$('#novo_realizador_fecha_modal').on('click', function() {
    $('#modal_novo_realizador')
      .modal('hide')
    ;
});