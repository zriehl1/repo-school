open Document;;
open Doccol;;

let showall doccol =
  let helper (str,doc) =
    Printf.printf "--List %s--\n" str;
    Sortedlist.print doc.current;
  in
  List.iter helper doccol.docs;
;;

let saveall doccol =
  let helper (str,doc) = Util.strlist_to_file doc.current str in
  List.iter helper doccol.docs;
;;

let addall doccol elem =
  let helper (str,doc) = Document.set doc (Sortedlist.insert doc.current elem) in
  List.iter helper doccol.docs;
;;

 let mergeall doccol =
  let helper cur (str,doc) = Sortedlist.merge doc.current cur in
  List.fold_left helper [] doccol.docs;
;;
