package processoseletivo;

import java.util.ArrayList;
import java.util.Random;

public class ProcessoSeletivo {
    private static int salarioOferecido;
    private static ArrayList<String> candidatos;
    private static ArrayList<String> candidatosSelecionados;

    public static void main(String[] args) {
        System.out.println("=================================\n" + 
                            "|| Iniciando processo seletivo ||\n" +
                            "=================================");
        selecaoCandidatos();
        for (String candidato : candidatosSelecionados) {
            entrarEmContatoComCandidato(candidato);
        }
        System.out.println("\n===================================\n" + 
                            "|| Finalizando processo seletivo ||\n" +
                            "===================================");
    }

    public static void selecaoCandidatos() {
        int candidatoAtual = 0;
        candidatosSelecionados = new ArrayList<>();
        salarioOferecido = 2000;
        populateCandidateList();

        while (candidatosSelecionados.size() < 5 && candidatoAtual < candidatos.size()) {

            String candidato = candidatos.get(candidatoAtual);
            int salarioPretendido = valorPretendido();
                System.out.println("O candidato " + candidato + " pretende ganhar " + salarioPretendido + " Reais.");
                if (salarioOferecido >= salarioPretendido) {
                    System.out.println("O candidato " + candidato + " foi selecionado para a vaga.");
                    candidatosSelecionados.add(candidato);
                }
                candidatoAtual++;
        }

        System.out.println("\n=============================\n" + 
                            "|| Candidatos selecionados ||\n" +
                            "=============================");
        for (String candidato : candidatosSelecionados) {
            System.out.println(candidato);
        }
    }

    private static void populateCandidateList() {
        candidatos = new ArrayList<>();
        candidatos.add("Felipe");
        candidatos.add("Marcia");
        candidatos.add("Julia");
        candidatos.add("Monica");
        candidatos.add("Fabricio");
        candidatos.add("Pedro");
        candidatos.add("Jorge");
        candidatos.add("Ana");
        candidatos.add("Bruno");
        candidatos.add("Carla");
        candidatos.add("Danilo");
        candidatos.add("Eduardo");
        candidatos.add("Fernanda");
        candidatos.add("Gabriela");
    }

    public static int valorPretendido() {
        Random random = new Random();
        return random.nextInt(1501) + 1300;
    }

    public static void entrarEmContatoComCandidato(String candidato) {
        int tentativas = 0;
        System.out.println("\nEntrando em contato com o candidato " + candidato);
        do {
            tentativas++;
            System.out.println("Tentativa " + (tentativas) + " de contato.");
            if (atendeu()) {
                System.out.println("O candidato " + candidato + " atendeu a ligação.");
                break;
            } else {
                System.out.println("O candidato " + candidato + " não atendeu a ligação.");
            }
            
        } while (tentativas < 3);

        if (tentativas == 3) {
            System.out.println("O candidato " + candidato + " não atendeu a ligação após 3 tentativas.");
        }
        
    }

    static boolean atendeu() {
        int random = new Random().nextInt(3);
        return (random == 1);
    }


}
