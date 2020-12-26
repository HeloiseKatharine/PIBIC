package dto;

public class Paciente {

    private String cpf, nome;
    private int id_paciente;
    private int id_exame;

    public int getId_exame() {
        return id_exame;
    }

    public void setId_exame(int id_exame) {
        this.id_exame = id_exame;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getId_paciente() {
        return id_paciente;
    }

    public void setId_paciente(int id_paciente) {
        this.id_paciente = id_paciente;
    }

}
