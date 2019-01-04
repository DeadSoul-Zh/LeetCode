int hammingDistance(int x,int y) {
    int res, ext;
    ext = x ^ y;
    res = 0;
    while (ext) {
        res++;
        ext &= (ext - 1);
    }
   return res;
}