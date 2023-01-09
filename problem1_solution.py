def ahbp(in_text: str, num_max: int):
    len_a = len(in_text)
    while True:
        if len(in_text)>num_max:
            in_text = in_text[:num_max]
            break
        in_text += in_text
    
    return in_text.count("a"), in_text 
    
num_str, out_text = ahbp("aba", 10)
print(f"string: {out_text}")
print(f"The number of characters a: {num_str}")
