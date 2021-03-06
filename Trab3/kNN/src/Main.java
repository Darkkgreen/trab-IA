import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.util.*;

/**
 * Created by Charizard on 12/17/2016.
 */
public class Main {
    private static int k_value = 5;

    public static void main( String []args ) {
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

        System.out.println("Please insert your info: ");

        while(entrada != null){
            entrada = scan.next();
            entryObj = entrada.split(",");
            novo = new Object(treatPrice(entryObj[0]), treatPrice(entryObj[1]), treatDoors(entryObj[2]), treatPeople(entryObj[3]), treatLug(entryObj[4]), treatSafety(entryObj[5]));

            saida = classifica(novo, listaObjetos);
            novo.setClassificacao(saida);

            System.out.println("Classified as " + saida);

            listaObjetos.add(novo);
            saida = "";
            novo = null;
            entryObj = null;
            entrada = "-";
        }
    }

    public static String classifica(Object novo, ArrayList<Object> listaObjs){
        ArrayList<Object> topK = new ArrayList<>();
        Iterator<Object> it = listaObjs.iterator();
        Hashtable<String, Integer> mapa = new Hashtable<String, Integer>();

        Integer auxiliar, maior = 0;
        Integer total = 0;
        String retorno = "";

        while(it.hasNext()){
            Object aux = it.next();
            aux.setDist(novo.calcDist(aux));

            if(topK.size() < k_value){
                topK.add(aux);
            }else{
                //printList(topK);
                if(topK.get(topK.size()-1).getDist() > aux.getDist()){
                    topK.remove(topK.size()-1);
                    topK.add(aux);
                }
                //printList(topK);
            }

            Collections.sort(topK);
        }

        Collections.sort(listaObjs);
        printList(listaObjs);

        for(Object aux: topK){
            if(mapa.containsKey(aux.getClassificacao())){
                auxiliar = mapa.get(aux.getClassificacao());
                mapa.put(aux.getClassificacao(), auxiliar+1);
            }else{
                mapa.put(aux.getClassificacao(), 1);
            }
            //System.out.println(aux.getClassificacao());
        }

        for(Object aux: topK){
            auxiliar = mapa.get(aux.getClassificacao());
            if(auxiliar > maior){
                maior = auxiliar;
                retorno = aux.getClassificacao();
            }
        }

        return retorno;
    }

    public static void printList(ArrayList<Object> tree){
        Iterator<Object> it = tree.iterator();
        Object aux;

        while(it.hasNext()){
            aux = it.next();
            System.out.println(aux.getDist() + "( " + aux.getClassificacao() + " " + aux.retornaValores() + " ) ");
        }
    }

    public static ArrayList<Object> recebeTestes() throws FileNotFoundException{
        ArrayList<Object> listaObjetos = new ArrayList<Object>();
        Object novo = null;

        FileInputStream fis = new FileInputStream("C:\\Users\\Charizard\\IdeaProjects\\kNN\\src\\teste.txt");
        Scanner reader = new Scanner(fis);

        String[] element;

        while(reader.hasNextLine()){
            element = reader.nextLine().split(",");
            novo = new Object(treatPrice(element[0]), treatPrice(element[1]), treatDoors(element[2]), treatPeople(element[3]), treatLug(element[4]), treatSafety(element[5]), element[6]);
            listaObjetos.add(novo);
        }

        System.out.println("Lines read: " + listaObjetos.size());
        System.out.println("Done loading archive!");

        return listaObjetos;
    }

    public static int treatPrice(String value){
        if(value.equals("vhigh")){
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

    public static int treatDoors(String value){
        if(value.equals("5more")){
            return 5;
        }else
            return Integer.parseInt(value);
    }

    public static int treatPeople(String value){
        if(value.equals("more")){
            return 5;
        }else
            return Integer.parseInt(value);
    }

    public static int treatLug(String value) {
        if (value.equals("small")) {
            return 1;
        } else if (value.equals("med")) {
            return 2;
        } else if (value.equals("big")) {
            return 3;
        }

        return 0;
    }

    public static int treatSafety(String value){
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