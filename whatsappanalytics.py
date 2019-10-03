import pandas as pd
import numpy as np
#importing the files
filename=r"insert file name here"
newfile=r"insert new file name here"

#parsing the file
df=pd.read_fwf(filename,header=None,usecols=[0])
df1=pd.DataFrame(df[0].str.split('-',expand=True))
df2=pd.DataFrame(df1[1].str.split(':',expand=True))
data=df2[0]
#buliding a dictionary to count number of messages
counts={}
for i in data:
    if i in counts.keys():
        counts[i]+=1
    else:
        counts[i]=1

#converting a dictionary to a list
# lcounts=[]
# for key, value in counts.items():
#     temp = key,value
#     lcounts.append(temp)


#converting dictionary to a dataframe
dfcounts=pd.DataFrame(list(counts.items()), columns=['Name', 'Numberofmessages'])
df2counts=dfcounts[(dfcounts.Numberofmessages>20)].copy()

#setting an index
#df2counts.index = range(len(df2counts))
df2counts=df2counts.sort_values('Numberofmessages',ascending=False)
#df2counts.index = range(len(df2counts))
df2counts.index = np.arange(1, len(df2counts) + 1)
#removing a particular row
df2counts.drop(df2counts.index[[10,12]], inplace=True)
df2counts.index = np.arange(1, len(df2counts) + 1)
print(df2counts)

#plotting the data
# ax = df2counts[['Name','Numberofmessages']].plot(kind='bar', title ="Most active members of the group", figsize=(15, 10), legend=True, fontsize=12)
# ax.set_xlabel("Name", fontsize=12)
# ax.set_ylabel("Numberofmessages", fontsize=12)
# plt.show()


#writing it to a text file
# df2counts.to_csv(r"C:\Users\sai yarra\Downloads\counts.csv", header=True, index=None, sep='\t', mode='a')

#converting it to a json file

# jcounts=json.dumps(counts)











# with open(newfile, 'w') as outfile:
#     json.dump(jcounts, outfile)
# print(jcounts)
# for key, value in counts.items():
#     temp = [key,value]
#     dictlist.append(temp)
#
# with open('newfile', 'wb') as fp:
#     pickle.dump(dictlist, fp)
#
# with open ('newfile', 'rb') as fp:
#     itemlist = pickle.load(fp)
#
# print(itemlist)
