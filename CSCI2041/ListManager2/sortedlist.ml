
let rec insert lst elem =
  match lst with
  |[] -> [elem]
  | a :: b when a = elem -> insert b elem
  | a :: b when a > elem -> elem :: a :: b
  | a :: b -> a :: (insert b elem) (*catch-all case that only actually catches the less than case*)
;;


let rec remove lst elem =
  match lst with
  |[] -> []
  |a :: b when a = elem -> b
  |a :: b when a < elem -> a :: remove b elem
  |a :: b -> lst (*catch-all case than only actually catches the greater than case*)
;;

let rec print strlist =
  match strlist with
  |[] -> ()
  |a :: b ->
    Printf.printf "%s\n" a;
    print b
;;
let rec merge list1 list2 =
  match list1,list2 with
  |[], [] -> [] (*list1 and list2 empty means that you're done*)
  |[], a2::b2 -> a2 :: merge [] b2 (*list1 empty, but keep adding elements from list2*)
  |a1::b1, [] -> a1 :: merge b1 [] (*above but backwards*)
  |a1::b1, a2::b2 when a1 < a2 -> a1 :: merge b1 list2 (*list1 elem bigger than list2 elem, continue with list1, keep same list2*)
  |a1::b1, a2::b2 when a1 = a2 -> a1 :: merge b1 b2 (*list1 and list2 elem equal, put one in and proceed with both lists*)
  |a1::b1, a2::b2 -> a2 :: merge list1 b2 (*backwards less than case*)
;;
