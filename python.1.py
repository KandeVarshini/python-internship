def remove_sql_specialists(people_list):
    result=[]
    for person in people_list:
      if "sql" not in person[1]:
         result.append(person)
    return result
new_hires=[("mark adams","sql analyst",4000),("leslie burton","hr specialist",2300),("dorothy castillo","ux designer",3100)]
filtered_hires=remove_sql_specialists(new_hires)
print(filtered_hires)
