$('[data-widget="pushmenu"]').on('click', function (){
        $('[data-widget="pushmenu"]').PushMenu("toggle");
});

$(function () {
  bsCustomFileInput.init();
});

//$(document).ready( function () {
//  var table = $('#example1').DataTable();
//  $(".dataTables_empty").text("Desculpe, nada foi encontrado!");
//});

$(function () {
$("#example1",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "searching": false,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
}).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$('#documentosPad').DataTable({
  "paging": true,
  "lengthChange": false,
  "searching": true,
  "ordering": true,
  "info": true,
  "autoWidth": false,
  "responsive": true,
});
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#tramitacaoPad",).DataTable({
  "responsive": true, "lengthChange": false, "ordering": false, "autoWidth": false, "searching": true,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
}).buttons().container().appendTo('#tramitacaoPad_wrapper .col-md-6:eq(0)');
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#notificacaoLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
});
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#vistoriaLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
});
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#averbacoesLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
}).buttons().container().appendTo('#averbacoesLebre_wrapper .col-md-6:eq(0)');
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#pareceresArquivosLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
});
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#tramitacaoLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
}).buttons().container().appendTo('#tramitacaoLebre_wrapper .col-md-6:eq(0)');
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
$("#despachoInternoLebre",).DataTable({
  "responsive": true, "lengthChange": false, "autoWidth": false, "ordering": false, "searching": true,
  "buttons": ["csv", "excel", "pdf", "print", "colvis"]
}).buttons().container().appendTo('#despachoInternoLebre_wrapper .col-md-6:eq(0)');
$(".dataTables_empty").text("Desculpe, nada foi encontrado!");
});

var x = document.getElementsByClassName("cpfcnpj");
for(i=0;i<x.length;i++){ x[i].addEventListener('focus',function(e){ document.getElementById(e.target.id).select(); }); }
for(var i = 0; i < x.length; i++) { x[i].addEventListener('keyup', myFunction, false); }
function myFunction(e)
{
    x = '';
    if(e.keyCode == 8 || e.keyCode == 46){
        return false;
    }
    if(e.keyCode >= 48 || e.keyCode <= 57){

        var id = e.target.id;
        document.getElementById(id).setAttribute('maxlength',18);
        var str = e.target.value.replace(/\D/g,'');
        //var str = str.replace(/^0+/, '');
        var len = str.length; //
        if(len==11){
            x = str.substr(0, 3) + '.' + str.substr(3, 3) + '.' + str.substr(6, 3) + '-' + str.substr(9, 2);; // 510.791.784-49
        }else if(len>11 && len<15){
            x = str.substr(0, 2) + '.' + str.substr(2, 3) + '.' + str.substr(5, 3) + '/' + str.substr(8, 4) + '-' + str.substr(12, 2);  // 04.498.492/0001-67
        }else{
            x = str;
        }
        document.getElementById(id).value = x;
    }
}

document.querySelector('button[type="reset"]').addEventListener('click', function (e) {
  e.preventDefault();
  this.parentElement.reset();
})

$(document).ready( function() {
   $('#despachoInternoLebre').dataTable( {
     "language": {
       "emptyTable": "No data ae"
     }
   });
});