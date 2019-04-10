type 'a document = {
  mutable current : 'a;
  mutable undo_stack : 'a list;
  mutable redo_stack : 'a list;
}

let make initial =
  {current = initial; undo_stack = []; redo_stack = [];}
;;

let set document data =
  document.undo_stack <- document.current :: document.undo_stack;
  document.current <- data;
  document.redo_stack <- [];
;;

let undo document =
  match document.undo_stack with
  | [] -> false
  | item :: rest ->
    document.redo_stack <- document.current :: document.redo_stack;
    document.current <- item;
    document.undo_stack <- rest;
    true


;;

let redo document =
  match document.redo_stack with
  | [] -> false
  | item :: rest ->
    document.undo_stack <- document.current :: document.undo_stack;
    document.current <- item;
    document.redo_stack <- rest;
    true
;;
