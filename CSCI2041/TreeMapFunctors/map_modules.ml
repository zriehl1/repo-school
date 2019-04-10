open Printf;;

module StringStringKV = struct
  type key_t = string;;
  type value_t = string;;
  let compare_keys key1 key2 = String.compare key1 key2;;
  let keyval_string key value = sprintf "{%s -> %s}" key value;;
end;;

module StringStringMap = Treemap.Make(StringStringKV);;

module IntpairBoolKV = struct
  type key_t = int*int;;
  type value_t = bool;;
  let compare_keys key1 key2 =
    let sum1 = (fst key1) - (fst key2) in
    let sum2 = (snd key1) - (snd key2) in
    if sum1 = 0 then
      sum2
    else
      sum1
  ;;
  let keyval_string key value=
    sprintf "{%d > %d : %s}" (fst key) (snd key) (string_of_bool value)
  ;;
end;;
module IntpairBoolMap = Treemap.Make(IntpairBoolKV);;
