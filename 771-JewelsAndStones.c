int numJewelsInStones(char* J, char* S) {
    int i,j,k;
    i = k = 0;
    while(S[i] != '\0') {
        j = 0;
        while(J[j] != '\0') {
            if (S[i] == J[j]) {
                k += 1;
                break;
            }
            j++;
        }
        i++;
    }
    return k;
}