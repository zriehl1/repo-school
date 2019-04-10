let array_rev arr =
  let arr_len = Array.length arr in
  for i = 0 to (arr_len/2) -1 do
    let temp = arr.(i) in
    arr.(i) <- arr.(arr_len - (1 + i));
    arr.(arr_len - (1+i)) <- temp;
  done;
;;

let list_rev lst =
  let rec helper lst r_lst =
    if lst = [] then
      r_lst
    else
      let new_l = List.hd lst :: r_lst in
      helper (List.tl lst) new_l
  in
  helper lst []
;;
