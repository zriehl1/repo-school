let curr_list : string list ref = ref [];;
let undo_stack : string list list ref = ref [];;
let redo_stack : string list list ref = ref [];;
let reset_all () =
  curr_list := [];
  undo_stack := [];
  redo_stack := [];
;;
let set_to_list new_list =
  undo_stack := !curr_list :: !undo_stack;
  curr_list := new_list;
  redo_stack := [];
;;
let add_elem elem =
  set_to_list (Sortedlist.insert !curr_list elem)
;;
let remove_elem elem =
  set_to_list (Sortedlist.remove !curr_list elem)
;;
let merge_with_list lst =
  set_to_list (Sortedlist.merge !curr_list lst)
;;
let undo () =
  match !undo_stack with
  |[] -> false
  |a :: b -> (*if there is at least one element, change the values and report sucess*)
    undo_stack := b;
    redo_stack := !curr_list :: !redo_stack;
    curr_list := a;
    true
;;
let redo () =
  match !redo_stack with
  |[] -> false
  |a :: b -> (*if there is at least one element, change the values and report sucess*)
    redo_stack := b;
    undo_stack := !curr_list :: !undo_stack;
    curr_list := a;
    true
;;
