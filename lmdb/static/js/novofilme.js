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

$('#novo_actor_button').on('click', function() {
    $('#modal_novo_actor')
      .modal('show')
    ;
});

$('#novo_actor_fecha_modal').on('click', function() {
    $('#modal_novo_actor')
      .modal('hide')
    ;
});

$('#novo_filme_button').on('click', function() {
    var form = document.getElementById("novo_filme_form");
    $("#id_filme_form-nome").val($("#nome_filme").val());
    $("#id_filme_form-genero").val($("#genero_filme").val());
    $("#id_filme_form-data_lancamento").val($("#data_lancamento_filme").val());
    $("#id_filme_form-realizador").val($("#realizador_filme").val());
    $("#id_filme_form-actores").val($("#actores_filme").val());
    form.submit();
});