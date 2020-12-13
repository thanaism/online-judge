# def xor(x,y):
#     return x^y

# class segtree:
#     def __init__(self, n,operator,identity):
#         nb = bin(n)[2:]
#         bc = sum([int(digit) for digit in nb])
#         if bc == 1:
#             self.num_end_leaves = 2**(len(nb)-1)
#         else:
#             self.num_end_leaves = 2**(len(nb))
#         self.array = [identity for i in range(self.num_end_leaves * 2)]
#         self.identity = identity 
#         self.operator =operator
#     def update(self,x,val):
#         actual_x = x+self.num_end_leaves
#         self.array[actual_x] = val
#         while actual_x>0:
#             actual_x=actual_x//2
#             self.array[actual_x] = self.operator(self.array[actual_x*2],self.array[actual_x*2+1])
#     def get(self,q_left,q_right,arr_ind=1,leaf_left=0,depth=0):
#         width_of_floor = self.num_end_leaves//(2**depth)
#         leaf_right = leaf_left+width_of_floor-1
#         if leaf_left > q_right or leaf_right < q_left:
#             return  self.identity
#         elif leaf_left >= q_left and leaf_right <= q_right:
#             return self.array[arr_ind]
#         else:
#             val_l = self.get(q_left,q_right,2*arr_ind,leaf_left,depth+1)
#             val_r = self.get(q_left,q_right,2*arr_ind+1,leaf_left+width_of_floor//2,depth+1)
#             return self.operator(val_l,val_r)

#####segfunc#####
def segfunc(x, y):
    return x^y
#################

#####ide_ele#####
ide_ele = 0
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():
    n,q=map(int,input().split())
    # seg=segtree(n,xor,0)
    a=[*map(int,input().split())]
    # b=0
    seg=SegTree(a,segfunc,ide_ele)
    # for i,v in enumerate(a):
    #     seg.update(i+1,v)
    for _ in range(q):
        t,x,y=map(int,input().split())
        if t==1:
            # seg.update(x-1,seg.array[x+seg.num_end_leaves]^y)
            seg.update(x-1,seg.query(x-1,x)^y)
        else:
            # print(seg.get(x-1,y))
            print(seg.query(x-1,y))

main()