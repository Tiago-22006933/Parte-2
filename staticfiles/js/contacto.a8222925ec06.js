$( document ).ready(function() {
    $("#home_page").removeClass("active");
    $("#filmes_page").removeClass("active");
    $("#streaming_page").removeClass("active");
    $("#contacto_page").removeClass("active");
    $("#comentarios_page").removeClass("active");

    $("#contacto_page").addClass("active");
    $('.ui.dropdown')
      .dropdown()
    ;
});

$('#novo_contacto_button').on('click', function() {
    $('#modal_novo_contacto')
      .modal('show')
    ;
});

$('#novo_contacto_fecha_modal').on('click', function() {
    $('#modal_novo_contacto')
      .modal('hide')
    ;
});

$('.deleteicon').on('click', function() {
    $('#contacto_id').val(this.id);
    $('#modal_confirma_delete')
      .modal('show')
    ;
});

$('#remove_contacto_fecha_modal').on('click', function() {
    $('#modal_confirma_delete')
      .modal('hide')
    ;
});

$('.editicon').on('click', function() {
    $('#edita_contacto_id1').val(this.id);
    $.ajax({
        url: '/ajax/validate_username/',
        type: 'post',
        data: {
            'edita_contacto_id': this.id,
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        },
        dataType: 'json',
        success: function (data) {
            $.each(data, function(key, val) {
                $.each(val.fields, function(fieldname, field) {
                    if(fieldname == 'first_name') {
                        $('#first_name_edit').val(field);
                    } else if(fieldname == 'last_name') {
                        $('#flast_name_edit').val(field);
                    } else if(fieldname == 'email') {
                        $('#email_edit').val(field);
                    }
                });
            });
        }
    });
    $('#modal_edita_contacto')
      .modal('show')
    ;
});

$('#edita_contacto_fecha_modal').on('click', function() {
    $('#modal_edita_contacto')
      .modal('hide')
    ;
});