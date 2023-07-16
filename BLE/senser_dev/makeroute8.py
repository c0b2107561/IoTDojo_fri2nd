import ujson
from collections import OrderedDict

class RouteMake:
    def _readtxt(self):
        split = []
        with open("data/makeroute_data.txt",'r',encoding="utf-8")as f:
            data = f.readlines()
            for i in range(len(data)):
                # if data[i] in '\n':
                #     data[i].replace('\n' , '')
                data[i] = data[i].split('_')
                for j in range(len(data[i])):
                    #print(data[0][0])
                    if '\r' in data[i][j]:
                        data[i][j] = data[i][j].replace('\r', '')
                    if '\n' in data[i][j]:
                        data[i][j] = data[i][j].replace('\n', '')
                split.append(data[i])
            print(split)
            f.close()
            return split
        
    def _makeval(self,split):
        with open("data/packet_table.json", 'r', encoding="utf-8") as f:
            table= ujson.load(f)
            print("@@@@@")
            print(table)
            print(split)
            print(type(table))
            # for key in table.keys():
            #     print(key)
            print('---------')
            lis = []

            for i in range(len(split)):
                ls = []
                for list in split[i][:-2]:
                    print(list)
                    # print(type(list))
                    ls.append(table[list])
                lis.append(ls)
            print(lis)
            return lis

    def _makekey(self, lis):
        print("$$$$$$$$$")
        _lis = []
        for i in range(len(lis)):
            _ls = []
            for j in range(len(lis[i])):
                if j == 0:
                    _ls.append('senser'+ str(i) + str(j))
                else:
                    _ls.append('relay'+ str(i) + str(j))
            _lis.append(_ls)
        print(_lis)
        return _lis

    def _dict(self,split, val, key):
        print("##########")
        print(val)
        print(key)
        for i in range(len(key)):
            print(key[0])
            if i is 0:
                dic= OrderedDict(zip(key[i],val[i]))
                print(dic)
                print("&&&&&")
                hopnum = split[i][-2]
                dic['hop'+str(i)] = hopnum
                rank = split[i][-1]
                dic['rank'+str(i)] = rank
                print(dic)
            else:
                dic.update(OrderedDict(zip(key[i],val[i])))
                print("######")
                print(dic)
                hopnum = split[i][-2]
                dic['hop'+str(i)] = hopnum
                rank = split[i][-1]
                dic['rank'+str(i)] = rank
                print(dic)
        return dic
    
    def _json(self, dic):
        with open('data/routeinfo.json','w',encoding="utf-8") as f:
            num = len(dic)
            print(num)
            #json.dump(dic,f,indent=num)
            ujson.dump(dic,f)


def _routemake():
    rm = RouteMake()
    split = rm._readtxt()
    val = rm._makeval(split)
    key =rm._makekey(val)
    dic = rm._dict(split,val,key)
    rm._json(dic)


if __name__ == "__main__":
    _routemake()