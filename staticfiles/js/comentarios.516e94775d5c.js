$( document ).ready(function() {
    $("#home_page").removeClass("active");
    $("#filmes_page").removeClass("active");
    $("#streaming_page").removeClass("active");
    $("#contacto_page").removeClass("active");
    $("#comentarios_page").removeClass("active");

    $("#comentarios_page").addClass("active");
    $(".rating").rating();
});


$('#comentario_submit').on('click', function() {
    var form = document.getElementById("comentario_form");
    var count_clareza = 0;
    var count_rigor = 0;
    var count_precisao = 0;
    var count_profundidade = 0;
    var count_amplitude = 0;
    var count_logica = 0;
    var count_significancia = 0;
    var count_originalidade = 0;
    var count_global = 0;

    $("#rating_clareza").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_clareza++;
        }
    });
    $("#rating_rigor").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_rigor++;
        }
    });
    $("#rating_precisao").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_precisao++;
        }
    });
    $("#rating_profundidade").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_profundidade++;
        }
    });
    $("#rating_amplitude").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_amplitude++;
        }
    });
    $("#rating_logica").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_logica++;
        }
    });
    $("#rating_significancia").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_significancia++;
        }
    });
    $("#rating_originalidade").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_originalidade++;
        }
    });
    $("#rating_global").find("i").each(function()
    {
        if($(this).hasClass('active')){
            count_global++;
        }
    });

    $("#id_clareza").val(count_clareza);
    $("#id_rigor").val(count_rigor);
    $("#id_precisão").val(count_precisao);
    $("#id_profundidade").val(count_profundidade);
    $("#id_amplitude").val(count_amplitude);
    $("#id_lógica").val(count_logica);
    $("#id_significância").val(count_significancia);
    $("#id_originalidade").val(count_originalidade);
    $("#id_globalidade").val(count_global);
    $("#id_comentário").val($("#comentario_input").val());

    form.submit();
});

$('#novo_comentario_button').on('click', function() {
    $('#modal_novo_comentario')
      .modal('show')
    ;
});

$('#novo_comentario_fecha_modal').on('click', function() {
    $('#modal_novo_comentario')
      .modal('hide')
    ;
});