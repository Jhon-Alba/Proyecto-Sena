$(document).ready(function() {
  var table = $('#myTable').DataTable({
    "paging": true,
    "lengthChange": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": true,
    "responsive": true,
    "language": {
      "sProcessing": "Procesando...",
      "sLengthMenu": "Mostrar _MENU_ registros",
      "sZeroRecords": "No se encontraron resultados",
      "sEmptyTable": "Ningún dato disponible en esta tabla",
      "sInfo": " _START_ al _END_ de _TOTAL_ registros",
      "sInfoEmpty": " 0 al 0 de 0 registros",
      "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
      "sSearch": "Buscar:",
      "oPaginate": {
        "sFirst": "<<",
        "sLast": ">>",
        "sNext": ">",
        "sPrevious": "<"
      }
    }
  });

  // Filtro por estado en cualquier columna
  $('#estadoFilter').on('change', function() {
    var status = this.value.toLowerCase();
    
    if (status) {
      // Recorrer todas las filas de la tabla para buscar "Activo" o "Inactivo" en cualquier columna
      table.rows().every(function() {
        var rowData = this.data();
        var found = false;

        // Recorrer cada celda de la fila y buscar "Activo" o "Inactivo"
        $(rowData).each(function(index, value) {
          if (status === 'activado' && value.match(/\bActivo\b/i)) {
            found = true;
          } else if (status === 'inactivado' && value.match(/\bInactivo\b/i)) {
            found = true;
          }
        });

        // Mostrar/ocultar la fila dependiendo si encontramos coincidencias
        if (found) {
          $(this.node()).show();
        } else {
          $(this.node()).hide();
        }
      });
    } else {
      // Si no hay filtro, mostrar todas las filas
      table.rows().every(function() {
        $(this.node()).show();
      });
    }
  });

  // Búsqueda por nombre
  $('#searchInput').on('keyup', function() {
    table.search(this.value).draw();
  });

  // Botón de búsqueda
  $('#searchButton').on('click', function() {
    table.search($('#searchInput').val()).draw();
  });
});
