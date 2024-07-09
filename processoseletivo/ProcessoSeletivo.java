package processoseletivo;

public class ProcessoSeletivo {
    private static int salarioOferecido;

    public static void main(String[] args) {
        System.out.println("Iniciando processo seletivo");
    }

    public static void analisarCandidato(double salarioPretendido) {
        salarioOferecido = 2000;
        if (salarioOferecido > salarioPretendido) {
            System.out.println("Ligando para o candidato");
        } else if (salarioOferecido == salarioPretendido) {
            System.out.println("Orferecer contraproposta");
        } else {
            System.out.println("Aguardando resultados dos demais candidatos");
        }
    }
}
