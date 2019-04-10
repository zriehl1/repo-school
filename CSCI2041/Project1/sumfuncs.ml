let array_sum arr =
  let len = Array.length arr in
  let sum = ref 0 in
  for i = 0 to len-1 do (* iterates through the array and sums the elements using a ref *)
    let temp = !sum + arr.(i) in
    sum := temp;
    done;
  !sum
  ;;

let rec list_sum lst =
  let remaining = List.length lst in
  if remaining = 0 then
    0
  else
    List.hd lst + list_sum (List.tl lst)
;;
