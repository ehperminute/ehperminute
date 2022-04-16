df = pd.read_excel('shifted_tables.xlsx', engine='openpyxl', header=None)
dfcsv = df.to_csv(index=False, header=False)
frames = {}
for line in dfcsv.split('\n'):     
    line = line.strip(',')
    if 'Table' in line:
        current_table = line.split('=')[-1]
        frames[current_table] = []            
        continue
    if len(line.split(',')) > 1:
        frames[current_table].append(line.split(','))        
        
for framename, dframe in frames.items():
    frames[framename] = pd.DataFrame(dframe[1:], columns=[dframe[0]])
