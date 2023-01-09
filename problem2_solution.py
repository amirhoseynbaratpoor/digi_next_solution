import re
def no_rep(in_str):
    in_no_space = re.sub(" +", "", in_str)
    out = "".join(re.findall(r"(\w)\1*", in_no_space))
    num_repl = len(in_str) - len(out)
    return num_repl
	
no_rep("AABAAB")