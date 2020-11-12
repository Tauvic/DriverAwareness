import pandas as pd

tag_df = pd.read_csv('tmp/26122013_223310_cam.tag',
                 delimiter=':',
                 skiprows=19,
                 index_col = 0,
                 skipfooter=1,
                 engine='python',
                 names=['frameID', 'blinkID', 'NF', 'LE_FC', 'LE_NV', 'RE_FC', 'RE_NV', 'F_X', 'F_Y', 'F_W',
                        'F_H', 'LE_LX', 'LE_LY', 'LE_RX', 'LE_RY', 'RE_LX', 'RE_LY', 'RE_RX', 'RE_RY' ])

txt_df = pd.read_csv('tmp/26122013_223310_cam.txt',delimiter=' ', index_col=0, header=None,names=['frameID','time'])

df = pd.merge(txt_df, tag_df, how='inner',on='frameID')

print(df.head(20))
#print(df[df.blinkID!=-1].head(20))