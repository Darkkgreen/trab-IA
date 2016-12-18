import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.TreeSet;

/**
 * Created by Charizard on 12/17/2016.
 */
public class Main {
    private int k_value = 5;

    public void main( String []args ) {
        Object novo;
        ArrayList<Object> listaObjetos = null;
        Scanner scan = new Scanner(System.in);
        String entrada = "-";
        String[] entryObj;
        String saida = null;


        try{
            listaObjetos = recebeTestes();
        }catch(Exception e){
            System.out.println(e);
        }

        while(entrada != null){
            entrada = scan.next();
            entryObj = entrada.split(",");
            novo = new Object(treatPrice(entryObj[0]), treatPrice(entryObj[1]), treatDoors(entryObj[2]), treatPeople(entryObj[3]), treatLug(entryObj[4]), treatSafety(entryObj[5]));

            //aqui precisa chamar o tratador, receber o resultado e remover as variáveis (além de adicionar o objeto à nova lista)
            saida = classifica(novo, listaObjetos);
            novo.setClassificacao(saida);
        }
    }

    public String classifica(Object novo, ArrayList<Object> listaObjs){
        TreeSet<Object> topK;

        //precisa saber o tamanho máximo de K
        //ir atualizando o TreeSet e fazendo as devidas comparações
        //ao final da análise, verificar o treeSet e categorizar a nova inserção

        return "alalalal";
    }

    public ArrayList<Object> recebeTestes() throws FileNotFoundException{
        ArrayList<Object> listaObjetos = new ArrayList<Object>();
        Object novo = null;

        FileInputStream fis = new FileInputStream("arquivo vem aqui");
        Scanner reader = new Scanner(fis);

        String[] element;

        while(reader.hasNextLine()){
            element = reader.nextLine().split(",");
            novo = new Object(treatPrice(element[0]), treatPrice(element[1]), treatDoors(element[2]), treatPeople(element[3]), treatLug(element[4]), treatSafety(element[5]), element[6]);
            listaObjetos.add(novo);
            novo = null;
        }

        return listaObjetos;
    }

    public int treatPrice(String value){
        if(value.equals("v-high")){
            return 1;
        }else if(value.equals("high")){
            return 2;
        }else if(value.equals("med")){
            return 3;
        }else if(value.equals("low")) {
            return 4;
        }else
            return Integer.parseInt(value);
    }

    public int treatDoors(String value){
        if(value.equals("5-more")){
            return 5;
        }else
            return Integer.parseInt(value);
    }

    public int treatPeople(String value){
        if(value.equals("more")){
            return 5;
        }else
            return Integer.parseInt(value);
    }

    public int treatLug(String value) {
        if (value.equals("small")) {
            return 1;
        } else if (value.equals("med")) {
            return 2;
        } else if (value.equals("big")) {
            return 3;
        }

        return 0;
    }

    public int treatSafety(String value){
        if (value.equals("low")) {
            return 1;
        } else if (value.equals("med")) {
            return 2;
        } else if (value.equals("high")) {
            return 3;
        }

        return 0;
    }
}