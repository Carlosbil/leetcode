class Solution {
 public:
    bool isPalindrome(int x) {
        // Los números negativos y aquellos que terminan en 0 (excepto 0) no son palíndromos
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        // convertimos unidades en decenas, centas ... ...
        // dejando un hueco para añadir el primer numero de X al principio de esta nueva lista
        // al ser palindromo, se lee igual empezando desde el final, el nuevo construido , que desde el principio
        // por tanto invirtiendo solo la mitad, es más que suficiente para comparar
        int reversedHalf = 0;
        while (x > reversedHalf) {
            reversedHalf = reversedHalf * 10 + x % 10;
            x /= 10;
        }
        // teniendo en cuenta que el numero de cifras sea impar
        return x == reversedHalf || x == reversedHalf / 10;
    }
};