type 'a doccol = {
  mutable count : int;
  mutable curdoc : 'a Document.document;
  mutable curname : string;
  mutable docs : (string * 'a Document.document) list;
}

let make name doc =
  {count = 1; curdoc = doc; curname = name; docs = [( name , doc )];}
;;

let add doccol name doc =
  let return = List.assoc_opt name doccol.docs in (*checks to see if the name is already being used*)
  match return with
  | None ->
    doccol.count <- doccol.count + 1;
    doccol.docs <- (name,doc) :: doccol.docs;
    true
  | Some _ -> false
;;

let remove doccol name =
  let name_case = (name = doccol.curname) in (*is the input the current list*)
  let is_in = List.assoc_opt name doccol.docs in (*does the list contain*)
  match (name_case, is_in) with
  | (true, _) -> false
  | (false, None) -> false
  | (false, Some _) ->
    doccol.count <- doccol.count - 1;
    doccol.docs <- (List.remove_assoc name doccol.docs);
    true

;;

let has doccol name =
  let is_in = List.assoc_opt name doccol.docs in
  match is_in with
  | None -> false
  | Some _ -> true
;;

let switch doccol name =
  let has_name = has doccol name in
  match has_name with
  | true ->
    doccol.curname <- name;
    doccol.curdoc <- List.assoc name doccol.docs;
    true
  | false -> false
;;

let string_of_doccol doccol =
  let init = Printf.sprintf "%d docs\n" doccol.count in
  List.fold_left (fun str (s,_) -> str^"- "^s^"\n") init doccol.docs;
;;
