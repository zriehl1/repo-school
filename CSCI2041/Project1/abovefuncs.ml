let array_above thresh arr =
  if arr = [||] then (* if input is empty array return empty array*)
    [||]
  else
  let arr_len = Array.length arr in
  let counter = ref 0 in
  for i=0 to arr_len-1 do (*counts the number of elements above the thresh *)
    if thresh < arr.(i) then
      counter := !counter + 1;
    done;
  let new_arr = Array.make !counter arr.(0) in
  let place = ref 0 in
  for i=0 to arr_len-1 do (*places elements above the thresh into the new array *)
    if thresh < arr.(i) then
      begin
      new_arr.(!place) <- arr.(i);
      place := !place + 1;
      end;
    done;
  new_arr;;

let rec list_above thresh lst =
  let remain = List.length lst in
  if remain = 0 then (* base case *)
    []
  else if thresh < List.hd lst then (*recursive when above thresh *)
    List.hd lst :: list_above thresh (List.tl lst)
  else              (* recursive when below thresh *)
    list_above thresh (List.tl lst)

;;
