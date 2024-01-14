#include <unordered_map>

class Solution {
public:
    unordered_map<char, int> miMapa;

    int romanToInt(string s) {
        miMapa['I'] = 1;
        miMapa['V'] = 5;
        miMapa['X'] = 10;
        miMapa['L'] = 50;
        miMapa['C'] = 100;
        miMapa['D'] = 500;
        miMapa['M'] = 1000;
        int num_ant = 0;
        int sum = 0;
        for(int i=0; i< s.length(); i++){
            int num_actual = miMapa[s[i]];
            if(num_ant < num_actual){
                sum += num_actual - (2*num_ant);
                num_ant = num_actual;
            }else{
                sum+=num_actual;
                num_ant = num_actual;
            };
        };
    return sum;
    }
};