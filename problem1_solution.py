def swap_num(in_text: str, num_max: int):
    num_max = 10
    len_a = len(in_text)
    c = 1
    while True:
        if len(in_text)>l_to_reach:
            in_text = in_text[:l_to_reach]
            break
        in_text += in_text
    
    return in_text.count("a"), in_text 
    
num_str, out_text = swap_num("aba", 10)