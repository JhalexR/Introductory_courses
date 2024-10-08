package Estructura_de_Datos.Tablas_Hash;

public class HashTable{
    Integer sizeHash;

    public HashTable(int size_1){
        sizeHash = size_1;
    }

    private Integer hash(Integer d){
        Integer key = 0;
        key = Math.abs(d)%sizeHash;
        return key;
    }

    public int insert (Integer x){
        int result = hash(x);
        return result;
    }

    public static void main(String[] args){
        HashTable table = new HashTable(41);
        int test;
        int aux []= {10, 49, 35, 95, 41, 37, 38, 31, 48, 23, 42, 20, 74, 52, 57, 54, 24, 98, 11, 67, 79, 82, 43, 33, 97, 40, 49, 68, 65, 45};
        for(int i=0; i<aux.length; i++){
            test = table.insert(aux[i]);
            System.out.println("x: es"+aux[i]+" f(x) es: "+test);
        }
    }
}