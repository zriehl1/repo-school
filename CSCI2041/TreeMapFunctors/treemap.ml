open Printf;;
module type KEYVAL_SIG = sig
  type key_t;;
  type value_t;;
  val compare_keys : key_t -> key_t -> int;;
  val keyval_string : key_t -> value_t -> string;;
end;;

module Make(KVMod : KEYVAL_SIG) : sig
  type treemap =
    | Empty
    | Node of {key : KVMod.key_t; value : KVMod.value_t; left : treemap; right : treemap}
  val empty : treemap
  val add : treemap -> KVMod.key_t -> KVMod.value_t -> treemap
  val tree_string : treemap -> string
  val getopt : treemap -> KVMod.key_t -> KVMod.value_t option
  val contains_key : treemap -> KVMod.key_t -> bool
  val iter : (KVMod.key_t -> KVMod.value_t -> 'a) -> treemap -> unit
  val fold : ('a -> KVMod.key_t -> KVMod.value_t -> 'a) -> 'a -> treemap -> 'a
  val to_string : treemap -> string
  val findmin_keyval : treemap -> KVMod.key_t * KVMod.value_t
  val remove_key : treemap -> KVMod.key_t -> treemap
end = struct

type treemap =
  | Empty
  | Node of {
      key   : KVMod.key_t;
      value : KVMod.value_t;
      left  : treemap;
      right : treemap;
    }
;;

let empty = Empty;;

let rec add map key value =
  match map with
  | Empty ->
     Node{key=key; value=value;
          left=Empty; right=Empty}
  | Node(node) ->
     let diff = KVMod.compare_keys key node.key in
     if diff = 0 then
       Node{node with value=value}
     else if diff < 0 then
       Node{node with left=(add node.left key value)}
     else
       Node{node with right=(add node.right key value)}
;;

let tree_string map =
  let buf = Buffer.create 256 in

  let rec build tree depth =
    match tree with
    | Empty -> ()
    | Node(node) ->
       build node.right (depth+1);
       for i=1 to depth do
         Buffer.add_string buf "  ";
       done;
       let datastr =
         sprintf "%2d: %s\n" depth (KVMod.keyval_string node.key node.value)
       in
       Buffer.add_string buf datastr;
       build node.left (depth+1);
  in

  build map 0;
  Buffer.contents buf

let rec getopt map key =
  match map with
    | Empty ->
      None
    | Node(node) ->
      let diff = KVMod.compare_keys key node.key in
      if diff = 0 then
        Some (node.value)
      else if diff < 0 then
        getopt node.left key
      else
        getopt node.right key
;;

let contains_key map str =
  (getopt map str) <> None
;;

let rec iter func map = (*same as fold, but without a continuing element*)
  match map with
    | Empty -> ()
    | Node(node) ->
      iter func node.left;
      func node.key node.value;
      iter func node.right;
;;

let rec fold func cur map =
  match map with
    | Empty -> cur
    | Node(node) ->
      let temp = fold func cur node.left in (*fold over the lower indicies and return the new val*)
      let cur = func temp node.key node.value in (*fold over the current element*)
      fold func cur node.right (*fold over the higher stuff*)
;;

let to_string map =
  let sbuf = Buffer.create 256 in

  let append key value =
    Buffer.add_string sbuf ((KVMod.keyval_string key value)^", ");
  in

  let shorten buf =
    let len = Buffer.length buf in
    if len > 4 then
      Buffer.sub buf 0 (len-2)
    else
      Buffer.contents buf
  in

  Buffer.add_string sbuf "[";
  iter append map;
  (shorten sbuf)^"]"


;;


let rec findmin_keyval map =
  match map with
    | Empty -> failwith "No minimum in an empty tree"
    | Node(node) ->
      if node.left <> Empty then
        findmin_keyval node.left
      else
        node.key,node.value
;;

let rec remove_key map key =
  match map with
    | Empty -> Empty
    | Node(node) ->
      let diff = KVMod.compare_keys key node.key in
      if (diff < 0) then                              (*case where you don't need to remove anything from a branch*)
        Node{node with left=remove_key node.left key}
      else if (diff > 0) then                         (*case where you don't need to remove anything from a branch*)
        Node{node with right=remove_key node.right key}
      else                                            (*removal case*)
        match node.left,node.right with
          | Empty, Empty -> Empty (*both children are empty*)
          | Node(l), Empty -> (*left branch has something, promote it*)
            node.left
          | Empty, Node(r) -> (*right branch has something, promote it*)
            node.right
          | Node(l), Node(r) -> (*both branches have something, promote the smallest element connected to the right branch and remove it*)
          let keyval = findmin_keyval node.right in
            Node{key=(fst keyval);value=(snd keyval);left=node.left;right=(remove_key node.right (fst keyval))}
;;
end;;
