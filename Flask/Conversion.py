def compare_lines_with_dict(input_text, dictionary):
 lines = input_text.split('\n')
 matching_values = []
 for line in lines:
    matching_value = ""
    found_match=False
    for key in dictionary:
     if key in line:
       matching_value += dictionary[key]
       found_match=True
       break 
    if found_match==False:
       matching_value += "NOT-FOUND"
       
    matching_values.append(matching_value)
    ans=matching_values[0:]
    answer="\n".join(ans)
 return answer
