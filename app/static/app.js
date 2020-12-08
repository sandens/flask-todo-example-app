
function delete_todo(todo_id) { 

var r = confirm("Sure you want to delete thie todo?");
  if (r == true) {
    $('<form action="/remove" method="POST">' +
            '<input type="hidden" name="todo_id" value="' + todo_id + '" />' +
                '</form>').appendTo('body').submit();
       
  } 
}