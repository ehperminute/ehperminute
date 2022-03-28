def df_to_test(df, opts=4, nq=10):
    assert 1 < opts <= len(df.index)    
    assert 0 < nq <= len(df.index)    
    return pd.DataFrame.from_dict({q: a.tolist() + random.sample(a.tolist() + df[df.index != q].sample(opts-1).iloc[:, 0].tolist(), k=opts) 
                        for q, a in df.sample(nq).iterrows()}, orient='index').rename(columns = {0: 'correct'})

data = {'rus': [chr(i) for i in range(1072, 1083)], 'eng': [chr(i) for i in range (97, 108)]}
df = pd.DataFrame(data)
df = df.set_index('rus')
test = df_to_test(df, nq=10, opts=4)